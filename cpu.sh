#!/bin/bash

#Вызываем утилиту "sensors" и выцепляем грепом строки температуры и записываем в файлик
echo `sensors | grep temp1` > /media/nextcloud/projects/cpunotify/cpu_temp
a=`cat /media/nextcloud/projects/cpunotify/cpu_temp`

#Делаем красиво и записываем обратно в файлик )
b=${a//temp1: /}; b=${b//+/}; b=${b//°C/}; echo $b > /media/nextcloud/projects/cpunotify/cpu_temp
echo `rev /media/nextcloud/projects/cpunotify/cpu_temp | cut -c 18- | rev` > /media/nextcloud/projects/cpunotify/cpu_temp

