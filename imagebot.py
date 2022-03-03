#!/usr/bin/env python
# Author: Ajinkya Pathak

from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler,Filters
import requests
import re

token = 'xxxxxxxxxxxxxxxxxxxxxx'
YOUR_ACCESS_KEY = "xxxxxxxxxxxxxxxxxxxxxxx"
search_api = "https://api.unsplash.com/search/photos"

def do_something(user_input):
    answer = "You have wrote me " + user_input
    return answer

def get_img_url(userinput):
    result = requests.get(search_api+"/?query="+userinput+"&client_id=" + YOUR_ACCESS_KEY).json()
    print("url",result['results'][0]['urls']['small'])
    return result['results'][0]['urls']['small']

def reply(update, context):
    user_input = update.message.text
    chat_id = update.message.chat_id
    print(user_input)
    url = get_img_url(user_input)
    print(url)
    update.message.reply_text("search keyword: "+user_input+"\nURL:"+url)

def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


