#!/usr/bin/python3.10
#! /usr/bin/env python
# -* - coding: utf-8-*-﻿
from distutils.cmd import Command
from telebot import types
import os
import random
from glob import glob
from random import randint
import telebot

bot = telebot.TeleBot('6780076816:AAHqj4-CGjOu4DVTZpNXQaMhcd6NGGkpk8w');

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.KeyboardButton(text='Начать играть')
    markup.add(keyboard)
    photo = open(r"C:\Users\Алексей\Desktop\ajnj\pct\2024-02-19_23-38-24.png", 'rb')
    bot.send_photo(message.from_user.id, photo=photo)
    bot.send_message(message.from_user.id, 'Приветствуем в нашем боте с мини-играми. Здесь ты можешь отвлечься, расслабиться и просто получить удовольствие!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
   if message.text.lower() == "начать играть":
       kbPhoto = telebot.types.ReplyKeyboardMarkup()
       kbPhoto.row('Games menu')
       kbPhoto.row('/help')
       bot.send_message(message.from_user.id, 'Выбери, что ты хочешь увидеть)', reply_markup = kbPhoto)
   elif message.text == "/help":
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard = types.KeyboardButton(text='Начать играть')
       markup.add(keyboard)
       bot.send_message(message.from_user.id, "Приветствуем тебя в нашем игровом боте! Список доступных команд: \n\n/start - для перезапуска бота \n\nПомни, что играть нужно ради развлечения, а не из чувства азарта. Создатели не несут никакой ответственности за развитие лудомании! Удачи!", reply_markup = markup)
       bot.send_message(message.from_user.id, "Нажми на кнопочку ниже", reply_markup = markup)
   elif message.text == "Games menu":
       bot.send_message(message.from_user.id, "В разработке")
   else:
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard = types.KeyboardButton(text='/help')
       markup.add(keyboard)
       bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.", reply_markup = markup)



bot.polling( none_stop = True, interval=0 )
