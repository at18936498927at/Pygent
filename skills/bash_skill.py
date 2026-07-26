import subprocess as sp
from typing import Any, List

from base_skill import BaseSkill


class BashSkill(BaseSkill):
    name = "bash"
    description = "Execute bash/system commands safely."

    def run(self, args: List[Any]) -> tuple[bytes, bytes, int]:
        """
        Run a bash command with arguments.
        
        Args:
            args: Command and arguments as a list, e.g. ["ls", "-l"]

        Returns:
            A tuple containing (stdout, stderr, returncode)
        """
        process = sp.run(
            args,
            capture_output=True,
            shell=False
        )
        return process.stdout, process.stderr, process.returncode
    
