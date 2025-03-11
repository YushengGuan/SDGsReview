import requests

# Owner: Yusheng Guan. Please replace the api into yours ones
api = 'sk-xmnatxfdmblzucppfxepbqirbcrqnlisdbdembmjjnvwemgh'


def gen_result(txt, mode):
    if mode == 'V3':
        if 'content' in txt and 'finish' in txt:
            return txt[txt.find('content')+10:txt.find('finish')-4]
        else:
            return txt
    elif mode == 'R1':
        if 'content' in txt and 'finish' in txt and 'reasoning' in txt:
            return [txt[txt.find('content')+10:txt.find('reasoning')-3], txt[txt.find('reasoning')+20:txt.find('finish')-4]]
        else:
            return [-1, txt]


def siliconflow(prompt, system="你是一个科学文献总结助手，请你读取英文文章，并根据文章内容严格按照用户要求回答问题。"):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
        "temperature": 0.7,
        "response_format": {"type": "text"},
    }
    headers = {
        "Authorization": "Bearer "+api,
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return gen_result(response.text, 'R1')