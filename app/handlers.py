from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import types
from aiogram.fsm.context import FSMContext
from app.keyboards import create_categories_keyboard, create_exercises_keyboard, create_week_selection_keyboard, back_keyboard, menu
import app.keyboards as kb
import sqlite3

#это новое
import re
from aiogram.utils.markdown import hlink

from app.motivsender import save_user 

router = Router()


# Обработчик команды /start
@router.message(CommandStart())
async def cmd_start(message: types.Message):
    chat_id = message.chat.id  # Получаем chat_id пользователя
    save_user(chat_id)  # Сохраняем chat_id в базе данных

    photo_url = "https://disk.yandex.ru/i/Cy64rMGMHPYFrA.jpg"
    
    greeting_text = (
        f"🎶 <b>Привет, {message.from_user.first_name}!</b>\n\n"
        "Я <b>Lala Yo</b>, твой личный помощник в мире вокала! 🎤\n"
        "Вместе мы будем развивать твой голос, разбирать упражнения и совершенствовать технику.\n\n"
        "Готов начать? 😊"
    )

    await message.answer_photo(photo_url, caption=greeting_text, parse_mode="HTML")
    
    level_question = (
        "🌟 <b>Определи свой уровень:</b>\n\n"
        "🔹 <b>Новичок</b> – если только начинаешь и хочешь изучить основы.\n"
        "🔹 <b>Опытный</b> – если уже умеешь петь, но хочешь улучшить технику.\n\n"
        "👉 Напиши в чат свой уровень, и я подберу для тебя подходящие упражнения!"
    )

    await message.answer(level_question, parse_mode="HTML", reply_markup=kb.menu)


# 🎯 Обработчик команды /help
@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "🔹 <b>Список доступных команд:</b>\n\n"
        "📌 <b>/start</b> – Начать работу с ботом\n"
        "📌 <b>/help</b> – Получить справку по командам\n"
        "📌 <b>Шпаргалка для новичка</b> – План занятий для начинающих\n"
        "📌 <b>Список упражнений</b> – Все доступные упражнения\n"
        "📌 <b>Советы по вокалу</b> – Полезные рекомендации\n"
        "📌 <b>Информация о голосе</b> – Узнай свой уровень\n\n"
        "✨ Просто нажмите на команду или введите её в чат!"
    )
    await message.answer(help_text, parse_mode="HTML")

# 🎤 Обработчик "Советы по вокалу"
@router.message(lambda message: message.text == "Советы по вокалу")
async def handle_vocal_tips(message: types.Message):
    tips_text = (
        "🎶 <b>Полезные советы для вокалистов:</b>\n\n"
        "1️⃣ <b>Правильное дыхание</b> – Дышите животом, а не грудью. Диафрагмальное дыхание даёт контроль над голосом и улучшает звук.\n\n"
        "2️⃣ <b>Разогрев перед пением</b> – Выполняйте простые вокальные упражнения: гудение (ммм...), легкие распевки, губные трели. Это помогает связкам разогреться и избежать напряжения.\n\n"
        "3️⃣ <b>Гидратация</b> – Пейте тёплую воду или травяные чаи. Избегайте холодных напитков и кофеина перед пением – они сушат связки.\n\n"
        "4️⃣ <b>Записывайте себя</b> – Слушайте свои записи, отмечайте ошибки, работайте над интонацией и дикцией. Это поможет вам прогрессировать быстрее.\n\n"
        "5️⃣ <b>Эмоции в голосе</b> – Пойте с настроением! Голос должен передавать эмоции – радость, грусть, вдохновение. Представьте, что вы рассказываете историю!\n\n"
        "6️⃣ <b>Основа хорошего звука</b> – Не сжимайте горло! Расслабьте мышцы лица, шеи и плеч, пойте естественно.\n\n"
        "7️⃣ <b>Следите за осанкой</b> – Выпрямите спину, слегка опустите плечи. Хорошая осанка помогает лучше контролировать дыхание.\n\n"
        "8️⃣ <b>Пойте с удобным диапазоном</b> – Не пытайтесь сразу брать сложные высокие ноты. Постепенно расширяйте диапазон, развивая гибкость голоса.\n\n"
        "9️⃣ <b>Тренируйтесь регулярно</b> – Лучше заниматься 15–30 минут каждый день, чем 2 часа один раз в неделю.\n\n"
        "🔟 <b>Отдыхайте!</b> – Не перенапрягайте голосовые связки. Если чувствуете усталость или охриплость, дайте голосу восстановиться.\n\n"
        "🎤 Главное – наслаждайтесь процессом и получайте удовольствие от пения! Удачи! 😊"
    )
    await message.answer(tips_text, parse_mode="HTML")

# 🗣 Обработчик "Информация о голосе"
@router.message(lambda message: message.text == "Информация о голосе")
async def handle_voice_info(message: types.Message):
    voice_info_text = (
        "🧐 <b>Интересные факты о голосе:</b>\n\n"
        "🔹 <b>Голос – это не только связки!</b> 🗣️ Он создаётся за счёт работы голосовых связок, резонаторов (рот, нос, грудь) и дыхания.\n\n"
        "🔹 <b>Уникальный инструмент 🎵</b> – Голос каждого человека неповторим, как отпечаток пальца. Даже у близнецов есть различия в тембре!\n\n"
        "🔹 <b>Развитие диапазона</b> 🔥 – Если регулярно тренироваться, можно увеличить свой вокальный диапазон на несколько нот, а иногда и на целую октаву!\n\n"
        "🔹 <b>Голосовые связки – это мышцы 💪</b> – Они работают как мышцы, поэтому их можно тренировать, укреплять и развивать.\n\n"
        "🔹 <b>Высокие и низкие ноты</b> 🎶 – За них отвечают длина и натяжение связок. Чем короче и натянутее связки, тем выше звук, и наоборот.\n\n"
        "🔹 <b>Грудной и головной резонанс</b> 🏆 – Грудные звуки создаются за счёт вибрации в груди, а головные – в области головы и носовых пазух.\n\n"
        "🔹 <b>Умение говорить – не равно умению петь! 🎤</b> – Разговорный голос и певческий голос работают по-разному. Пение требует контроля дыхания, техники и резонанса.\n\n"
        "🔹 <b>Связки могут выдерживать до 1 000 000 вибраций в день! 😲</b> – Именно поэтому важно давать им отдых и правильно заботиться о голосе.\n\n"
        "🔹 <b>Вокал улучшает здоровье 🩺</b> – Пение помогает развивать лёгкие, улучшает осанку и даже снижает стресс!\n\n"
        "🎤 <b>Вывод:</b> Голос – это мощный инструмент, который можно развивать, как и любой другой музыкальный навык. Главное – практика и любовь к пению! ❤️"
    )
    await message.answer(voice_info_text, parse_mode="HTML")

# 🎯 Обработка ответа на уровень вокала
@router.message(lambda message: message.text.lower() in ["новичок", "опытный"])
async def handle_level(message: types.Message):
    user_input = message.text.lower()
    if "новичок" in user_input:
        await message.answer(
            "🎉 Отлично! Давайте начнём с азов. Вот план занятий для новичков:",
            parse_mode="HTML",
            reply_markup=kb.menu
        )
        await handle_cheat_sheet(message)
    elif "опытный" in user_input:
        await message.answer(
            "🚀 Прекрасно! Вам подойдут продвинутые упражнения:",
            parse_mode="HTML",
            reply_markup=kb.menu
        )
        await handle_exercises_list(message)

# 📜 Обработчик "Команды данного бота"
@router.message(lambda message: message.text == "Команды данного бота")
async def handle_commands(message: types.Message):
    commands_text = (
        "📜 <b>Список доступных команд:</b>\n\n"
        "🟢 <b>/start</b> – Начать работу с ботом\n"
        "🟢 <b>/help</b> – Получить справку\n"
        "🟢 <b>Шпаргалка для новичка</b> – Узнать о базовых упражнениях\n"
        "🟢 <b>Список упражнений</b> – Все доступные упражнения\n"
        "🟢 <b>Советы по вокалу</b> – Полезные рекомендации\n"
        "🟢 <b>Информация о голосе</b> – Интересные факты о голосе\n\n"
        "🎶 Просто выберите команду и наслаждайтесь обучением!"
    )
    await message.answer(commands_text, parse_mode="HTML")


# Обработчик для кнопки "Шпаргалка для новичка"
@router.message(lambda message: message.text == "Шпаргалка для новичка")
async def handle_cheat_sheet(message: types.Message):    

    explanation = (
        "📚 <b>План занятий на месяц</b>\n\n"
        "Этот план поможет вам постепенно развить голос, улучшить дыхание и дикцию.\n"
        "Каждая неделя включает полезные упражнения. Выбирайте неделю и следуйте рекомендациям!"
    )

    await message.answer(explanation, parse_mode="HTML")

    await message.answer(
        "Выберите неделю:", 
        parse_mode="HTML",
        reply_markup=create_week_selection_keyboard()
    )

# Обработчик выбора недели
@router.callback_query(lambda c: c.data.startswith("week_"))
async def process_week_callback(callback_query: CallbackQuery):

    week_data = {
        "week_1": (
            "📌 <b>Неделя 1: Дыхание и основы звукоизвлечения</b>\n\n"
            "1️⃣ <b>Воздушный шар</b> 🎈 – представьте, что у вас в животе воздушный шар. Вдохните через нос, наполняя живот, а затем медленно выдохните через рот.\n\n"
            "2️⃣ <b>Свеча</b> 🕯 – вдохните и выдыхайте так, чтобы пламя свечи колебалось, но не гасло. Это научит вас контролировать дыхание.\n\n"
            "3️⃣ <b>Шипящее дыхание</b> 🐍 – сделайте длинный выдох со звуком 'сссс', как змея. Попробуйте продержаться как можно дольше.\n\n"
            "4️⃣ <b>Гудение</b> 🎵 – закройте рот и тяните 'ммм', ощущая вибрацию в губах. Это разогреет голос.\n\n"
            "5️⃣ <b>Ленивые звуки</b> 🗣 – тяните 'А-а-а', 'О-о-о', 'У-у-у', расслабляя горло.\n\n"
            "6️⃣ <b>Дыхание 4-4-4</b> 🌬 – вдохните на 4 счёта, задержите дыхание на 4 счёта, медленно выдохните на 4 счёта.\n\n"
            "7️⃣ <b>Шёпот</b> 🤫 – прошепчите длинную фразу, не напрягая горло.\n\n"
            "8️⃣ <b>Качели</b> 🎢 – пойте 'у-а' или 'о-и', меняя высоту звука плавно.\n\n"
            "9️⃣ <b>Мягкое произношение</b> ☁ – говорите гласные звуки плавно и без резких атак.\n\n"
            "🔟 <b>Расслабление</b> 🛀 – перед занятием расслабьте лицо, шею и плечи, покрутите головой и разомните челюсть.\n"
        ),

        "week_2": (
            "📌 <b>Неделя 2: Развитие голоса</b>\n\n"
            "1️⃣ <b>Бабочка</b> 🦋 – губы в трубочку, произнесите 'ббррр', чтобы они завибрировали.\n\n"
            "2️⃣ <b>Жужжание</b> 🐝 – скажите 'ззз' или 'ввв', чувствуя вибрацию в лице.\n\n"
            "3️⃣ <b>Тянем резину</b> 🎶 – пойте 'Ма-Мо-Му-Ми-Мэ', плавно растягивая звуки.\n\n"
            "4️⃣ <b>Напевание</b> 🎼 – напевайте простую мелодию на 'ля-ля-ля'.\n\n"
            "5️⃣ <b>Пение без слов</b> 🎤 – пойте мелодии только на гласные 'А-О-У-И-Э'.\n\n"
            "6️⃣ <b>Кашель с голосом</b> 🤧 – легко покашляйте с голосом, ощущая вибрацию в груди.\n\n"
            "7️⃣ <b>Ворчание</b> 🦁 – мягко ворчите, чувствуя вибрацию в груди.\n\n"
            "8️⃣ <b>Скользящие звуки</b> 🏄‍♂️ – тяните 'у-у-у' или 'и-и-и', плавно меняя высоту звука.\n\n"
            "9️⃣ <b>Говорим на разной высоте</b> 📣 – произносите фразы сначала низким, потом высоким голосом.\n\n"
            "🔟 <b>Звуковой массаж</b> 💆 – пойте 'м-м-м', прикладывая пальцы к щекам, чтобы почувствовать вибрацию.\n"
        ),

        "week_3": (
            "📌 <b>Неделя 3: Артикуляция и дикция</b>\n\n"
            "1️⃣ <b>Скороговорки</b> 🏃‍♂️ – проговаривайте медленно, затем ускоряйтесь.\n\n"
            "2️⃣ <b>Карандаш во рту</b> ✏ – зажмите карандаш зубами и говорите фразы.\n\n"
            "3️⃣ <b>Чередование гласных</b> 🔄 – произносите 'А-О-У-И-Э' в разном темпе.\n\n"
            "4️⃣ <b>Разминка губ</b> 👄 – вытягивайте губы в трубочку, затем улыбайтесь.\n\n"
            "5️⃣ <b>Разминка языка</b> 👅 – делайте круги языком внутри рта.\n\n"
            "6️⃣ <b>Произношение шёпотом</b> 🤫 – чётко проговаривайте текст шёпотом.\n\n"
            "7️⃣ <b>Разнообразные темпы</b> 🏎 – сначала говорите медленно, затем быстро.\n\n"
            "8️⃣ <b>Имитация речи</b> 🎙 – повторяйте за дикторами или актёрами.\n\n"
            "9️⃣ <b>Чёткие согласные</b> 🔊 – утрированно произносите звуки 'Б', 'Д', 'К'.\n\n"
            "🔟 <b>Пение с дикцией</b> 🎤 – пойте песню, делая акцент на чёткости слов.\n"
        ),

        "week_4": (
            "📌 <b>Неделя 4: Интонация и ритм</b>\n\n"
            "1️⃣ <b>Лестница</b> 🎶 – пойте ноты, двигаясь вверх и вниз.\n\n"
            "2️⃣ <b>Громко-тихо</b> 🔊 – пойте звук, сначала усиливая, потом ослабляя громкость.\n\n"
            "3️⃣ <b>Ритм хлопками</b> 👏 – хлопайте ритм и повторяйте его голосом.\n\n"
            "4️⃣ <b>Имитация мелодий</b> 🎵 – напевайте мелодии без слов.\n\n"
            "5️⃣ <b>Пение с улыбкой</b> 😃 – пойте, улыбаясь, меняя тембр.\n\n"
            "6️⃣ <b>Голосовая волна</b> 🌊 – пойте звук, делая его то громче, то тише.\n\n"
            "7️⃣ <b>Песня в разном настроении</b> 🎭 – попробуйте спеть песню весело, грустно, удивлённо.\n\n"
            "8️⃣ <b>Шёпот + голос</b> 🗣 – начните фразу шёпотом, затем плавно добавьте голос.\n\n"
            "9️⃣ <b>Разные ритмы</b> 🥁 – пойте одну и ту же мелодию в медленном и быстром темпе.\n\n"
            "🔟 <b>Динамика в песне</b> 🎼 – выберите строчку песни и попробуйте спеть её сначала очень тихо, затем громко.\n"
        ),
    }


    week_key = callback_query.data
    text = week_data.get(week_key, "Ошибка: Неделя не найдена")


    await callback_query.message.edit_text(text, parse_mode="HTML", reply_markup=back_keyboard())

# Обработчик возврата к списку недель
@router.callback_query(lambda c: c.data == "back_to_weeks")
async def back_to_weeks(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Выберите неделю:", 
        parse_mode="HTML",
        reply_markup=create_week_selection_keyboard()
    )


# Обработчик для кнопки "Список упражнений"
@router.message(lambda message: message.text == "Список упражнений")
async def handle_exercises_list(message: types.Message):
    await message.answer("Выберите категорию упражнений:", reply_markup=create_categories_keyboard())

# Обработчик выбора категории
@router.callback_query(lambda c: c.data.startswith('category_'))
async def handle_category_selection(callback_query: CallbackQuery):
    # Соответствие категорий с названиями таблиц в базе данных
    category_map = {
        'category_breath': 'breath',
        'category_vocal': 'vocal',
        'category_articulation': 'articulation',
        'category_pitch': 'pitch',
        'category_resonance': 'resonance',
        'category_registers': 'registers',
        'category_rhythm': 'rhythm',
        'category_dynamics': 'dynamics',
        'category_accuracy': 'accuracy'
    }

    # Русские названия категорий
    category_names = {
        'breath': 'Дыхательные упражнения',
        'vocal': 'Разогрев голосовых связок',
        'articulation': 'Артикуляция и дикция',
        'pitch': 'Интонация',
        'resonance': 'Резонанс',
        'registers': 'Вокальные регистры',
        'rhythm': 'Ритм',
        'dynamics': 'Динамика',
        'accuracy': 'Точность интонирования'
    }

    category = category_map.get(callback_query.data)
    
    if category:
        try:
            # Лог для отладки
            print(f"Запрос к категории: {category}")

            # Создаем клавиатуру упражнений для выбранной категории
            keyboard = await create_exercises_keyboard(category)

            # Получаем русское название категории, если оно есть
            category_display_name = category_names.get(category, category)

            await callback_query.message.edit_text(
                #f"Упражнения в категории: {category.replace('_', ' ').title()}",
                f"Упражнения в категории: {category_display_name}",
                reply_markup=keyboard
            )
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")
            await callback_query.message.answer("Произошла ошибка при работе с базой данных.")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")
            await callback_query.message.answer("Произошла ошибка при обработке вашего запроса.")
    else:
        await callback_query.message.answer("Неверная категория.")

# Обработчик для возврата в категории
@router.callback_query(lambda c: c.data == 'back_to_categories')
async def back_to_categories(callback_query: CallbackQuery):
    try:
        # Возврат к категориям
        keyboard = create_categories_keyboard()
        await callback_query.message.edit_text("Выберите категорию упражнений:", reply_markup=keyboard)
    except Exception as e:
        print(f"Ошибка: {e}")
        await callback_query.message.answer("Произошла ошибка при возвращении к категориям.")


CHANNEL_ID = -1002611999941  # ID закрытого канала

TECH_CHANNEL_ID = -1002528783467  # ID скрытого канала

@router.callback_query(lambda c: c.data.startswith('exercise_'))
async def handle_exercise_selection(callback_query: CallbackQuery):
    bot = callback_query.bot
    exercise_id = callback_query.data.split('_')[1]
    category = callback_query.data.split('_')[2]

    try:
        conn = sqlite3.connect('v_exercises.db')
        cursor = conn.cursor()

        # Получаем ссылку на пост с видео
        cursor.execute(f"SELECT exercise_link FROM {category} WHERE id=?", (exercise_id,))
        exercise = cursor.fetchone()
        conn.close()

        if exercise:
            link = exercise[0]

            # Извлекаем message_id из ссылки
            match = re.search(r'/(\d+)$', link)
            if match:
                message_id = int(match.group(1))

                # Пересылаем сообщение в скрытый канал
                forwarded_message = await bot.forward_message(
                    chat_id=TECH_CHANNEL_ID, 
                    from_chat_id=CHANNEL_ID, 
                    message_id=message_id
                )

                # Получаем file_id видео
                file_id = forwarded_message.video.file_id  

                # Удаляем сообщение из скрытого канала, чтобы не засорять его
                await bot.delete_message(chat_id=TECH_CHANNEL_ID, message_id=forwarded_message.message_id)

                # Отправляем видео пользователю напрямую
                await bot.send_video(chat_id=callback_query.message.chat.id, video=file_id)

            else:
                await callback_query.message.answer(f"Вот ваше упражнение: {hlink('Ссылка на упражнение', link)}", parse_mode="HTML")

        else:
            await callback_query.message.answer("Упражнение не найдено.")

    except sqlite3.Error as e:
        await callback_query.message.answer("Произошла ошибка при работе с базой данных.")
        print(f"Ошибка базы данных: {e}")
    except Exception as e:
        await callback_query.message.answer("Произошла ошибка.")
        print(f"Неизвестная ошибка: {e}")

