import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)

bot = Bot(token="7609769606:AAFjWNqDanDKthxO6MkqbXrD7O2WMuAfNMU")  # Вставьте сюда токен бота
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет, первокурсник! Я бот, который поможет тебе найти ответы на важные вопросы.\n\n"
        "Доступные команды:\n"
        "/help - помощь\n"
        "/schedule - расписание занятий\n"
        "/scholarship - информация о стипендии\n"
        "/library - информация о библиотеке\n"
        "/campus - информация о кампусе\n"
    )

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply(
        "Вот чем я могу помочь:\n\n"
        "/schedule - узнать расписание\n"
        "/scholarship - узнать про стипендию\n"
        "/library - узнать про библиотеку\n"
        "/campus - узнать про кампус"
    )

@dp.message_handler(commands=['schedule'])
async def send_schedule(message: types.Message):
    await message.reply(
        "https://rasp.omgtu.ru/ruz/main\n\n"
        "Для удобства рекомендую установить мобильное приложение вуза."
    )

@dp.message_handler(commands=['scholarship'])
async def send_scholarship_info(message: types.Message):
    await message.reply(
        "Стипендии бывают академические и социальные. Академическую получают студенты с высокими оценками.\n\n"
        "Социальная стипендия назначается для студентов, имеющих право на поддержку (например, по семейному положению). "
        "Подробности можно уточнить в стипендиальном отделе вуза."
    )

@dp.message_handler(commands=['library'])
async def send_library_info(message: types.Message):
    await message.reply(
        "Библиотека находится в главном корпусе на 1 этаже. Для записи в библиотеку возьмите читательский билет.\n\n"
    )

@dp.message_handler(commands=['campus'])
async def send_campus_info(message: types.Message):
    await message.reply(
        "Кампус вуза включает несколько корпусов и общежитий. С картой кампуса можно ознакомиться на сайте вуза.\n\n"
        "Общежития находятся в шаговой доступности от учебных корпусов."
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)