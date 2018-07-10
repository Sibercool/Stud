_author_ = 'Одегов Денис Юрьевич'

print("Напишите номера элементов ограничивающих область в ряду Фибоначчи")
print("n - min элемент: ")
a = int(input())
print("m - max элемент: ")
b = int(input())

def fibonacci(n, m):
	fibo = [1, 1, 2, 3, 5, 8, 13]# работает
	x = 6
	while x > m:
		x1 = int(x - 1) 
		x2 = int(x - 2)
		y = int(fibo[x1] + fibo[x2])
		fibo.append(y)# работает
		x = x + 1
	return fibo[n:(m + 1)]

print("Ваш фрагмент ряда Фибоначчи:", fibonacci(a, b))
