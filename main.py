import requests
import telebot
from telebot import types

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
bot_token = '6222084445:AAEp3MD8bjXN3xTAzm9NVTZU593IHgUtkIY'
bot = telebot.TeleBot(bot_token)

# Replace 'YOUR_API_ENDPOINT' with the provided API endpoint
api_endpoint = 'https://gptzaid.zaidbot.repl.co/1/text={message_text}'

# Start command handler
@bot.message_handler(commands=['start'])
def start(message):
    buttons = types.InlineKeyboardMarkup(row_width=2)
    but1 = types.InlineKeyboardButton(text='👨🏻‍💻 Developer', url='https://t.me/S4NCHIT')
    but2 = types.InlineKeyboardButton(text='🤡 Channel', url='https://t.me/+Q5RcaQe268lmYmI9')
    buttons.add(but1, but2)
    bot.send_message(message.chat.id, text=f"•⚜️ Hii {message.from_user.first_name} \n\n•😘 Welcome To SanchitGPT BOT\n\n•😇 Please Ask Your Questions\n\n•🙇 I Hope Can Help You 👍", reply_to_message_id=message.message_id, reply_markup=buttons)

# Message handler
@bot.message_handler(func=lambda message: True)
def reply_to_message(message):
    # Get the user's message
    user_message = message.text

    # Call the GPT API to get the response
    response = requests.get(api_endpoint.format(message_text=user_message)).text

    # Send the response back to the user
    bot.send_message(message.chat.id, response)

# Start the bot
bot.polling()
