_author_ = 'Одегов Денис Юрьевич'

print("Введите шестизначный номер билета):")
a = input()

def Lucky_ticket(number):
	number = list(number)
	s1 = sum(number[:3])
	s2 = sum(number[3:])
	if s1 == s2:
		return true
	else:
		return false
if len(a) == 6:
	if Lucky_ticket(a) == true:
		print("Поздравляем!!! Ваш билет - счастливый))")
	else:
		print("На этот раз не повезло(( попробуйте еще раз")

Q = input()
