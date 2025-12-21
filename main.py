import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "8487174877:AAH3stK1mYCplszEQkuQhLf3vlv-dT9MIbY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("📸 Rasm yubor — men senga link beraman")

@dp.message(lambda message: message.photo)
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)

    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file.file_path}"

    await msg.answer(
        "✅ Rasm linki tayyor:\n\n"
        f"{file_url}\n\n"
        "📌 Shu linkni mahsulot uchun ishlatishing mumkin"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
