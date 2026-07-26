from typing import Any


class BaseSkill:
    name: str
    description: str

    def run(self, args: Any) -> Any:
        ...

