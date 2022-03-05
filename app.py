
from aiogram import executor
# from pprint import pprint as print

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)
    # Ma'lumotlar bazasini yaratamiz:
    try:
        db.create_table_users()
    except Exception as err:
        pass

    # Bot ishga tushgani haqida adminga xabar berish
    try:
        await on_startup_notify(dispatcher)
        
    except Exception as e:
        pass


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
