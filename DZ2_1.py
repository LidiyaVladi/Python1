'''
1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
Пример:
67.82 -> 23
0.56 -> 11
'''
while True:
    num = input('Введите число ')
    try:
        n = float(num) 
        break
    except:
        if num.isalpha():
            print("Введены буквы")
        else:
            print("Введены непонятные символа")

stroka = list(num)

sum = 0
i = 0
col = len(stroka)

while i < col:
    if stroka[i] == '-':                
        ''' проверка на минус'''
        stroka[1] = int(stroka[1])*(-1)
        i+=1
    else:
        if stroka[i] != '.':
            ''' проверка на точку'''
            sum+=int(stroka[i])
            i+=1
        else: i+=1
print(f'Сумма элементов числа {num} = {sum}')

# -------------------------------------
'''
2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
Не используйте функцию math.factorial.
Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''
while True:
    n = input('Введите число ')
    try:
        n = int(n) 
        break
    except:
        if n.isalpha():
            print("Введены буквы")
        else:
            print("Введены непонятные символа")

faktorial = []
i = 1
element_faktorial = 1
while i <= n:
    element_faktorial*= i
    faktorial.append(element_faktorial)
    i+=1
print(f' Факториал числа {n} -> {faktorial}')

# -------------------------------------
'''
3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
Это происходит до тех пор, пока не будет найден палиндром.
Напишите такую программу, которая найдет палиндром введенного пользователем числа.
'''
while True:
    num = input('Введите число ')
    try:
        n = int(num) 
        break
    except:
        if num.isalpha():
            print("Введены буквы")
        else:
            print("Введены непонятные символа")

def inverted_num(a):  
    '''
    Функция перевнутого числа
    '''
    num_inverted = 0
    num_original = int(a)
    while num_original != 0:
        num_inverted = num_inverted*10 + (num_original%10)
        num_original//= 10
        
    return num_inverted

sum = inverted_num(n)

while inverted_num(n) != n:
    sum+= n
    n = sum
   
print(f'Число {n} - является палиндромом числа {num}')

'''
4 - Реализуйте выдачу случайного числа
не использовать random.randint и вообще библиотеку random
Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
Учтите, что есть диапазон: от(минимальное) и до (максимальное)
'''
min_interval = int(input('Введите интервал от: '))
max_interval = int(input('Введите интервал до: '))

if min_interval > max_interval:
    а = min_interval
    min_interval = max_interval
    max_interval = а
elif min_interval == max_interval: 
    print('Вы не задали интервал')

razniza = max_interval - min_interval

from re import A
import time 
milliseconds = str(round(time.time () * 1000))

srez = milliseconds[10:12]

while razniza < int(srez):
    a = int(srez)/5
    srez = a

rezul = min_interval + int(srez)

while rezul > max_interval: 
    rezul - max_interval

print(f'Случайное число: {rezul}')