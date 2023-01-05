import time
import telebot
import requests
from bs4 import BeautifulSoup

# Create an instance of the TeleBot class
bot = telebot.TeleBot('place_for_your_own_token')
# link for parsing
url = 'https://investzoloto.ru/gold-sber-oms/'


def parse_price():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    # Get text with necessary gold price
    gold_text = soup.find('div', class_='object').text
    gold_price = []
    # Search in gold_text:
    # "На 03.01.2023 Покупка: 3808.00 руб./гр.Продажа: 4424.00 руб./гр.+1.58%"
    # values of gold_price:
    # [3808.0, 4424.0]
    for t in gold_text.split():
        try:
            gold_price.append(float(t))
        except ValueError:
            pass
    return gold_price


def start_bot():
    # Define a message handler which handles incoming /start command
    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'Я на связи. Теперь, если курс золота превысит 4000, то ты узнаешь об этом!')
        while True:
            # Return message only in case if the price is above 4000
            if parse_price()[0] > 4000:
                bot.send_message(m.chat.id, "Продажа: " + str(parse_price()[0]) + "\nПокупка: " + str(parse_price()[1]))
            # parse_price() call every hour
            time.sleep(3600)

    # Define a message handler which handles incoming user text -> manual parse_price() call
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        bot.send_message(message.chat.id, "Продажа: " + str(parse_price()[0]) + "\nПокупка: " + str(parse_price()[1]))

    # Start the bot
    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    start_bot()
