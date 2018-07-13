a = input('Введите исходный список цифр: ')
a = list(a)
b = [i**2 for i in a]
print('новый список: ', b)