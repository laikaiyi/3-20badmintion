from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from waitress import serve
import inspect

# 初始化 Flask 應用程式
app = Flask(__name__)

# 用你實際的值替換 'YOUR_CHANNEL_ACCESS_TOKEN' 和 'YOUR_CHANNEL_SECRET'
line_bot_api = LineBotApi('FgRwDsmCC055uMWW/YTiv/X/+vP+WzYMz/X6nl9wde6iaB/Q/C1chDgrGCDxHJVnK5mcR8wJmKuYCT5ck5OGRbw1e6BW9C9JtQaQIQefuomJ4vpmmpmmpMr; gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d59461ed36fad764c35e258a67fe724f')

@app.route("/callback", methods=['POST'])
def callback():
    # 獲取 X-Line-Signature 請求頭的值
    signature = request.headers['X-Line-Signature']

    # 將請求體以文本形式獲取
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # 處理 webhook 請求體
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 回應收到的文本訊息
    reply_text = f"Echo: {event.message.text}"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

# 在主程式塊中使用 Waitress 作為伺服器
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)

import inspect

def sample_function(arg1, arg2='default', *args, kwarg1, kwarg2='kwdefault', **kwargs):
    pass

sig = inspect.signature(sample_function)
parameters = sig.parameters
print("Parameters:")
for name, param in parameters.items():
    print(f"{name}: {param.kind}, default={param.default}")
