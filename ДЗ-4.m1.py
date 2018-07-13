import random

file = open('1.txt', 'w')
numbers = '0123456789'
a = ''.join(random.choice(numbers) for _ in range(2500))
print(a)
file.write(a)
i = 0
m = 0
x = 0
while i < (len(a) - 1):
	n = 1
	if a[i] == a[(i + 1)]:
		n = n + 1
		i = i + 1
		if n > m:
			m = n 
			x = a[i]

	i = i + 1

print('максимадьная последовательность одинаковых чисел -', m, 'чисел', x)

file.colse()

