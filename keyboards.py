from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def industry_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Продукты", "Одежда / обувь")
    kb.add("Запчасти", "Косметика", "Другое")
    return kb

def scale_kb():
    return ReplyKeyboardMarkup(resize_keyboard=True).add("1", "2–5", "5+")

def pain_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Касса не сходится", "Хаос в остатках")
    kb.add("Воровство", "Много ручного учёта", "Нет цифр по прибыли")
    return kb

def warmth_kb():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        "Просто изучаю", "Ищу решение", "Готов внедрять"
    )

def phone_kb():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("📞 Отправить номер", request_contact=True)
    )
