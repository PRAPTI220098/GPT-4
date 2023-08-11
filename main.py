try:
	import os
	from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import requests
import json
from googletrans import Translator
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
except ModuleNotFoundError:
	os.system('pip install Updatet')
	os.system('pip install MessageHandler')
	os.system('pip install Filters')
	os.system('pip install CommandHandler')
	os.system('pip install os')
	os.system('pip install requests')
	os.system('pip install googletrans')
	os.system('pip install json')
	os.system("pip install Translator")
	os.system("pip install InlineKeyboardButton")
	os.system("pip install InlineKeyboardMarkup")
	os.system("pip install python-telegram-bot")
	os.system("pip install googletrans==4.0.0-rc1")
	os.system("clear")

# Your existing code here (import statements and other code)
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import requests
import json
from googletrans import Translator
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Now you can continue with the rest of your code

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

# Create an instance of the Updater class with your bot token
updater = Updater(token='6222084445:AAEWvWpWiY7Yec3Ne0HnxauZjM4B9ymR1nE', use_context=True)
dispatcher = updater.dispatcher

def chat_with_gpt(message_text):
    api_url = f'https://hercai.onrender.com/v2/hercai?question={message_text}'
    response = requests.get(api_url).text
    return response

def start(update, context):
    chat_id = update.message.chat.id
    buttons = [
        [InlineKeyboardButton("👨🏻‍💻 Developer", url='https://t.me/S4NCHIT')],
        [InlineKeyboardButton("📣 Channel", url='https://t.me/+Q5RcaQe268lmYmI9')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    welcome_message = f"👋 Hi {update.message.from_user.first_name}!\n\n" \
                      f"😃 Welcome to SanchitGPT BOT!\n\n" \
                      f"💬 I am here to answer your questions and have a conversation with you.\n\n" \
                      f"✨ Just type your message, and I'll do my best to respond.\n\n" \
                      f"👨🏻‍💻 If you need to contact the developer or join the channel, check the buttons below.\n"

    context.bot.send_message(chat_id=chat_id, text=welcome_message, reply_markup=reply_markup)

def handle_message(update, context):
    user_input = update.message.text
    chat_id = update.message.chat.id

    if user_input.lower() == 'exit':
        context.bot.send_message(chat_id, "Goodbye!")
        return

    print(f"{C}User: {Y}{user_input}\n\n")

    # Check if the user asked about Sanchit Vishwakarma
    if "who is sanchit vishwakarma" in user_input.lower():
        sanchit_response = ("Sanchit Vishwakarma is not just a skilled Python developer, "
                            "but also an adept hacker, all while currently pursuing his studies in the tenth grade. "
                            "His mastery over Python allows him to create digital marvels with ease. "
                            "Beyond the world of coding, he fearlessly delves into the intricacies of hacking, "
                            "showcasing his cool confidence and establishing himself as a true virtuoso in both realms.")
        
        # Send the response about Sanchit Vishwakarma
        context.bot.send_message(chat_id=chat_id, text=sanchit_response)
    else:
        # Send the 🤔 emoji and typing action to indicate processing
        context.bot.send_chat_action(chat_id=chat_id, action='typing')
        reply = context.bot.send_message(chat_id=chat_id, text="🤔", reply_to_message_id=update.message.message_id)

        response_json = chat_with_gpt(user_input)
        response_dict = json.loads(response_json)
    
        response_text = response_dict.get("reply", "I'm not sure how to respond.")
    
        # Replace "Herc.ai" with "Sanchit.ai" in the response text
        response_text = response_text.replace("Herc.ai", "Sanchit.ai")
    
        # Translate the response to English
        translator = Translator()
        translated_response = translator.translate(response_text, src='auto', dest='en').text
    
        # Remove the "@User" mention from the response
        cleaned_response = translated_response.replace("@User", "")
        
        # Remove any leading or trailing whitespaces
        cleaned_response = cleaned_response.strip()
    
        # Send the cleaned response as a reply
        context.bot.send_message(chat_id=chat_id, text=cleaned_response, reply_to_message_id=reply.message_id)
        print(f"{C}Answer: {Y}{cleaned_response}\n\n")

def main():
    print(f"{PN}ChatGPT Telegram Bot is running...\n")

# Register the command handlers and message handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()

if __name__ == "__main__":
    main()
