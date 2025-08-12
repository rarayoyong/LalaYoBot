import sqlite3

# Подключение к базе данных (если файла базы данных нет, он будет создан)
conn = sqlite3.connect('v_exercises.db')
cursor = conn.cursor()

# Функция для удаления таблицы, если она существует
def drop_table_if_exists(table_name):
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    print(f"Таблица {table_name} удалена.")

# Функция для создания таблицы
def create_table(table_name):
    cursor.execute(f'''
        CREATE TABLE {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise_name TEXT NOT NULL,
            exercise_link TEXT NOT NULL
        )
    ''')
    print(f"Таблица {table_name} создана.")

# Список категорий таблиц
categories = [
    'breath', 
    'vocal', 
    'articulation', 
    'pitch', 
    'resonance', 
    'registers', 
    'rhythm', 
    'dynamics', 
    'accuracy'
]

# Удаление старых таблиц (если они существуют) и создание новых
for category in categories:
    drop_table_if_exists(category)  # Удаляем старую таблицу
    create_table(category)  # Создаём новую таблицу

# Функция для вставки данных в таблицы
def insert_data(table_name, exercise_name, exercise_link):
    cursor.execute(f'''
        INSERT INTO {table_name} (exercise_name, exercise_link)
        VALUES (?, ?)
    ''', (exercise_name, exercise_link))
    print(f"Добавлено упражнение '{exercise_name}' в таблицу {table_name}.")

# Вставка данных в таблицы

# 1. Breath Control
insert_data('breath', 'Вокальное упражнение на дыхание 1', 'https://t.me/c/2611999941/4')
insert_data('breath', 'Вокальное упражнение на дыхание 2', 'https://t.me/c/2611999941/6')
insert_data('breath', 'Вокальное упражнение на дыхание 3', 'https://t.me/c/2611999941/8')
insert_data('breath', 'Вокальное упражнение на дыхание 4', 'https://t.me/c/2611999941/10')
insert_data('breath', 'Вокальное упражнение на дыхание 5', 'https://t.me/c/2611999941/12')
insert_data('breath', 'Вокальное упражнение на дыхание 6', 'https://t.me/c/2611999941/14')
insert_data('breath', 'Вокальное упражнение на дыхание 7', 'https://t.me/c/2611999941/16')

# 2. Vocal Warm-ups
insert_data('vocal', 'Вокальное упражнение на глиссандо', 'https://t.me/c/2611999941/19')
insert_data('vocal', 'Вокальное упражнение на хроматическую гамму', 'https://t.me/c/2611999941/21')
insert_data('vocal', 'Вокальное упражнение на гармоническую мажорную гамму', 'https://t.me/c/2611999941/23')
insert_data('vocal', 'Ежедневные упражнения на сложные гаммы', 'https://t.me/c/2611999941/25')

# 3. Articulation and Diction
insert_data('articulation', 'Вокальное упражнение на артикуляцию', 'https://t.me/c/2611999941/28')
insert_data('articulation', 'Вокальное упражнение на согласные звуки', 'https://t.me/c/2611999941/30')
insert_data('articulation', "Тренировка дикции на фразу \"Mommy made me mash my m&m's\"", 'https://t.me/c/2611999941/32')
insert_data('articulation', 'Вокальное упражнение на гласные звуки', 'https://t.me/c/2611999941/34')
insert_data('articulation', 'Тренировка дикции на фразу "YOGI MOGU"', 'https://t.me/c/2611999941/36')
insert_data('articulation', 'Тренировка дикции на фразу "Peter picked a peck of pickled peppers"', 'https://t.me/c/2611999941/38')
insert_data('articulation', 'Тренировка дикции на фразу "PI BAE PA BO PU"', 'https://t.me/c/2611999941/40')
insert_data('articulation', 'Тренировка дикции на фразу "LAH LEH"', 'https://t.me/c/2611999941/42')
insert_data('articulation', 'Ежедневные вокальные упражнения на артикуляцию', 'https://t.me/c/2611999941/44')

# 4. Pitch and Intonation Training
insert_data('pitch', 'Стаккато и легато на звук "У"', 'https://t.me/c/2611999941/47')
insert_data('pitch', 'Упражнение на звук "Хи Хи Ха Ха" для мужского голоса', 'https://t.me/c/2611999941/49')
insert_data('pitch', 'Упражнение на звук "Хи Хи Ха Ха"', 'https://t.me/c/2611999941/51')
insert_data('pitch', 'Стаккато и легато на звук "У"', 'https://t.me/c/2611999941/53')
insert_data('pitch', 'Стаккато и легато для мужского голоса', 'https://t.me/c/2611999941/55')
insert_data('pitch', 'Упражнение на фразу "Laughing is Contagious"', 'https://t.me/c/2611999941/57')
insert_data('pitch', 'Ежедневные упражнения на мелизмы', 'https://t.me/c/2611999941/59')
insert_data('pitch', 'Ежедневные упражнения на гибкость голоса', 'https://t.me/c/2611999941/61')
insert_data('pitch', 'Упражнение на точность попадания в ноты и гибкость голоса', 'https://t.me/c/2611999941/63')

# 5. Resonance and Tone Development
insert_data('resonance', 'Упражнение на плавные переходы', 'https://t.me/c/2611999941/66')
insert_data('resonance', 'Вокальное упражнение на резонанс', 'https://t.me/c/2611999941/68')
insert_data('resonance', 'Вокальное упражнение на звук "May"', 'https://t.me/c/2611999941/70')
insert_data('resonance', 'Вокальное упражнение на звук "Hum"', 'https://t.me/c/2611999941/72')
insert_data('resonance', 'Вокальное упражнение на звук "Nay"', 'https://t.me/c/2611999941/74')
insert_data('resonance', 'Вокальное упражнение на звук "NG"', 'https://t.me/c/2611999941/76')
insert_data('resonance', 'Вокальное упражнение на звук "NJA"', 'https://t.me/c/2611999941/78')

# 6. Vocal Registers
# Vocal Registers CHEST
insert_data('registers', 'Вокальное упражнение на грудной регистр на длинный звук "А"', 'https://t.me/c/2611999941/82')
insert_data('registers', 'Вокальное упражнение на грудной регистр', 'https://t.me/c/2611999941/84')
insert_data('registers', 'Вокальное упражнение на грудной регистр на короткий звук "А"', 'https://t.me/c/2611999941/86')
insert_data('registers', 'Вокальное упражнение на грудной регистр на звук "NUAH"', 'https://t.me/c/2611999941/88')
insert_data('registers', 'Вокальное упражнение на грудной регистр на звук "А"', 'https://t.me/c/2611999941/90')
insert_data('registers', 'Вокальное упражнение на грудной регистр, арпеджио на звук "А"', 'https://t.me/c/2611999941/92')
insert_data('registers', 'Вокальное упражнение на грудной регистр на звук "А"', 'https://t.me/c/2611999941/94')
insert_data('registers', 'Вокальное упражнение на грудной регистр на звук "А"', 'https://t.me/c/2611999941/96')
insert_data('registers', 'Ежедневные упражнения на грудной регистр', 'https://t.me/c/2611999941/98')

# Vocal Registers HEAD
insert_data('registers', 'Вокальное упражнение на головной регистр на звук "BUB"', 'https://t.me/c/2611999941/101')
insert_data('registers', 'Вокальное упражнение на головной регистр', 'https://t.me/c/2611999941/103')
insert_data('registers', 'Вокальное упражнение на головной регистр на звук "E"', 'https://t.me/c/2611999941/105')
insert_data('registers', 'Вокальное упражнение на головной регистр на звук "UH"', 'https://t.me/c/2611999941/107')
insert_data('registers', 'Вокальное упражнение на головной регистр на звук "NO"', 'https://t.me/c/2611999941/109')
insert_data('registers', 'Вокальное упражнение на головной регистр на звук "MUH"', 'https://t.me/c/2611999941/111')
insert_data('registers', 'Ежедневные упражнения на головной регистр', 'https://t.me/c/2611999941/113')

# Vocal Registers MIXED
insert_data('registers', 'Вокальное упражнение на смешанный регистр', 'https://t.me/c/2611999941/116')
insert_data('registers', 'Вокальное упражнение на смешанный регистр', 'https://t.me/c/2611999941/118')
insert_data('registers', 'Вокальное упражнение на смешанный регистр на звук "BUB"', 'https://t.me/c/2611999941/120')
insert_data('registers', 'Вокальное упражнение на смешанный регистр, плавные переходы на звук "А"', 'https://t.me/c/2611999941/122')
insert_data('registers', 'Вокальное упражнение на смешанный регистр, плавные переходы', 'https://t.me/c/2611999941/124')
insert_data('registers', 'Вокальное упражнение на смешанный регистр, мелизмы', 'https://t.me/c/2611999941/126')
insert_data('registers', 'Вокальное упражнение на смешанный регистр на звук "YEAH"', 'https://t.me/c/2611999941/128')
insert_data('registers', 'Вокальное упражнение на смешанный регистр, арпеджио на звук "А"', 'https://t.me/c/2611999941/130')
insert_data('registers', 'Ежедневные упражнения на смешанный регистр', 'https://t.me/c/2611999941/132')

# Vocal Registers FALSETTO
insert_data('registers', 'Вокальное упражнение на фальцет', 'https://t.me/c/2611999941/135')
insert_data('registers', 'Вокальное упражнение на фальцет', 'https://t.me/c/2611999941/137')
insert_data('registers', 'Вокальное упражнение на фальцет на звук "HI"', 'https://t.me/c/2611999941/139')
insert_data('registers', 'Вокальное упражнение на фальцет на звук "А"', 'https://t.me/c/2611999941/141')
insert_data('registers', 'Вокальное упражнение на фальцет на звуки "О" и "А"', 'https://t.me/c/2611999941/143')
insert_data('registers', 'Вокальное упражнение на фальцет, губная трель', 'https://t.me/c/2611999941/145')
insert_data('registers', 'Вокальное упражнение на фальцет', 'https://t.me/c/2611999941/147')
insert_data('registers', 'Вокальное упражнение на фальцет на звук "HOO"', 'https://t.me/c/2611999941/149')
insert_data('registers', 'Ежедневные упражнения на фальцет', 'https://t.me/c/2611999941/151')

# 7. Rhythm and Phrasing
insert_data('rhythm', 'Упражнение на ритм', 'https://t.me/c/2611999941/154')
insert_data('rhythm', 'Упражнение на ритм для новичков', 'https://t.me/c/2611999941/156')

# 8. Dynamics
insert_data('dynamics', 'Вокальное упражнение на динамику', 'https://t.me/c/2611999941/159')
insert_data('dynamics', 'Вокальное упражнение на динамику', 'https://t.me/c/2611999941/161')
insert_data('dynamics', 'Вокальное упражнение на динамику на звуки "HA", "HE", "EE", "HE", "HA"', 'https://t.me/c/2611999941/163')
insert_data('dynamics', 'Вокальное упражнение на динамику на звуки "YO", "WOW", "WOW", "WOW", "WOW"', 'https://t.me/c/2611999941/165')
insert_data('dynamics', 'Вокальное упражнение на динамику на звуки "HA" и "HE"', 'https://t.me/c/2611999941/167')
insert_data('dynamics', 'Вокальное упражнение на динамику, смех', 'https://t.me/c/2611999941/169')
insert_data('dynamics', 'Вокальное упражнение на динамику на звук "BAH"', 'https://t.me/c/2611999941/171')

# 9. Pitch Accuracy
insert_data('accuracy', 'Вокальное упражнение на точность интонирования 1', 'https://t.me/c/2611999941/174')
insert_data('accuracy', 'Вокальное упражнение на точность интонирования 2', 'hhttps://t.me/c/2611999941/176')
insert_data('accuracy', 'Вокальное упражнение на точность интонирования 3', 'https://t.me/c/2611999941/178')
insert_data('accuracy', 'Упражнение на точность интонирования и гибкость голоса', 'https://t.me/c/2611999941/180')
insert_data('accuracy', 'Вокальное упражнение на точность интонирования 1A', 'https://t.me/c/2611999941/182')
insert_data('accuracy', 'Вокальное упражнение на точность интонирования 1B', 'https://t.me/c/2611999941/184')
insert_data('accuracy', 'Вокальное упражнение на точность интонирования 1C', 'https://t.me/c/2611999941/186')

# Подтверждаем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных успешно создана и заполнена!")


