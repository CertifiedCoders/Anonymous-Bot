# Anonymous Sender Bot (PTB Version)

A Telegram bot that anonymously resends messages and media with inline reply options, built using `python-telegram-bot`.

## 🌟 Features

- Resend any text/media anonymously
- Handle captioned messages with Yes/No buttons
- Sticker + Welcome message on `/start`
- Inline keyboard for support, source code, and owner
- Built for both **Heroku** and **VPS**

---

## 🚀 Deploy

### ⚡ Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/CertifiedCoders/Anonymous-Bot)

1. Click the button above.
2. Add `BOT_TOKEN` from [@BotFather](https://t.me/BotFather)
3. Deploy and you’re live.

---

### 🖥 Deploy on VPS

1. Clone the repo:
    ```bash
    git clone https://github.com/CertifiedCoders/Anonymous-Bot
    cd anon-sender-bot
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set your environment variable:
    ```bash
    export BOT_TOKEN=your_token_here
    ```

4. Run the bot:
    ```bash
    python bot.py
    ```

---

## 📦 Required Files

- `anonymous.py` → main bot script
- `Procfile` → for Heroku
- `requirements.txt` → Python dependencies
- `app.json` → Heroku metadata

---

## 👤 Developer

- **[CertifiedCoder](https://t.me/CertifiedCoder)**
- Support Group: [@CertifiedCoders](https://t.me/CertifiedCoders)
- Updates Channel: [@CertifiedNetwork](https://t.me/CertifiedNetwork)
