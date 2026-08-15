import json
import os
from typing import Literal

import requests
from dotenv import load_dotenv

from message import AIMessage, HumanMessage
from session import session

load_dotenv()
url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

type GLMModels = Literal["glm-4v-flash", 
                         "glm-4.6v-flash", 
                         "glm-4.7-flash", 
                         "glm-4.1v-thinking-flash", 
                         "glm-4-flash-250414", 
                         "Cogview3-Flash", 
                         "CodVideoX-Flash"]


def stream_response(msg: str,  # type: ignore[reportUnknownParameterType]
                    model: GLMModels="glm-4v-flash", 
                    environ_name: str="GLM_API_KEY",
                    temperature: float=1) -> AIMessage: # type: ignore
    session.add_msg(HumanMessage(msg=msg))
    payload = {  # type: ignore
        "model": model,
        "messages": session.history, # type: ignore
        "stream": True,
        "temperature": temperature,
    }

    key = os.getenv(environ_name, "")

    headers = {
        "Authorization": f"Bearer {key}", 
        "Content-Type": "application/json"
    }

    response = requests.post(url, 
                             json=payload, # type: ignore
                             headers=headers, 
                             stream=True, 
                             verify=True)

    all_content: str = ""

    for line in response.iter_lines():
        if line:
            line_str = line.decode('utf-8')
            if line_str.startswith('data: [DONE]'):
                break
            if line_str.startswith('data: '):
                json_str = line_str[5:]
                try:
                    data = json.loads(json_str)
                    content = data["choices"][0]["delta"].get("content", "")
                    all_content += content
                    print(content, end="", flush=True)  # TODO: Use func.
                except Exception as e:
                    print(e)
    return AIMessage(msg=all_content)
