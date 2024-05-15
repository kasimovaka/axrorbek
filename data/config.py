from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "7105572363:AAHVosGayVNu4ltdz1ojbPFgVtEfv-Px_DI"  # Bot toekn
ADMINS = {"5724358922"}  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
