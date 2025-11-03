from telebot import types 


def create_menu():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Диагностика", callback_data="diag")
    btn2 = types.InlineKeyboardButton("Лонжероны", callback_data="about")
    btn3 = types.InlineKeyboardButton("Продажа за 150", callback_data="play")
    markup.add(btn1, btn2, btn3)  
    return markup
