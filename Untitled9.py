#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install line-bot-sdk


# In[ ]:


from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# Replace 'YOUR_CHANNEL_ACCESS_TOKEN' and 'YOUR_CHANNEL_SECRET' with your actual values
line_bot_api = LineBotApi('FgRwDsmCC055uMWW/YTiv/X/+vP+WzYMz/X6nl9wde6iaB/Q/C1chDgrGCDxHJVnK5mcR8wJmKuYCT5ck5OGRbw1e6BW9C9JtQaQIQefuomJ4vpmmpmmpMr; gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d59461ed36fad764c35e258a67fe724f')

@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Echo: " + event.message.text)
    )

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:




