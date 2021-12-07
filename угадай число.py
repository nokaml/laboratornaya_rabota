import random
popit = 0 # Число попыток
number = random.randint(1, 10) # Число от 1 до 50
print ('Угадай число от 1 до 10!')
while popit < 3: # Число разрешенных попыток - 3
    chislo = int(input('Введи число: '))
    popit += 1
    if chislo < number:
        print ('Твое число меньше того, что я загадал.')
    if chislo > number:
        print ('Твое число больше загаданного мной.')
    if chislo == number:
        break

if chislo == number:
    print ('Правильно, молодец!')
else:
    print ('Неправильно, попробуй ещё раз!')