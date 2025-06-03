import random
import time

a = 0
b = 0
c = 0
bal = 1000
stavka = 0
zapros = 0

while True:
    print(bal,'р')
    slovo = input('Готовы начать? <да или нет>: ')
    if slovo.lower() == 'да':
        zapros = int(input('Сколько поставите?'))
        if zapros <= bal and zapros > 0:
            stavka = zapros
            bal -= stavka
            times = 0.1
            for _ in range(random.randint(11, 22)):
                a = random.randint(0, 7)
                b = random.randint(0, 7)
                c = random.randint(0, 7)
                time.sleep(times)
                times += 0.1
                print(a, b, c)
            if a == b or b == c:
                bal += stavka * 1.15
                print('Поздравляю!')
            elif a == b == c:
                bal += stavka * 50
                print('Вы выиграли! Поздравляю!')
            elif a == b == c == 7:
                bal += stavka * 1000
                print('ДЖЕКПОТ!!!')
            else:
                print('В следующий раз повезет!')

        else:
            print('Нельзя поставить больше баланса')


    elif slovo.lower() == 'нет':
        break
    else:
        print('Ошибка! Попробуйте снова!')
