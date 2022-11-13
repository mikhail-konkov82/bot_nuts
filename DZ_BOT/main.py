import asyncio

from aiogram.utils import executor

from bot import bot, dp
import handlers


async def on_startup(_):
    print('I see you!')
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

#
