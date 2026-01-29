from aiogram import types
from aiogram.dispatcher import FSMContext
from states import Quiz
from keyboards import *
from database import save_lead
from config import ADMIN_CHAT_ID


async def start(message: types.Message):
    source = message.get_args() or "direct"

    await message.answer(
        "Привет! За 2 минуты разберём вашу ситуацию 👇",
        reply_markup=industry_kb()
    )

    await message.bot.send_message(
        ADMIN_CHAT_ID,
        f"👀 Новый вход\nИсточник: {source}\n@{message.from_user.username}"
    )

    await Quiz.industry.set()
    await message.state.update_data(source=source)


async def industry_step(message: types.Message, state: FSMContext):
    await state.update_data(industry=message.text)
    await message.answer("Сколько торговых точек?", reply_markup=scale_kb())
    await Quiz.scale.set()


async def scale_step(message: types.Message, state: FSMContext):
    await state.update_data(scale=message.text)
    await message.answer("Что сейчас больше всего напрягает?", reply_markup=pain_kb())
    await Quiz.pain.set()


async def pain_step(message: types.Message, state: FSMContext):
    await state.update_data(pain=message.text)
    await message.answer("Вы сейчас на каком этапе?", reply_markup=warmth_kb())
    await Quiz.warmth.set()


async def warmth_step(message: types.Message, state: FSMContext):
    await state.update_data(warmth=message.text)
    await message.answer("Как могу к вам обращаться?")
    await Quiz.name.set()


async def name_step(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Оставьте номер телефона", reply_markup=phone_kb())
    await Quiz.phone.set()


async def phone_step(message: types.Message, state: FSMContext):
    data = await state.get_data()

    lead = {
        "telegram_id": message.from_user.id,
        "username": message.from_user.username,
        "source": data["source"],
        "industry": data["industry"],
        "scale": data["scale"],
        "pain": data["pain"],
        "warmth": data["warmth"],
        "name": data["name"],
        "phone": message.contact.phone_number
    }

    save_lead(lead)

    text = (
        "📩 Заявка\n\n"
        f"👤 {lead['name']}\n"
        f"📞 {lead['phone']}\n"
        f"🏪 {lead['industry']}\n"
        f"📍 Точек: {lead['scale']}\n"
        f"🔥 {lead['pain']}\n"
        f"🌡 {lead['warmth']}\n"
        f"🔗 {lead['source']}"
    )

    await message.bot.send_message(ADMIN_CHAT_ID, text)
    await message.answer("Спасибо! Мы скоро свяжемся 🙌")
    await state.finish()
