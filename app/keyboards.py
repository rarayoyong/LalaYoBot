import sqlite3
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Основные клавиатуры
menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Шпаргалка для новичка'), KeyboardButton(text='Список упражнений')],
    [KeyboardButton(text='Команды данного бота')]
], resize_keyboard=True)


# Функция для создания инлайн-клавиатуры с категориями упражнений
def create_categories_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Дыхательные упражнения', callback_data='category_breath'),
            InlineKeyboardButton(text='Разогрев голосовых связок', callback_data='category_vocal'),
        ],
        [
            InlineKeyboardButton(text='Артикуляция и дикция', callback_data='category_articulation'),
            InlineKeyboardButton(text='Интонация', callback_data='category_pitch'),
        ],
        [
            InlineKeyboardButton(text='Резонанс', callback_data='category_resonance'),
            InlineKeyboardButton(text='Вокальные регистры', callback_data='category_registers'),
        ],
        [
            InlineKeyboardButton(text='Ритм', callback_data='category_rhythm'),
            InlineKeyboardButton(text='Динамика', callback_data='category_dynamics'),
        ],
        [
            InlineKeyboardButton(text='Точность интонирования', callback_data='category_accuracy'),
        ],
    ])

    return keyboard

# Функция для создания клавиатуры с упражнениями из базы данных
async def create_exercises_keyboard(category):
    keyboard = []

    try:
        # Открываем соединение с базой данных
        conn = sqlite3.connect('v_exercises.db')
        cursor = conn.cursor()
        
        # Запрос упражнений по выбранной категории
        cursor.execute(f"SELECT id, exercise_name FROM {category}")
        exercises = cursor.fetchall()
        conn.close()

        if not exercises:
            # Если нет упражнений, добавляем кнопку с сообщением
            keyboard.append([InlineKeyboardButton(text='Нет доступных упражнений', callback_data='none')])
        else:
            # Добавляем кнопки с упражнениями
            for exercise_id, exercise_name in exercises:
                keyboard.append([InlineKeyboardButton(text=exercise_name, callback_data=f'exercise_{exercise_id}_{category}')])

        # Кнопка возврата к категориям
        keyboard.append([InlineKeyboardButton(text='Назад к категориям', callback_data='back_to_categories')])

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        keyboard = [[InlineKeyboardButton(text="Ошибка загрузки упражнений", callback_data='none')]]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Нововведение
# Функция для создания клавиатуры выбора недели
def create_week_selection_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Неделя 1", callback_data="week_1")],
        [InlineKeyboardButton(text="Неделя 2", callback_data="week_2")],
        [InlineKeyboardButton(text="Неделя 3", callback_data="week_3")],
        [InlineKeyboardButton(text="Неделя 4", callback_data="week_4")],
    ])
    return keyboard

# Функция для создания кнопки "Назад" к списку недель
def back_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_weeks")]
    ])
