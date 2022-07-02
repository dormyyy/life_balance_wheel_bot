from aiogram.dispatcher.filters.state import StatesGroup, State


class Steps(StatesGroup):
    startState = State()
    regState = State()
    defaultState = State()
    wheel_creationState = State()
    wheel_updatingState = State()
    wheel_editingState = State()
    set_career_valueState = State()
    set_family_valueState = State()
    set_environment_valueState = State()
    set_hobbies_valueState = State()
    set_rest_valueState = State()
    set_education_valueState = State()
    set_health_valueState = State()
    edit_career_valueState = State()
    edit_family_valueState = State()
    edit_environment_valueState = State()
    edit_hobbies_valueState = State()
    edit_rest_valueState = State()
    edit_education_valueState = State()
    edit_health_valueState = State()
    confirmState = State()
    showState = State()
