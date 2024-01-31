#Модуль 1. Часть 2. Уровень 1.
a,b,c = map(int,input('Введи три целых числа:').split())
if a==b and a==c:
    print('Три числа совпадает')
elif (a==b and a!=c)or(a!=b and a==c):
    print('Два числа совпадает')
elif b==c:
    print('Два числа совпадает')
else:
    print('Ни одно число не совпадает')
