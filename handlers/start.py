from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.keyboards import fikr_qoldirish

start_router : Router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message : Message):
    await message.answer(f"""Xush kelibsiz!

Assalomu alaykum, hurmatli foydalanuvchi! Ushbu bot sizdan qimmatli fikr-mulohazalarni olish uchun yaratilgan. Fikrlaringiz biz uchun juda muhim va ularni yaxshiroq xizmat ko'rsatish uchun ishlatamiz.

✅ Iltimos, bizga fikrlaringizni yuboring.

ℹ️ Eslatma: Ushbu bot orqali yuborilgan hech qanday shaxsiy ma'lumotlar saqlanmaydi va maxfiyligingizni himoya qilamiz.

Matn yuborish uchun "Fikr qoldirish" tugmasini bosing.
""" , reply_markup=fikr_qoldirish)
    