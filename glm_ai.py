import requests
import json


url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

payload = {  # type: ignore
    "model": "glm-4v-flash",
    "messages": [
        {"role": "system", "content": "You are a helpful assiantant."},
        {"role": "user", "content": "Hello! I'm GLM 4.7 Flash."}
    ],
    "stream": True,
    "temperature": 1
}

headers = {
    "Authorization": "Bearer f76449fad5eb4aaabd5c25e1a1fdc524.hiGxkcdkTXYK0t8A",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers, stream=True, verify=True)  # type: ignore

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
                print(content, end="", flush=True)  # TODO: Make it into function and not use print.
            except Exception as e:
                print(e)
