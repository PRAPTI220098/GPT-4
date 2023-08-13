import os
import requests
import json
from translate import Translator
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

F = '\033[1;32m' #Ø§Ø®Ø¶Ø±
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
PN="\033[1;35m" #PINK

# Set up the bot with your bot token
bot = telebot.TeleBot('6222084445:AAEWvWpWiY7Yec3Ne0HnxauZjM4B9ymR1nE')

def chat_with_gpt(message_text):
    api_url = f'https://hercai.onrender.com/v2/hercai?question={message_text}'
    response = requests.get(api_url).text
    return response

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    buttons = [InlineKeyboardButton("👨🏻‍💻 Developer", url='https://t.me/S4NCHIT'),
               InlineKeyboardButton("📣 Channel", url='https://t.me/+Q5RcaQe268lmYmI9')]
    reply_markup = InlineKeyboardMarkup([buttons])
    
    welcome_message = f"👋 Hi {message.from_user.first_name}!\n\n" \
                      f"😃 Welcome to SanchitGPT BOT!\n\n" \
                      f"💬 I am here to answer your questions and have a conversation with you.\n\n" \
                      f"✨ Just type your message, and I'll do my best to respond.\n\n" \
                      f"👨🏻‍💻 If you need to contact the developer or join the channel, check the buttons below.\n"

    bot.send_message(chat_id=chat_id, text=welcome_message, reply_markup=reply_markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    chat_id = message.chat.id

    if user_input.lower() == 'exit':
        bot.send_message(chat_id, "Goodbye!")
        return

    print(f"{C}{message.from_user.first_name}: {Y}{user_input}\n\n")

    # Check if the user asked about Sanchit Vishwakarma
    if "who is sanchit vishwakarma" in user_input.lower():
        sanchit_response = ("Sanchit Vishwakarma is not just a skilled Python developer, "
                            "but also an adept hacker, all while currently pursuing his studies in the tenth grade. "
                            "His mastery over Python allows him to create digital marvels with ease. "
                            "Beyond the world of coding, he fearlessly delves into the intricacies of hacking, "
                            "showcasing his cool confidence and establishing himself as a true virtuoso in both realms.")

    else:
        # Send the 🤔 emoji to indicate processing
        bot.send_chat_action(chat_id=chat_id, action='typing')

        response_json = chat_with_gpt(user_input)
        response_dict = json.loads(response_json)
    
        response_text = response_dict.get("reply", "I'm not sure how to respond.")
    
        # Replace "Herc.ai" with "Sanchit.ai" in the response text
        response_text = response_text.replace("Herc.ai", "Sanchit.ai")
    
        # Translate the response to English
        translator = Translator(to_lang="en", from_lang="tr")
        translated_response = translator.translate(response_text)
    
        cleaned_response = translated_response.replace("@User!", message.from_user.first_name)
        cleaned_response = cleaned_response.replace("@user!", message.from_user.first_name)
        cleaned_response = cleaned_response.replace("@User server", "Sanchit's")
        cleaned_response = cleaned_response.replace("fivesobes", "Sanchit Vishwakarma")
        cleaned_response = cleaned_response.replace("Chatai", "Hacker x SP")
        cleaned_response = cleaned_response.replace("Sanchit's Discord server", "Sanchit's Private Server")

        # Remove any leading or trailing whitespaces
        cleaned_response = cleaned_response.strip()

        # Send the cleaned response as a reply
        bot.send_message(chat_id=chat_id, text=cleaned_response)
        print(f"{C}Answer: {Y}{cleaned_response}\n\n")

# Rest of your code about 'polling' and bot setup remains the same

# Start the bot
bot.polling()
