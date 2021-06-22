import requests


def push_text(msg: str, token: str) -> str:
    data = {
        "template": "markdown",
        "token": token,
        "title": "天翼云盘自动化结果通知",
        "content": msg.replace(" ", "&nbsp;").replace("\n", "  \n")
    }
    response = requests.post("http://www.pushplus.plus/send", data=data)

    try:
        j = response.json()
        return j['msg'] if j['data'] is None else j['data']
    except ValueError:
        return response.text
