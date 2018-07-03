_author_ = 'Одегов Денис Юрьевич'

x = int(input('Введите произвольное целое число '))
n = int(x)

max_digit = 0

while (x % 10) >= 1:
   digit = x % 10
   x //= 10
   if digit > max_digit:
   	  max_digit = digit

print('Максимальная цифра в числе ', n, ' - ', max_digit)

Q = input()
