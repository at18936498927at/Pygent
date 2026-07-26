import os

from generate import (
    load_all_skills,
    generate_tool_call_schema
)


__all__ = (
    "skills",
    "schema_dict",
)


os.chdir(os.path.dirname(__file__))

skills = load_all_skills() # pyright: ignore[reportUnknownVariableType]

schema_dict = {}
for skill in skills: # pyright: ignore[reportUnknownVariableType]
    try:
        schema_dict[skill.name] = generate_tool_call_schema(skill) # pyright: ignore[reportUnknownMemberType]
    except Exception as e:
        print(f"Can't generate schema for {skill.name}: {e}") # pyright: ignore[reportUnknownMemberType]

print("Skills:", [s.name for s in skills]) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType, reportUnknownVariableType]
print(schema_dict) # pyright: ignore[reportUnknownArgumentType]
