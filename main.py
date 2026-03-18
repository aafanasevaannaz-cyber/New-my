import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Я — Bot Factory 🤖\n\n"
        "Напиши, какого бота ты хочешь создать.\n"
        "Например: 'бот записи' или 'FAQ бот'"
    )


@dp.message()
async def handle(message: Message):
    text = message.text.lower()

    if "faq" in text:
        bot_type = "FAQ-бот"
    elif "запись" in text:
        bot_type = "бот записи"
    elif "ai" in text or "gpt" in text:
        bot_type = "AI-бот"
    else:
        bot_type = "универсальный бот"

    await message.answer(
        f"Поняла задачу: {bot_type}\n\n"
        "Дальше я соберу архитектуру (пока заглушка)"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
