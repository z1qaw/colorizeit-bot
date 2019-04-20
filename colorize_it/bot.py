import telebot
import connections
import _config
import colorize_it_api
import random
import string as stri
import base64

telebot.apihelper.proxy = {'https':'socks5://127.0.0.1:9050'}
bot = telebot.TeleBot(_config.TELEGRAM_BOT_API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, _config.START_MESSAGE)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, _config.HELP_MESSAGE)

@bot.message_handler(commands=['privacy'])
def send_welcome(message):
	bot.reply_to(message, _config.PRIVACY_POLICY_MESSAGE)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, _config.JUST_TEXT_MESSAGE)

@bot.message_handler(content_types=["photo"])
def send_colorized_photo(message):
    print('Getting photo')

    file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    random_name = ''.join(random.choice(stri.ascii_uppercase + stri.digits) for _ in range(20))

    with open(random_name + '.jpg', 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_message(message.chat.id, _config.SORRY_WAIT_MESSAGE)

    print('Sending photo...')
    out = colorize_it_api.send_pic(new_file, random_name)

    print('Photo was getted. Saving.')
    f = open(random_name + '.png', 'wb')
    f.write(out)
    f.close()

    out = open(random_name + '.png', 'rb')
    bot.send_photo(message.chat.id, out)
    print('Photo was sended.')

if __name__ == '__main__':
    bot.polling(none_stop=True)
