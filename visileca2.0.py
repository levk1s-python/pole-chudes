import random

slova = ['арбуз', 'апельсин', 'поезд', 'парогенератор', 'гидроэлектростанция', 'окно', 'поле', 'курица', 'амёба', 'инфузория', 'туфелька', 'щука', 'домик', 'барабан', 'шерлок', 'пюрешка']
r = random.randint(0,16)
vibor = input('Вы будите играть один или не один?')
if vibor.lower() == 'один':
    slovo = slova[r]
else:
    slovo = input('введите слово: ').lower()
bukvi = len(slovo)
c = ''.join(slovo)
slovo = list(slovo)
izvestnie = ['_'] * bukvi
a = ''.join(izvestnie)
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print(bukvi * '_')
popit = 6
n = 0
b = 0

while True:

    if popit < 1:
        print(f'Ты проиграл а слово было: {c}')
        break
    bukva = input().lower()
    for _ in range(bukvi):
        if bukva == slovo[n]:
            print('Правильно!')
            print('Откройте букву')
            izvestnie[n] = bukva
            b = 1
        n += 1
    a = ''.join(izvestnie)
    print(a)
    if bukva == c:
        print('Как? Ты выиграл миллион рублей!')
        break
    if b == 0:
        popit -= 1
        print('Нету такой буквы! На одну попытку меньше!')
        print(f'Попыток: {popit}')
    if izvestnie == slovo:
        print('Поздравляю пол лимона ваши!')
        break
    b = 0

    n = 0




