# -*- coding: utf-8 -*-
"""
@author: kate
"""
'''
pip install telegram
pip install python-telegram-bot==13.13
'''

from warehouse_db import (
    create_tables, fillup_tables, get_goods_list, get_item_quantity,
    set_item_quantity, add_item, delete_item, get_all_goods_info
    )
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

with open('warehouse_credenials.txt') as f:
    credenials = {line.split('=')[0]: line.split('=')[1][:-1] for line in f.readlines()}

bot = telegram.Bot(token=credenials['TG_bot_token'])
    
def start(update, context):
    text = ('Добро пожаловать на склад!\n' +
            'Используейте /help для получения дополнительной информации.')
    context.bot.send_message(update.effective_chat.id, text=text)


def handle_request(update, context):
    """Parse a request and route it to the appropriate function"""
    text = update.message.text.split(' ')
    command, args = text[0], text[1:]
    
    if command == '/default_fillup':
        create_tables()
        fillup_tables()
    elif command == '/show_goods':
        goods = get_goods_list()
        bot.send_message(chat_id=update.effective_chat.id, text=', '.join(goods))
    elif command == '/show_warehouse':
        goods = get_all_goods_info()
        bot.send_message(chat_id=update.effective_chat.id, text='\n'.join(goods))
    elif command == '/get_item_quantity':
        item_name = args[0]
        item_quantity = get_item_quantity(item_name)
        text = 'item ' + str(item_name) + ' quantity is ' + str(item_quantity)
        bot.send_message(chat_id=update.effective_chat.id, text=text)
    elif command == '/add_quantity':
        item_name = str(args[0])
        added_quantity = int(args[1])
        old_quantity = get_item_quantity(item_name)
        set_item_quantity(item_name, old_quantity + added_quantity)
    elif command == '/reduce_quantity':
        item_name = str(args[0])
        added_quantity = int(args[1])
        old_quantity = get_item_quantity(item_name)
        set_item_quantity(item_name, old_quantity - added_quantity)
    elif command == '/add_item':
        item_name = str(args[0])
        item_quantity = int(args[1])
        add_item(item_name, item_quantity)
    elif command == '/delete_item':
        item_name = str(args[0])
        delete_item(item_name)
    elif command == '/help':
        text = ('/default_fillup - заполнение по умолчанию\n' +
                '/show_goods - показать товары\n' +
                '/show_warehouse - показать все данные о товарах склада\n' +
                '/get_item_quantity item_name - количество этого товара\n' +
                '/add_quantity name quantity - увеличить количество товара\n' +
                '/reduce_quantity name quantity - уменьшить количество товара\n' +
                '/add_item name quantity - добавить новый товар\n' +
                '/delete_item name - удалить товар из базы\n'
                )
        bot.send_message(chat_id=update.effective_chat.id, text=text)
    else:
        bot.send_message(chat_id=update.effective_chat.id, text='Invalid command. Use /help')

def main():
    updater = Updater(credenials['TG_bot_token'])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, handle_request))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()