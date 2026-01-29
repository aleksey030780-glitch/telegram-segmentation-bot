from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN
import handlers
from states import Quiz

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.register_message_handler(handlers.start, commands=["start"])
dp.register_message_handler(handlers.industry_step, state=Quiz.industry)
dp.register_message_handler(handlers.scale_step, state=Quiz.scale)
dp.register_message_handler(handlers.pain_step, state=Quiz.pain)
dp.register_message_handler(handlers.warmth_step, state=Quiz.warmth)
dp.register_message_handler(handlers.name_step, state=Quiz.name)
dp.register_message_handler(
    handlers.phone_step,
    content_types=["contact"],
    state=Quiz.phone
)

if __name__ == "__main__":
    print("Bot started (polling)")
    executor.start_polling(dp, skip_updates=True)


