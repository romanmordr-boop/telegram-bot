import telebot  
from buttons import create_menu  

TOKEN = ''  
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = create_menu()  
    bot.reply_to(message, "Привет. Это бот, созданный при поддержке горького, но все же опыта Ежа, Жирафа, РДС и других. Надеюсь здесь вы найдете данные необходимые в помощи с обслуживанием вашего бегемота. Выбери опцию из меню:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "diag":
        bot.send_message(call.message.chat.id, "Оливковое в AJ, в остальное подсолнечное. ")
    elif call.data == "about":
        bot.send_message(call.message.chat.id, "Проверяются ударами отверткой, но можно не пыжиться, результат известен заранее.")
    elif call.data == "play":
        bot.send_message(call.message.chat.id, "Ну, дороже смысла нет)")
    bot.answer_callback_query(call.id)  

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты сказал: {message.text}")

bot.polling()
