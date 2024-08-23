from aiogram import Router , F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.states import feedback_state
from loader import bot

feedback_router : Router = Router()

malumotlar = dict()

@feedback_router.message(F.text == "Fikr qoldirish")
async def Fikrqoldirish_handler(message : Message , state: FSMContext):
    await state.set_state(feedback_state.teacher_p)
    await message.answer(text='''Sizning o'qituvchingiz haqida fikringiz qanday?

Hurmatli foydalanuvchi, sizning fikringiz biz uchun juda muhim! Iltimos, o'qituvchingiz haqida ijobiy fikrlaringizni biz bilan baham ko'ring. O'qituvchingizning sizga qanday yordam bergani yoki qanday yaxshi xususiyatlari borligini yozib yuboring.

📜 Biz sizning fikrlaringizni qadrlaymiz va ularni o'qituvchilarimizni qo'llab-quvvatlash uchun ishlatamiz.
''')

@feedback_router.message(feedback_state.teacher_p)
async def teacher_p_handler(message: Message , state: FSMContext):
    malumotlar['teacher_p'] = message.text
    await state.set_state(feedback_state.teacher_n)
    await message.answer(text="""Sizning o'qituvchingiz haqida tanqidingiz bormi?

Hurmatli foydalanuvchi, biz barcha fikr-mulohazalaringizni eshitishni xohlaymiz. Iltimos, o'qituvchingiz haqida sizni qoniqtirmagan jihatlarni biz bilan baham ko'ring. O'qituvchining qaysi xatti-harakatlari yoki o'qitish usuli sizga yoqmaganini yozib yuboring.

⚠️ Sizning salbiy fikrlaringiz biz uchun juda muhim va o'qituvchilarimizni yaxshilashda yordam beradi.
""")

@feedback_router.message(feedback_state.teacher_n)
async def teacher_n_handler(message: Message , state: FSMContext):
    malumotlar['teacher_n'] = message.text
    await state.set_state(feedback_state.teacher_score)
    await message.answer(text="""O'qituvchingizga baho bering va uninig ismini kiriting

Hurmatli foydalanuvchi, iltimos, o'qituvchingizga 0 dan 10 gacha baho bering. Sizning bahoingiz o'qituvchining darslarni qanday o'tayotgani va umumiy ish faoliyatini baholashga yordam beradi.

🔢 0 - umuman qoniqarli emas
🔢 10 - juda a'lo darajada

Iltimos, tanlovingizni biz bilan baham ko'ring.


""")

@feedback_router.message(feedback_state.teacher_score)
async def teacher_score_handler(message: Message , state:FSMContext):
    malumotlar['teacher_score'] = message.text
    await state.set_state(feedback_state.valiteach)
    await message.answer(text="""O'quv markazimizga takliflaringiz bormi?

Hurmatli foydalanuvchi, biz o'quv markazimizni yanada yaxshilash uchun sizning takliflaringizni eshitishni istaymiz. Iltimos, darslarimiz, o'qituvchilarimiz yoki umumiy muhitimizni yaxshilash bo'yicha har qanday takliflaringizni biz bilan baham ko'ring.

💡 Sizning takliflaringiz biz uchun juda muhim va o'quv markazimizni yanada samarali qilishga yordam beradi.
""")

@feedback_router.message(feedback_state.valiteach)
async def valiteach_handler(message: Message , state: FSMContext):
    malumotlar['valiteach'] = message.text
    await state.clear()
    await bot.send_message(chat_id='@valiteach_feedback' , text=f"""<b>O'qituvchi haqida ijobiy fikr</b>: {malumotlar['teacher_p']}
<b>O'qituvchi haqida salbiy fikr</b>: {malumotlar['teacher_n']}
<b>O'qituvchi ismi va o'qituvchiga 0 dan 10 gacha baho</b>: {malumotlar['teacher_score']}
<b>Markazga takliflaringiz</b>: {malumotlar['valiteach']}
""")
    await message.answer(text="""Fikr-mulohazangiz uchun rahmat!

Hurmatli foydalanuvchi, sizning fikrlaringiz uchun katta rahmat! Biz sizning taklif va mulohazalaringizni albatta inobatga olamiz va xizmatlarimizni yanada yaxshilash uchun ulardan foydalanamiz.

🌟 Sizning ishtirokingiz va qo'llab-quvvatlashingiz biz uchun juda qadrli!

Agar yana biror narsa haqida o'z fikringizni bildirmoqchi bo'lsangiz, istalgan vaqtda biz bilan bog'lanishingiz mumkin.""")