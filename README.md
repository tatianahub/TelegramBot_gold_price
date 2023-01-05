# <p align="center">Telegram Bot (price parser)<img src="https://www.17thshard.com/forum/uploads/monthly_2021_01/large.6012ee0ede275_Shinygoldcoin.gif.cf6c0a52a8988d961ecf12a146344ab1.gif" width=40px>

This Telegram Bot is written in Python 3.8 for parsing current gold price extracted from web page. 

### Getting started

1. There is a way how to install necessary libraries:

    ```
    pip3 install -r requirements.txt
    ```

2. To use this Telegram Bot you should get your own API token:

   * Find telegram bot named "@botfarther".
   * To create a new bot type “/newbot”.

3. Add your own TOKEN to this code:

    ```
   bot = telebot.TeleBot('place_for_your_own_token')
    ```
4. Start Telegram Bot:
   ```
   python3 telegram_bot.py
   ```
