from linebot import LineBotApi
from linebot.models import TextSendMessage
import schedule
import time
import os

# 從環境變數讀取設定
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def send_reminder_friday_easywallet():
    message = TextSendMessage(text="悠遊付可以繳費了！")
    line_bot_api.push_message(USER_ID, message)
    print("已發送提醒訊息")

# 每週五 00:00 執行
schedule.every().friday.at("00:00").do(send_reminder_friday_easywallet)

print("LINE Bot 提醒服務啟動中...")
while True:
    schedule.run_pending()
    time.sleep(1)
