# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_second = int(input('Введите количество секунд: '))

hours = str(user_second // 3600).zfill(2)
minutes = str((user_second - int(hours) * 3600) // 60).zfill(2)
seconds = str(user_second - int(hours) * 3600 - int(minutes) * 60).zfill(2)

print(f'Полученное время: {hours}:{minutes}:{seconds}')