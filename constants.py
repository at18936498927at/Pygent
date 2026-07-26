from enum import Enum


class MessageType(Enum):
    Human = "Human"
    AI = "AI"
    Tool = "Tool"
    System = "System"

