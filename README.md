<p align="center"><img src="/images/banner.jpg"></p>

![banner](/images/banner.jpg)

# Imagebot
A Telegram bot for searching image

### Demo
<p align="center"><img src="/images/bot.gif"></p>

### Register a bot on [Telegram](https://t.me/botfather)
1. Open Telegram
2. Search @ botfather
3. Type /newbot .
4. It will show “Alright, a new bot. How are we going to call it? Please choose a name for your bot.”
5. Type the name of your bot.
6. you can access your botusing such url `https://telegram.me/YOUR_BOT_USERNAME` 
7. your token should seems like this: `752713328:AAFQYLO6CJJnrwKnfo9MSqZUjCiue5XYYrw`


### Requirements
- `requests`for handlying api 
- `python-telegram-bot` library to acccess telegram apis

Importing required libraries
```python
from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler,Filters
import requests
```

Get Tokens
```python
token = 'xxxxxxxxxxxxxxxxxxxxxx'
YOUR_ACCESS_KEY = "xxxxxxxxxxxxxxxxxxxxxxx"
```

There are multiple image search apis available, I will be using [unsplash](https://unsplash.com/) api here
```
search_api = "https://api.unsplash.com/search/photos"
```

Write a function that with take search keyword as input and will return image url
```python
def get_img_url(userinput):
    result = requests.get(search_api+"/?query="+userinput+"&client_id=" + YOUR_ACCESS_KEY).json()
    print("url",result['results'][0]['urls']['small'])
    return result['results'][0]['urls']['small']
```

write a function that will respond to user's message or search keyword
```python
def reply(update, context):
    # get user's message string
    user_input = update.message.text
    
    # get user's chat id
    chat_id = update.message.chat_id
    print(user_input)
    
    # get image url from api
    url = get_img_url(user_input)
    print(url)
    
    # Reply or send  msg / image url to user
    update.message.reply_text("search keyword: "+user_input+"\nURL:"+url)
```

Write main function
```python
def main():
    # pass the bot token
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()
```

### Execution
`python imagebot.py`


### References
- [Learn-to-build-your-first-bot-in-telegram-with-python](https://www.freecodecamp.org/news/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4/)
