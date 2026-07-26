from constants import MessageType


class MessageInfo:
    """The info of the message, contains the type and the message"""
    def __init__(self, type: MessageType, msg: str):
        self.type = type
        self.msg = msg

    def __str__(self) -> str:
        return self.msg
    
    def __repr__(self) -> str:
        return self.type.value + "{" + self.msg + "}"


def HumanMessage(msg: str) -> MessageInfo:
    """The message send by human"""
    return MessageInfo(MessageType.Human, msg=msg)


def AIMessage(msg: str) -> MessageInfo:
    """The message send by AI"""
    return MessageInfo(MessageType.AI, msg=msg)


def ToolMessage(msg: str) -> MessageInfo:
    """The message send by the tool call"""
    return MessageInfo(MessageType.Tool, msg=msg)


def SystemMessage(msg: str) -> MessageInfo:
    """The message by system"""
    return MessageInfo(MessageType.System, msg=msg)

