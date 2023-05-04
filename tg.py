import telebot #импорт pyTelegramBotAPI 
from telebot import types #также достанем типы
import config
import openpyxl


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    item1 = types.KeyboardButton('Расписание')      
    item2 = types.KeyboardButton('Последние новости')
    item4 = types.KeyboardButton('Сайт гимназии')
    item5 = types.KeyboardButton('Электронный дневник')
    markup.add(item1,item2,item4,item5)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Это главное меню' .format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def a5(message):
    if message.chat.type == 'private':
        if message.text == 'Расписание':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            itemA = types.KeyboardButton('А')
            itemB = types.KeyboardButton('Б')
            itemV = types.KeyboardButton('В')
            itemBack = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA,itemB,itemV,itemBack)
            bot.send_message(message.chat.id, 'Выбери букву', reply_markup = markup)  
        if message.text == 'Главное меню 📃':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
            item1 = types.KeyboardButton('Расписание')      
            item2 = types.KeyboardButton('Последние новости')
            item4 = types.KeyboardButton('Сайт гимназии')
            item5 = types.KeyboardButton('Электронный дневник')
            markup.add(item1,item2,item4,item5)
            bot.send_message(message.chat.id, 'Главное меню:' .format(message.from_user), reply_markup = markup)
        if message.text == 'А':
            markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
            item5 = types.KeyboardButton('5️⃣ А')      
            item6 = types.KeyboardButton('6️⃣ А')
            item7 = types.KeyboardButton('7️⃣ А')
            item8 = types.KeyboardButton('8️⃣ А')
            item9 = types.KeyboardButton('9️⃣ А')
            item10 = types.KeyboardButton('🔟 А')
            item11 = types.KeyboardButton('1️⃣1️⃣ А')
            itemclass = types.KeyboardButton('Выбор буквы ⬅️')
            markup.add(item5,item6,item7,item8,item9,item10,item11,itemclass)
            bot.send_message(message.chat.id, 'Выбери класс', reply_markup = markup)
        if message.text == 'Выбор буквы ⬅️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            itemA = types.KeyboardButton('А')
            itemB = types.KeyboardButton('Б')
            itemV = types.KeyboardButton('В')
            itemBack = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA,itemB,itemV,itemBack)
            bot.send_message(message.chat.id, 'Выбери букву', reply_markup = markup)        
        if message.text == '5️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 5️⃣ А')         
            itemTuesday = types.KeyboardButton('Вторник 5️⃣ А')
            itemWednsday = types.KeyboardButton('Среда 5️⃣ А')
            itemThursday = types.KeyboardButton('Четверг 5️⃣ А')
            itemFriday = types.KeyboardButton('Пятница 5️⃣ А')
            itemSaturday = types.KeyboardButton('Суббота 5️⃣ А')
            itemBack = types.KeyboardButton('Выбор класса(А)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday, itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Выбор класса(А)⬅️':
            markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
            item5 = types.KeyboardButton('5️⃣ А')      
            item6 = types.KeyboardButton('6️⃣ А')
            item7 = types.KeyboardButton('7️⃣ А')
            item8 = types.KeyboardButton('8️⃣ А')
            item9 = types.KeyboardButton('9️⃣ А')
            item10 = types.KeyboardButton('🔟 А')
            item11 = types.KeyboardButton('1️⃣1️⃣ А')
            itemclass = types.KeyboardButton('Выбор буквы ⬅️')
            markup.add(item5,item6,item7,item8,item9,item10,item11,itemclass)
            bot.send_message(message.chat.id, 'Выбери класс', reply_markup = markup)
        if message.text == 'Понедельник 5️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,10):
                result = sheet[row][0].value + " " + sheet[row][1].value
                bot.send_message(message.chat.id, result, parse_mode = "HTML", reply_markup = markup)
        elif message.text == 'Вторник 5️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][1].value, 
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 5️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][1].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 5️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][1].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 5️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][1].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 5️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][1].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '6️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 6️⃣ А')         
            itemTuesday = types.KeyboardButton('Вторник 6️⃣ А')
            itemWednsday = types.KeyboardButton('Среда 6️⃣ А')
            itemThursday = types.KeyboardButton('Четверг 6️⃣ А')
            itemFriday = types.KeyboardButton('Пятница 6️⃣ А')
            itemSaturday = types.KeyboardButton('Суббота 6️⃣ А')
            itemBack = types.KeyboardButton('Выбор класса(А)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 6️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][4].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 6️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][4].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 6️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][4].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 6️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][4].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 6️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][4].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 6️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][4].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '7️⃣ А': 
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 7️⃣ А')         
            itemTuesday = types.KeyboardButton('Вторник 7️⃣ А')
            itemWednsday = types.KeyboardButton('Среда 7️⃣ А')
            itemThursday = types.KeyboardButton('Четверг 7️⃣ А')
            itemFriday = types.KeyboardButton('Пятница 7️⃣ А')
            itemSaturday = types.KeyboardButton('Суббота 7️⃣ А')
            itemBack = types.KeyboardButton('Выбор класса(А)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 7️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][7].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 7️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][7].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 7️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][7].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 7️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][7].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 7️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][7].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 7️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][7].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '8️⃣ А': 
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 8️⃣ А')         
            itemTuesday = types.KeyboardButton('Вторник 8️⃣ А')
            itemWednsday = types.KeyboardButton('Среда 8️⃣ А')
            itemThursday = types.KeyboardButton('Четверг 8️⃣ А')
            itemFriday = types.KeyboardButton('Пятница 8️⃣ А')
            itemSaturday = types.KeyboardButton('Суббота 8️⃣ А')
            itemBack = types.KeyboardButton('Выбор класса(А)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 8️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][10].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 8️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][10].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 8️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][10].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 8️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][10].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 8️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][10].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 8️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][10].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '9️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 9️⃣ А')         
            itemTuesday = types.KeyboardButton('Вторник 9️⃣ А')
            itemWednsday = types.KeyboardButton('Среда 9️⃣ А')
            itemThursday = types.KeyboardButton('Четверг 9️⃣ А')
            itemFriday = types.KeyboardButton('Пятница 9️⃣ А')
            itemSaturday = types.KeyboardButton('Суббота 9️⃣ А')
            itemBack = types.KeyboardButton('Выбор класса(А)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 9️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][13].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 9️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][13].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 9️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][13].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 9️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][13].value
                bot.send_message(message.chat.id, result)
        elif message.text == 'Пятница 9️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][13].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 9️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][13].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '🔟 А':
            markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 🔟А')         
            itemTuesday = types.KeyboardButton('Вторник 🔟А')
            itemWednsday = types.KeyboardButton('Среда 🔟А')
            itemThursday = types.KeyboardButton('Четверг 🔟А')
            itemFriday = types.KeyboardButton('Пятница 🔟А')
            itemSaturday = types.KeyboardButton('Суббота 🔟А')
            itemBack = types.KeyboardButton('Выбор класса(А)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 🔟А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][16].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 🔟А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][16].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 🔟А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][16].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 🔟А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][16].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 🔟А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][16].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 🔟А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][16].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '1️⃣1️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 1️⃣1️⃣ А')         
            itemTuesday = types.KeyboardButton('Вторник 1️⃣1️⃣ А')
            itemWednsday = types.KeyboardButton('Среда 1️⃣1️⃣ А')
            itemThursday = types.KeyboardButton('Четверг 1️⃣1️⃣ А')
            itemFriday = types.KeyboardButton('Пятница 1️⃣1️⃣ А')
            itemSaturday = types.KeyboardButton('Суббота 1️⃣1️⃣ А')
            itemBack = types.KeyboardButton('Выбор класса(А)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 1️⃣1️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][18].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 1️⃣1️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][18].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 1️⃣1️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][18].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 1️⃣1️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][18].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 1️⃣1️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][18].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 1️⃣1️⃣ А':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][18].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == 'Б':
            markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
            item5 = types.KeyboardButton('5️⃣ Б')      
            item6 = types.KeyboardButton('6️⃣ Б')
            item7 = types.KeyboardButton('7️⃣ Б')
            item8 = types.KeyboardButton('8️⃣ Б')
            item9 = types.KeyboardButton('9️⃣ Б')
            item10 = types.KeyboardButton('🔟Б')
            item11 = types.KeyboardButton('1️⃣1️⃣ Б')
            itemBack = types.KeyboardButton('Выбор буквы ⬅️')
            markup.add(item5,item6,item7,item8,item9,item10,item11,itemBack)
            bot.send_message(message.chat.id, 'Выбери класс', reply_markup = markup)
        if message.text == 'Выбор класса(Б)⬅️':
            markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
            item5 = types.KeyboardButton('5️⃣ Б')      
            item6 = types.KeyboardButton('6️⃣ Б')
            item7 = types.KeyboardButton('7️⃣ Б')
            item8 = types.KeyboardButton('8️⃣ Б')
            item9 = types.KeyboardButton('9️⃣ Б')
            item10 = types.KeyboardButton('🔟 Б')
            item11 = types.KeyboardButton('1️⃣1️⃣ Б')
            itemclass = types.KeyboardButton('Выбор буквы ⬅️')
            markup.add(item5,item6,item7,item8,item9,item10,item11,itemclass)
            bot.send_message(message.chat.id, 'Выбери класс', reply_markup = markup)
        if message.text == '5️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 5️⃣ Б')         
            itemTuesday = types.KeyboardButton('Вторник 5️⃣ Б')
            itemWednsday = types.KeyboardButton('Среда 5️⃣ Б')
            itemThursday = types.KeyboardButton('Четверг 5️⃣ Б')
            itemFriday = types.KeyboardButton('Пятница 5️⃣ Б')
            itemSaturday = types.KeyboardButton('Суббота 5️⃣ Б')
            itemBack = types.KeyboardButton('Выбор класса(Б)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 5️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][2].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 5️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][2].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 5️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][2].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 5️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][2].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 5️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][2].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 5️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][2].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '6️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 6️⃣ Б')         
            itemTuesday = types.KeyboardButton('Вторник 6️⃣ Б')
            itemWednsday = types.KeyboardButton('Среда 6️⃣ Б')
            itemThursday = types.KeyboardButton('Четверг 6️⃣ Б')
            itemFriday = types.KeyboardButton('Пятница 6️⃣ Б')
            itemSaturday = types.KeyboardButton('Суббота 6️⃣ Б')
            itemBack = types.KeyboardButton('Выбор класса(Б)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 6️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][5].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 6️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][5].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 6️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][5].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 6️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][5].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 6️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][5].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 6️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][5].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '7️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 7️⃣ Б')         
            itemTuesday = types.KeyboardButton('Вторник 7️⃣ Б')
            itemWednsday = types.KeyboardButton('Среда 7️⃣ Б')
            itemThursday = types.KeyboardButton('Четверг 7️⃣ Б')
            itemFriday = types.KeyboardButton('Пятница 7️⃣ Б')
            itemSaturday = types.KeyboardButton('Суббота 7️⃣ Б')
            itemBack = types.KeyboardButton('Выбор класса(Б)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 7️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][8].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 7️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][8].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 7️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][8].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 7️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][8].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 7️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][8].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 7️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][8].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '8️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 8️⃣ Б')         
            itemTuesday = types.KeyboardButton('Вторник 8️⃣ Б')
            itemWednsday = types.KeyboardButton('Среда 8️⃣ Б')
            itemThursday = types.KeyboardButton('Четверг 8️⃣ Б')
            itemFriday = types.KeyboardButton('Пятница 8️⃣ Б')
            itemSaturday = types.KeyboardButton('Суббота 8️⃣ Б')
            itemBack = types.KeyboardButton('Выбор класса(Б)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 8️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][11].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 8️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][11].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 8️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][11].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 8️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][11].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 8️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][11].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 8️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][11].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '9️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 9️⃣ Б')         
            itemTuesday = types.KeyboardButton('Вторник 9️⃣ Б')
            itemWednsday = types.KeyboardButton('Среда 9️⃣ Б')
            itemThursday = types.KeyboardButton('Четверг 9️⃣ Б')
            itemFriday = types.KeyboardButton('Пятница 9️⃣ Б')
            itemSaturday = types.KeyboardButton('Суббота 9️⃣ Б')
            itemBack = types.KeyboardButton('Выбор класса(Б)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 9️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][14].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 9️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][14].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 9️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][14].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 9️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][14].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 9️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][14].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 9️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][14].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '🔟Б':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 🔟Б')         
            itemTuesday = types.KeyboardButton('Вторник 🔟Б')
            itemWednsday = types.KeyboardButton('Среда 🔟Б')
            itemThursday = types.KeyboardButton('Четверг 🔟Б')
            itemFriday = types.KeyboardButton('Пятница 🔟Б')
            itemSaturday = types.KeyboardButton('Суббота 🔟Б')
            itemBack = types.KeyboardButton('Выбор класса(Б)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 🔟Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][17].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 🔟Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][17].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 🔟Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][17].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 🔟Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][17].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 🔟Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][17].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 🔟Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][17].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '1️⃣1️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 1️⃣1️⃣ Б')         
            itemTuesday = types.KeyboardButton('Вторник 1️⃣1️⃣ Б')
            itemWednsday = types.KeyboardButton('Среда 1️⃣1️⃣ Б')
            itemThursday = types.KeyboardButton('Четверг 1️⃣1️⃣ Б')
            itemFriday = types.KeyboardButton('Пятница 1️⃣1️⃣ Б')
            itemSaturday = types.KeyboardButton('Суббота 1️⃣1️⃣ Б')
            itemBack = types.KeyboardButton('Выбор класса(Б)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 1️⃣1️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][19].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 1️⃣1️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][19].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 1️⃣1️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][19].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 1️⃣1️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][19].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 1️⃣1️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][19].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 1️⃣1️⃣ Б':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][19].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == 'В':
            markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
            item5 = types.KeyboardButton('5️⃣ В')      
            item6 = types.KeyboardButton('6️⃣ В')
            item7 = types.KeyboardButton('7️⃣ В')
            item8 = types.KeyboardButton('8️⃣ В')
            item9 = types.KeyboardButton('9️⃣ В')
            itemclass = types.KeyboardButton('Выбор буквы ⬅️')
            markup.add(item5,item6,item7,item8,item9,itemclass)
            bot.send_message(message.chat.id, 'Выбери класс', reply_markup = markup)
        if message.text == '5️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 5️⃣ В')         
            itemTuesday = types.KeyboardButton('Вторник 5️⃣ В')
            itemWednsday = types.KeyboardButton('Среда 5️⃣ В')
            itemThursday = types.KeyboardButton('Четверг 5️⃣ В')
            itemFriday = types.KeyboardButton('Пятница 5️⃣ В')
            itemSaturday = types.KeyboardButton('Суббота 5️⃣ В')
            itemBack = types.KeyboardButton('Выбор класса(В)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 5️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][3].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 5️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][3].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 5️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][3].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 5️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][3].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 5️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][3].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 5️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][3].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '6️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 6️⃣ Б')         
            itemTuesday = types.KeyboardButton('Вторник 6️⃣ Б')
            itemWednsday = types.KeyboardButton('Среда 6️⃣ Б')
            itemThursday = types.KeyboardButton('Четверг 6️⃣ Б')
            itemFriday = types.KeyboardButton('Пятница 6️⃣ Б')
            itemSaturday = types.KeyboardButton('Суббота 6️⃣ Б')
            itemBack = types.KeyboardButton('Выбор класса(В)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 6️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][6].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 6️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][6].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 6️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][6].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 6️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][6].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 6️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][6].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 6️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][6].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '7️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 7️⃣ В')         
            itemTuesday = types.KeyboardButton('Вторник 7️⃣ В')
            itemWednsday = types.KeyboardButton('Среда 7️⃣ В')
            itemThursday = types.KeyboardButton('Четверг 7️⃣ В')
            itemFriday = types.KeyboardButton('Пятница 7️⃣ В')
            itemSaturday = types.KeyboardButton('Суббота 7️⃣ В')
            itemBack = types.KeyboardButton('Выбор класса(В)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday, itemBack)
            bot.send_message(message.chat.id, 'Выбери день', reply_markup = markup)
        if message.text == 'Понедельник 7️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][9].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 7️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][9].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 7️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][9].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 7️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][9].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 7️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][9].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 7️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][9].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '8️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 8️⃣ В')         
            itemTuesday = types.KeyboardButton('Вторник 8️⃣ В')
            itemWednsday = types.KeyboardButton('Среда 8️⃣ В')
            itemThursday = types.KeyboardButton('Четверг 8️⃣ В')
            itemFriday = types.KeyboardButton('Пятница 8️⃣ В')
            itemSaturday = types.KeyboardButton('Суббота 8️⃣ В')
            itemBack = types.KeyboardButton('Выбор класса(В)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'ВыВери день', reply_markup = markup)
        if message.text == 'Понедельник 8️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][12].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 8️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][12].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 8️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][12].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 8️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][12].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 8️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][12].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 8️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][12].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == '9️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
            itemMonday = types.KeyboardButton('Понедельник 9️⃣ В')         
            itemTuesday = types.KeyboardButton('Вторник 9️⃣ В')
            itemWednsday = types.KeyboardButton('Среда 9️⃣ В')
            itemThursday = types.KeyboardButton('Четверг 9️⃣ В')
            itemFriday = types.KeyboardButton('Пятница 9️⃣ В')
            itemSaturday = types.KeyboardButton('Суббота 9️⃣ В')
            itemBack = types.KeyboardButton('Выбор класса(В)⬅️')
            markup.add(itemMonday,itemTuesday,itemWednsday,itemThursday,itemFriday,itemSaturday,itemBack)
            bot.send_message(message.chat.id, 'ВыВери день', reply_markup = markup)
        if message.text == 'Понедельник 9️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[0]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][15].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Вторник 9️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[1]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][15].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Среда 9️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[2]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][15].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Четверг 9️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[3]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][15].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Пятница 9️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[4]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][15].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        elif message.text == 'Суббота 9️⃣ В':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
            itemA = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA)
            book = openpyxl.open("monday.xlsx", read_only = True)
            sheet = book.worksheets[5]
            bot.send_message(message.chat.id, "Твое расписание: ")
            for row in range(2,9):
                result = sheet[row][0].value + " " + sheet[row][15].value
                bot.send_message(message.chat.id, result, reply_markup = markup)
        if message.text == 'Выбор класса(В)⬅️':
            markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
            item5 = types.KeyboardButton('5️⃣ В')      
            item6 = types.KeyboardButton('6️⃣ В')
            item7 = types.KeyboardButton('7️⃣ В')
            item8 = types.KeyboardButton('8️⃣ В')
            item9 = types.KeyboardButton('9️⃣ В')
            item10 = types.KeyboardButton('🔟 В')
            item11 = types.KeyboardButton('1️⃣1️⃣ В')
            itemclass = types.KeyboardButton('Выбор буквы ⬅️')
            markup.add(item5,item6,item7,item8,item9,item10,item11,itemclass)
            bot.send_message(message.chat.id, 'Выбери класс', reply_markup = markup)
        if message.text == 'Назад ⬅️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            itemA = types.KeyboardButton('А')
            itemB = types.KeyboardButton('Б')
            itemV = types.KeyboardButton('В')
            itemBack = types.KeyboardButton('Главное меню 📃')
            markup.add(itemA,itemB,itemV,itemBack)
            bot.send_message(message.chat.id, 'Выбери букву', reply_markup = markup)
        if message.text == 'Последние новости':
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Гимназическая научно-практическая конференция «Открытие».", url='https://nrg-ng1.obr.sakha.gov.ru/news/front/view/id/3168907')
            button2 = types.InlineKeyboardButton("Предметная неделя методического объединения учителей математики и информационных технологий", url='https://nrg-ng1.obr.sakha.gov.ru/news/front/view/id/3168892')
            button3 = types.InlineKeyboardButton("«Технологическая викторина» в рамках недели математики, информатики и технологии", url='https://nrg-ng1.obr.sakha.gov.ru/news/front/view/id/3168891')
            button4 = types.InlineKeyboardButton("Массовая гонка «Лыжня России-2023»", url='https://nrg-ng1.obr.sakha.gov.ru/news/front/view/id/3167530')
            button5 = types.InlineKeyboardButton("Cоревнования по ОФП среди ОУ Нерюнгринского района 1 - 4 классы", url='https://nrg-ng1.obr.sakha.gov.ru/news/front/view/id/3167526')
            button6 = types.InlineKeyboardButton("Меню 📃 ", callback_data='mainmenu')
            markup.add(button1,button2,button3,button4,button5,button6)
            bot.send_message(message.chat.id, "Привет, {0.first_name}! Здесь ты можешь посмотреть, последние 5 новостей".format(message.from_user), reply_markup = markup)
        if message.text == 'Сайт гимназии':
            markup = types.InlineKeyboardMarkup(row_width=1)
            button6 = types.InlineKeyboardButton("Меню 📃 ", callback_data='mainmenu')
            sight1 = types.InlineKeyboardButton("Сайт", url='http://www.nerungri.edu.ru/~gym/gym1/')
            markup.add(sight1, button6)
            bot.send_message(message.chat.id, "Ссылка на сайт гимназии", reply_markup = markup)
        if message.text == 'Электронный дневник':
            markup = types.InlineKeyboardMarkup(row_width=1)
            button6 = types.InlineKeyboardButton("Меню 📃 ", callback_data='mainmenu')
            sight1 = types.InlineKeyboardButton("Сайт", url='https://sgo.e-yakutia.ru')
            markup.add(sight1, button6)
            bot.send_message(message.chat.id, "Ссылка на Электронный дневник", reply_markup = markup)
@bot.callback_query_handler(func=lambda c: True)
def callback(call): # мне удобней через переменную `c`, а не `call` или `callback`
    if call.message:
        if call.data == 'mainmenu':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
            item1 = types.KeyboardButton('Расписание')      
            item2 = types.KeyboardButton('Последние новости')
            item4 = types.KeyboardButton('Сайт гимназии')
            item5 = types.KeyboardButton('Электронный дневник')
            markup.add(item1,item2,item4,item5)
            bot.send_message(call.message.chat.id, 'Главное меню:', reply_markup = markup)

#             @bot.callback_query_handler(func=lambda c: True)
# def callback(call): # мне удобней через переменную `c`, а не `call` или `callback`
#     if call.message:
#         cid = call.message.chat.id
#         mid = call.message.message_id
#         kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
#         item1 = types.KeyboardButton('Расписание')      
#         item2 = types.KeyboardButton('Последние новости')
#         item4 = types.KeyboardButton('Сайт гимназии')
#         item5 = types.KeyboardButton('Электронный дневник')
#         kb.add(item1,item2,item4,item5)
#         if call.data == 'mainmenu':
#             bot.edit_message_text('answer', cid, mid, reply_markup=kb, parse_mode='Markdown')
# def ans(call):
#     kb = types.InlineKeyboardMarkup()
#     cid = call.message.chat.id
#     mid = call.message.message_id
#     if call.data == "next":
#         bot.edit_message_text('answer', cid, mid, reply_markup=kb, parse_mode='Markdown')

        # elif call.inline_message_id:
        # if call.data == "test":
        #     bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")
        

bot.polling(none_stop=True) #обязательная для работы бота часть
bot.polling()