import telebot
import threading
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

# Temporary user session store (you can replace with database)
user_sessions = {}

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Welcome to the Testbook Extractor Bot!\n\n"
        "Use the following commands:\n"
        "/login - Log in to Testbook using your mobile number\n"
        "/fetch - Send a Testbook test series link to extract it"
    )

@bot.message_handler(commands=["login"])
def login(message):
    msg = bot.send_message(message.chat.id, "Please send your mobile number to login:")
    bot.register_next_step_handler(msg, process_mobile_number)

def process_mobile_number(message):
    mobile = message.text.strip()
    chat_id = message.chat.id
    user_sessions[chat_id] = {"mobile": mobile}
    
    # Simulate OTP sending (replace with actual request to Testbook)
    bot.send_message(chat_id, f"OTP sent to {mobile}. Please enter the OTP:")
    bot.register_next_step_handler(message, process_otp)

def process_otp(message):
    otp = message.text.strip()
    chat_id = message.chat.id

    # Simulate login success (replace with actual login request to Testbook)
    user_sessions[chat_id]["otp"] = otp
    bot.send_message(chat_id, "Login successful! Now you can use /fetch to download tests.")

@bot.message_handler(commands=["fetch"])
def fetch(message):
    msg = bot.send_message(message.chat.id, "Send the Testbook test series URL:")
    bot.register_next_step_handler(msg, process_url)

def process_url(message):
    url = message.text.strip()
    chat_id = message.chat.id

    # Simulate fetching and sending the test
    # In real usage, fetch test data, generate HTML, send via bot
    if "testbook.com" in url:
        bot.send_message(chat_id, f"Fetching test series from: {url}")
        # Replace with actual scraping and HTML formatting logic
        bot.send_message(chat_id, "<b>[Test]</b> Sample HTML test would be sent here.", parse_mode="HTML")
    else:
        bot.send_message(chat_id, "Invalid Testbook URL. Please try again.")

def run_bot():
    bot.polling(non_stop=True)

# Uncomment if you want to test locally
# if __name__ == "__main__":
#     run_bot()