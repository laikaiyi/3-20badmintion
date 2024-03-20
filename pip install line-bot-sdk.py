from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from waitress import serve

# 初始化 Flask 应用
app = Flask(__name__)

# 用你实际的值替换 'YOUR_CHANNEL_ACCESS_TOKEN' 和 'YOUR_CHANNEL_SECRET'
line_bot_api = LineBotApi('FgRwDsmCC055uMWW/YTiv/X/+vP+WzYMz/X6nl9wde6iaB/Q/C1chDgrGCDxHJVnK5mcR8wJmKuYCT5ck5OGRbw1e6BW9C9JtQaQIQefuomJ4vpmmpmmpMr; gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d59461ed36fad764c35e258a67fe724f')

@app.route("/callback", methods=['POST'])
def callback():
    # 获取 X-Line-Signature 请求头的值
    signature = request.headers['X-Line-Signature']

    # 将请求体以文本形式获取
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # 处理 webhook 请求体
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 回应收到的文本信息
    reply_text = f"Echo: {event.message.text}"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

# 在主程序块中使用 Waitress 作为服务器
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)


