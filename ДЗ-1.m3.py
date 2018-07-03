_author_ = 'Одегов Денис Юрьевич'

print('Имеем квадратное уровнение: a*x*x + b*x + c = 0')
print('Для вычисления корней введите коэффициенты')


a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

discr = (b ** 2) - (4 * a * c)

import math
Q = int(math.sqrt(discr))

if D > 0:
	X1 = (- b + Q) / (2 * a)
	X2 = (- b - Q) / (2 * a)
elif D == 0:
	X1 = - b / (2 * a)
	X2 = X1
else:
	print('Нет корней')

print('Корень Х1: ', X1)
print('Корень Х2: ', X2)
Q = input()
