import json

from message import MessageInfo


class Session:
    """The current session of the agent"""
    _instance = None

    def __new__(cls, *args, **kwargs): # type: ignore
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            background = open("background.md", "r", encoding="utf-8").read()
            skill = open("skills/skill.md", "r", encoding="utf-8").read()
            cls._instance.history = [{"role": "system", "content": background+"\n"+skill}] # pyright: ignore[reportAttributeAccessIssue]
        return cls._instance
    
    def add_message(self, message: MessageInfo) -> None:
        """Add message into it.
        Args:
            message (MessageInfo): The message you want to insert
        """
        self.history.append(message) # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]

    add_msg = add_message

    def to_json(self, file) -> None: # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
        """Write the history list to .json file.
        Args:
            file: The json file you want to save the list
        """
        with open(file, "a", encoding="utf-8") as f: # pyright: ignore[reportUnknownArgumentType]
            json.dump(self.history, f) # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]


session = Session()
