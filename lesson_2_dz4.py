# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_str = list(input('Введите предложение из более 2 слов: ').split())
count = 0

for i in user_str:
    count += 1
    print(f'{count}. {i[:10]}')