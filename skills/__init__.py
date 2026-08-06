import os
from typing import Any

from generate import (
    load_all_skills,
    generate_tool_call_schema,
)
from base_skill import BaseSkill


__all__ = (
    "skills",
    "schema_dict",
    "run_skill",
)


os.chdir(os.path.dirname(__file__))

skills = load_all_skills() # pyright: ignore[reportUnknownVariableType]

schema_dict = {}
for skill in skills: # pyright: ignore[reportUnknownVariableType]
    try:
        schema_dict[skill.name] = generate_tool_call_schema(skill) # pyright: ignore[reportUnknownMemberType]
    except Exception as e:
        print(f"Can't generate schema for {skill.name}: {e!r}") # pyright: ignore[reportUnknownMemberType]

print("Skills:", [s.name for s in skills]) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType, reportUnknownVariableType]
print(schema_dict) # pyright: ignore[reportUnknownArgumentType]

def run_skill(name: str, *args, **kwargs) -> Any: # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
    for skill in skills: # pyright: ignore[reportUnknownVariableType]
        if skill.name == name: # pyright: ignore[reportUnknownMemberType]
            return skill.run(*args, **kwargs) # pyright: ignore[reportUnknownMemberType]
    return f"Skill {name} not found"

def generate_md():
    try:
        with open("skill.md", "w", encoding="utf-8") as file:
            file.write(f"""You have some skills that can call:{[s.name for s in skills]}.
Call the skills with arguments.
Here are the schemas:
{schema_dict}""")
    except Exception as exc:
        print(f"Can't generate MarkDown:{exc!r}")

generate_md()

def add_skill(name: str, content: str) -> tuple[list[BaseSkill], dict[Any, Any]]:
    global skills, schema_dict
    try:
        with open(f"{name}_skill.py", "w", encoding="utf-8") as file:
            file.write(content)
        skills = load_all_skills()
        schema_dict = {}
        for skill in skills: # pyright: ignore[reportUnknownVariableType]
            try:
                schema_dict[skill.name] = generate_tool_call_schema(skill) # pyright: ignore[reportUnknownMemberType]
            except Exception as e:
                print(f"Can't generate schema for {skill.name}: {e!r}") # pyright: ignore[reportUnknownMemberType]
        generate_md()
    except Exception as e:
        print(f"Some error occured:{e!r}")
    return skills, schema_dict # pyright: ignore[reportUnknownVariableType]
