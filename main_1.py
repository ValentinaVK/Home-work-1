#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration

duration = int(input( 'Введите количество секунд:  '))
day = duration // 86400
hour = (duration - day * 86400) // 3600
minute = (duration - hour * 3600 - day * 86400) // 60
second = (duration - minute * 60) % 60
print(day, 'дней' , hour , 'час', minute, 'минута', second, 'секунда')




