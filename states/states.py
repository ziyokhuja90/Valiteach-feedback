from aiogram.fsm.state import StatesGroup , State


class feedback_state(StatesGroup):
    teacher_p = State()
    teacher_n = State()
    teacher_score = State()
    valiteach = State()