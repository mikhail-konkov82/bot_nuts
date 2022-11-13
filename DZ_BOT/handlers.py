from bot import dp, bot
from aiogram import types
from keyb import kb_nuts
import random

nuts = 121

def win(nuts):
    if nuts <= 0:
        return True
    else:
        return False

def comp_take():
    return random.randint(1, 29)

# Хэндлер на команду /start
@dp.message_handler(commands=["start","help"])
async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, здравствуй дорогой!\n'
                           "Как ты бро?\nРаскинем орешки? Жмякай не ссы ;-) /game\n"
                           "Выход /finish")

@dp.message_handler(commands=["new_game"])
async def newgame(message:types.Message):
    global nuts
    nuts = 121
    await message.answer(
        'Поиграем. Правила:\n Ходим по очереди, за один ход снять можно от 1 до 28 орешков. Стартовое количество 121 орех.\n '
        'Кто оставит после своего хода пустой стол, тот и победил. Ваш ход', reply_markup=kb_nuts)


@dp.message_handler(commands=["game"])
async def cmd_game_start(message: types.Message):
    await message.answer('Поиграем. Правила:\n Ходим по очереди, за один ход снять можно от 1 до 28 орешков. Стартовое количество 121 орех.\n '
                         'Кто оставит после своего хода пустой стол, тот и победил. Ваш ход', reply_markup=kb_nuts)

@dp.callback_query_handler()
async def process_callback(callback: types.CallbackQuery):
    global nuts
    data = callback.data
    if win(nuts):
        await callback.answer('Я победил\nЗахочешь заново набери /new_game,\nВыход /finish')
        return 1
    await callback.answer(f'вы забрали {data} орешков')
    nuts = nuts - int(data)
    if nuts <= 0 :
        await callback.message.answer(f'ты победил \nЗахочешь заново набери /new_game,\nВыход /finish')
        return 1
    else:
        await callback.message.answer(f'осталось {nuts} орешков')
    nuts = nuts - comp_take()
    if win(nuts):
        await callback.message.answer('я победил !!! \nЗахочешь заново набери /new_game,\nВыход /finish')
    else:
        await callback.message.answer(f'я забрал немного, осталось {nuts} орешков')

@dp.message_handler(commands=["finish"])
async def finish(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'до свидания!')