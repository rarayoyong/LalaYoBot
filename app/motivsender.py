from apscheduler.schedulers.asyncio import AsyncIOScheduler
import sqlite3
import asyncio

# Хранение текущей позиции
current_index = 0

# Функция для получения всех цитат из базы данных
def get_all_quotes():
    conn = sqlite3.connect('motivational_quotes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT quote FROM quotes ORDER BY id')
    quotes = cursor.fetchall()
    conn.close()
    return [quote[0] for quote in quotes]  # Возвращаем список строк цитат

# Функция для получения следующей фразы
def get_next_quote(all_quotes):
    global current_index

    # Проверка на конец списка
    if current_index >= len(all_quotes):
        current_index = 0

    # Получение текущей фразы
    quote = all_quotes[current_index]
    current_index += 1

    return quote

# Функция для сохранения chat_id пользователя
def save_user(chat_id):
    try:
        conn = sqlite3.connect('motivational_quotes.db')
        cursor = conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO users (chat_id) VALUES (?)', (chat_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Ошибка при сохранении chat_id: {e}")

# Функция для рассылки фраз всем сохранённым пользователям
async def send_motivational_quote(bot):
    all_quotes = get_all_quotes()  # Получаем все цитаты
    quote = get_next_quote(all_quotes)

    try:
        conn = sqlite3.connect('motivational_quotes.db')
        cursor = conn.cursor()

        # Получение всех chat_id пользователей
        cursor.execute('SELECT chat_id FROM users')
        users = cursor.fetchall()
        conn.close()

        print(f"Количество пользователей для рассылки: {len(users)}")  # Лог количества пользователей

        # Отправка цитаты каждому пользователю
        for user in users:
            chat_id = user[0]
            try:
                print(f"Отправка цитаты: '{quote}' пользователю: {chat_id}")  # Лог отправки
                await bot.send_message(chat_id, quote)
            except Exception as e:
                print(f"Ошибка при отправке сообщения пользователю {chat_id}: {e}")

    except sqlite3.Error as e:
        print(f"Ошибка при получении пользователей: {e}")

# Настройка планировщика
async def send_motivation(bot):
    scheduler = AsyncIOScheduler()

    # Добавление задачи для регулярной рассылки каждые 2 минуты
    scheduler.add_job(send_motivational_quote, 'interval', minutes=2, args=[bot])
    
    # Запуск планировщика
    scheduler.start()

    # Бесконечный цикл, чтобы планировщик не завершался
    while True:
        await asyncio.sleep(1)
