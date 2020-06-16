from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
button1 = KeyboardButton('А')
button2 = KeyboardButton('Б')
button3 = KeyboardButton('В')
button4 = KeyboardButton('Г')
button5 = KeyboardButton('Д')

markup1 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).row(button1,button2,button3,button4,button5)
markup2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).row(button1,button2,button3,button4)
