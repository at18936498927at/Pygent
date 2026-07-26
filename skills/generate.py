import inspect
import os
import importlib
import re
from typing import Any, Callable, Dict, List
from base_skill import BaseSkill


def get_function_signature(func: Callable[..., Any]) -> Dict[str, Any]:
    sig = inspect.signature(func)
    doc = inspect.getdoc(func) or ""
    param_descriptions: Dict[str, str] = {}
    param_enums: Dict[str, List[Any]] = {}

    lines = [line.strip() for line in doc.splitlines()]
    in_args_section = False

    # 匹配枚举行，例如：choices: [a, b, c] 或 enum: [x, y]
    enum_pattern = re.compile(r"(?:choices|enum)\s*:\s*\[(.*)\]", re.IGNORECASE)

    for line in lines:
        if line.startswith("Args:"):
            in_args_section = True
            continue
        if line.startswith(("Returns:", "Raises:", "Examples:")):
            in_args_section = False
        if in_args_section and line:
            parts = line.split(":", 1)
            if len(parts) == 2:
                param_name = parts[0].strip().split()[0]
                desc_part = parts[1].strip()

                # 分离描述和枚举
                enum_match = enum_pattern.search(desc_part)
                if enum_match:
                    enum_str = enum_match.group(1)
                    # 提取枚举值
                    enum_list = [s.strip().strip("'\"") for s in enum_str.split(",") if s.strip()]
                    param_enums[param_name] = enum_list
                    # 去掉枚举部分，保留纯描述
                    desc_part = enum_pattern.sub("", desc_part).strip()

                param_descriptions[param_name] = desc_part

    params: Dict[str, Dict[str, Any]] = {}
    for name, param in sig.parameters.items():
        ann = param.annotation
        type_name = ann.__name__ if hasattr(ann, "__name__") else str(ann).replace("typing.", "")
        has_default = param.default is not inspect.Parameter.empty

        params[name] = {
            "type": type_name,
            "default": param.default if has_default else None,
            "required": not has_default,
            "description": param_descriptions.get(name, ""),
            "enum": param_enums.get(name, []),  # 新增枚举
        }

    ret_ann = sig.return_annotation
    return_type = ret_ann.__name__ if hasattr(ret_ann, "__name__") else str(ret_ann).replace("typing.", "")

    return {
        "parameters": params,
        "signature": str(sig),
        "return_type": return_type
    }


def extract_tool_info(skill: BaseSkill) -> Dict[str, Any]:
    run_sig = get_function_signature(skill.run)
    return {
        "name": skill.name,
        "description": skill.description,
        "parameters": run_sig["parameters"],
        "return_type": run_sig["return_type"]
    }


def generate_tool_call_schema(skill: BaseSkill) -> Dict[str, Any]:
    info = extract_tool_info(skill)

    schema = { # pyright: ignore[reportUnknownVariableType]
        "type": "function",
        "function": {
            "name": info["name"],
            "description": info["description"],
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }

    type_map = {
        "int": "integer",
        "float": "number",
        "str": "string",
        "bool": "boolean",
        "list": "array",
        "dict": "object",
        "NoneType": "null",
    }

    properties = schema["function"]["parameters"]["properties"] # pyright: ignore[reportUnknownVariableType]
    required = schema["function"]["parameters"]["required"] # pyright: ignore[reportUnknownVariableType]

    for name, detail in info["parameters"].items():
        json_type = type_map.get(detail["type"], "string")
        prop = { # pyright: ignore[reportUnknownVariableType]
            "type": json_type,
            "description": detail["description"] or f"Parameter {name}"
        }
        # 加入 enum
        if detail.get("enum"):
            prop["enum"] = detail["enum"]

        properties[name] = prop
        if detail["required"]:
            required.append(name) # pyright: ignore[reportUnknownMemberType]

    return schema # pyright: ignore[reportUnknownVariableType]


def find_all_skill_files() -> Dict[str, BaseSkill]:
    """扫描当前目录所有 xxx_skill.py 并加载 XxxSkill 类"""
    skills: Dict[str, BaseSkill] = {}
    files = os.listdir()

    for fname in files:
        if not fname.endswith("_skill.py"):
            continue
        if fname.startswith(("_", ".")):
            continue

        mod_name = fname[:-3]
        try:
            mod = importlib.import_module(mod_name)
        except Exception:
            continue

        for attr_name in dir(mod):
            attr = getattr(mod, attr_name)
            if (
                isinstance(attr, type)
                and issubclass(attr, BaseSkill)
                and attr != BaseSkill
            ):
                try:
                    inst = attr()
                    skills[inst.name] = inst
                except Exception:
                    continue
    return skills


def load_all_skills() -> List[BaseSkill]:
    return list(find_all_skill_files().values())


def generate_all_schemas() -> List[Dict[str, Any]]:
    return [generate_tool_call_schema(s) for s in load_all_skills()]

