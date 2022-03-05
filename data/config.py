# from environs import Env

# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()

# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

GROUP_CHAT_ID = -1001704364861

import os 
BOT_TOKEN = str(os.environs.get("BOT_TOKEN"))
ADMINS = list(os.environs.get("ADMINS"))
IP = str(os.environs.get("ip"))