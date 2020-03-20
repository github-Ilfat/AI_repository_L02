#Задачи на циклы и оператор условия------
#----------------------------------------

'''
*******************************************************************************************
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
'''
print('Данный скрипт выводит на экран циклом пять пронумерованных строк из нулей.')
for i in range(1,6,1): print(i,') ', 0, sep='')
'''
'''
*******************************************************************************************
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
'''

def is_digit(string):
    flag_ok = 0
    if string.isdigit():
        if len(string)==1 and (int(string) >=0 and int(string) <= 10): return True
    else:
        return False
five = 0
err = 0
i = 0
print('Данный скрипт подсчитывает количество цифр 5, введённых пользователем в цикле 10 цифр.')
print('Прошу 10 раз, поочерёдно ввести любую цифру от 0 до 9.')
while i < 10:
    i = i + 1 - err
    print('введите цифру N', i, sep = '', end = ' ')
    user_digital = input(':')
    if is_digit(user_digital):
        user_digital = int(user_digital)
        if user_digital == 5: five = five + 1
        if i == 10: print(five)
        err = 0
    else:
        err = 1
        print('Это не цифра алфавита десятичной системы счисления!')
    continue
'''

'''
*******************************************************************************************
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
'''
print('Данный скрипт подсчитывает сумму ряда чисел от 1 до 100 и выводит результат на экран.')
sum = 0
for i in range(1,101): sum += i
print(sum)
'''

'''
*******************************************************************************************
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
'''
print('Данный скрипт подсчитывает произведение ряда чисел от 1 до 10 и выводит результат на экран.')
proizv = 1
for i in range(1,11): proizv = proizv * i
print(proizv)
'''

'''
*******************************************************************************************
Задача 5
Вывести цифры числа на каждой строчке.
'''
'''
print('Данный скрипт выводит цифры числа на каждой строчке начиная справа-налево.')
integer_number = 2129
#print(integer_number%10,integer_number//10)
while integer_number > 0:
    print(integer_number % 10)
    integer_number = integer_number // 10
'''
'''
print('Данный скрипт выводит цифры числа на каждой строчке начиная слева-направо.')
integer_number = 2129
ostatok_number=integer_number%1000
cifra_number=integer_number//1000
#print(ostatok_number,cifra_number)
k = 1000
ostatok_number=integer_number
while ostatok_number > 0:
    cifra_number=int(ostatok_number//k)
    ostatok_number=ostatok_number%k
    k = k / 10
    print(cifra_number)
'''

'''
*******************************************************************************************
Задача 6
Найти сумму цифр числа.
'''
'''
print('Данный скрипт определяет сумму цифр числа.')
integer_number = 2129
#ostatok_number=integer_number%1000
#cifra_number=integer_number//1000
print('число:', integer_number)
print('Cумма цифр числа равна:')
k = 1000
sum = 0
ostatok_number=integer_number
while ostatok_number > 0:
    cifra_number = int(ostatok_number // k)
    if ostatok_number > 10: print(cifra_number, end = ' + ')
    if ostatok_number < 10: print(cifra_number, end = ' = ')
    sum = sum + int(cifra_number)
    ostatok_number = ostatok_number % k
    k = k / 10
    if ostatok_number == 0: print(sum)
'''

'''
*******************************************************************************************
Задача 7
Найти произведение цифр числа.
'''
'''
print('Данный скрипт определяет сумму цифр числа.')
integer_number = 2129
#ostatok_number=integer_number%1000
#cifra_number=integer_number//1000
print('число:', integer_number)
print('Cумма цифр числа равна:')
k = 1000
sum = 1
ostatok_number=integer_number
while ostatok_number > 0:
    cifra_number = int(ostatok_number // k)
    if ostatok_number > 10: print(cifra_number, end = ' + ')
    if ostatok_number < 10: print(cifra_number, end = ' = ')
    sum = sum * int(cifra_number)
    ostatok_number = ostatok_number % k
    k = k / 10
    if ostatok_number == 0: print(sum)
'''

'''
*******************************************************************************************
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
'''
print('Данный скрипт определяет: есть ли среди цифр числа 5.')
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
'''

'''
*******************************************************************************************
Задача 9
Найти максимальную цифру в числе
'''
'''
print('Данный скрипт определяет: максимальную цифру в числе.')
integer_number = 213413
print('исследуемое число: ', integer_number)
max = 0
while integer_number>0:
    if integer_number%10 > max: max = integer_number%10
    integer_number = integer_number//10
    if integer_number == 0:  print('максимальная цифра в числе = ', max)
'''

'''
*******************************************************************************************
Задача 10
Найти количество цифр 5 в числе
'''
'''
print('Данный скрипт определяет количество цифр 5 в числе.')
integer_number = 2535154345
print('исследуемое число: ', integer_number)
n5=0
while integer_number>0:
    if integer_number%10 == 5: n5+=1
    integer_number = integer_number//10
    if integer_number == 0:  print('количество цифр 5 в числе = ', n5)
'''