#!/bin/python3

import telebot
from telebot import types
import os
import time

bot = telebot.TeleBot("***TOKEN***")
i = 1

#Создаем бесконечный цикл проверки температуры
while i > -1:
    os.system("/media/nextcloud/projects/cpunotify/cpu.sh")
    file = open('/media/nextcloud/projects/cpunotify/cpu_temp', 'r')
    te = file.read()
    te = int(te)

    t = int('70')   #Выставляем нужную нам температуру после которой будут приходить уведомления
    #print(type(t))
    
    if te > t: #Создаем условие, если температура поднимается выше которой мы указали, то отправляем сообщение в тг
        bot.send_message(935991394, 'Оу, как горячо, чекни почему так жарко: ' + str(te) + '°C')

    #Задаем интервал проверки  температуры и отправки уведомлений в телеграм
    time.sleep(5)   #В данном случае каждые 5 секунд будет проверяться температура и каждые 5 секунд спамить в телеграм
