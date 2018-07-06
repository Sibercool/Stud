_author_ = 'Одегов Денис Юрьевич'

a = list(input('Введите список №1: '))
b = list(input('Введите список №2: '))

print('№1 = ', a)
print('№2 = ', b)

i = 0
n = 0

while n < len(a):
	  while i < len(b):
	 	if int(a[n]) == int(b[i]):
	 		a.remove(n)
	 		i = i + 1
n = n + 1	

print('Список№1 - Список№2 = ', a)

Q = input()
