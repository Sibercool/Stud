_author_ = 'Одегов Денис Юрьевич'

print("Введите произвольное десятичное число(формат - ххх.ххххххх...):")
a = str(input())
print("Введите степень округления(количество знаков после точки):")
b = input()

def my_round(number, ndigits):
	number = list(number)
	ndigits = int(ndigits)
	t = '.'
	i = number.index(t) # индекс точки
	n = ndigits + i # общая длинна числа
	nd = n + 1

	if n < len(number):
		x = 0
		if int(number[nd]) >= 5: 
			nx = n - x
			unx = n - 1 - x
			while int(number[nx]) != 9: # округление 9-ки
				number[nx] = 0
				w = int(number[unx]) + 1
				number[unx] = w
				x = x + 1
		else:
		 return number
	
	#number = str(number)
	#number = int(number)
	return number[:n]


print("Число после округления:")
print(my_round(a, b))
