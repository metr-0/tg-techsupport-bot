# tg-techsupport-bot

Бот принимает пересылает сообщения пользователей в чат техподдержки.
Если в этом чате ответят реплаем на обращение пользователя, бот перешлёт ему ответ.

### Создание venv и установка aiogram:

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Настройка:

    mv config/config-example.json config/config.json

Добавьте токен бота и ID чата техподдержки в `config/config.json`

На своё усмотрение отредактируйте ответы бота в `config/templates.json`

### Запуск:

    python run.py
