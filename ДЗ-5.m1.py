import shutil
import os

#Смена директории
print('Введите адрес папки для работы')
adres = input()
os.chdir(r"adres")

while vibor == 5:
	print('Выберите действие: \n 1.Посмотреть содержимое папки \n 2.Создать новую папку \n 3.Удалить папку \n 4.Перейти в другую папку \n 5.Выход')
	vibor = input()
	if vibor == 1:
			print('Вот что у нас тут:', os.listdir('adres'))
		elif vibor == 2:
			print('Введите имя новой папки')
			new_dir = input()
			try:
				os.mkdir('new_dir')
				print('Новая папка успешно создана:', os.listdir('adres'))
			except FileExistsError:
				print('Кто-то уже создал эту папку до Вас')
		elif vibor == 3:
			print('Введите имя папки, которую необходимо удалить')
			del_dir = input()
			os.rmdir('del_dir')
			print('Папка успешно удалена:', os.listdir('adres'))#Нужно дописать защиту от неверного адреса
		elif vibor == 4:
			print('Введите имя папки, в которую необходимо перейти')
			new_adres = input()
			os.chdir(r"new_adres")
			print('Вот что у нас тут:', os.listdir('new_adres'))
		elif vibor != 1 or vibor != 2 or vibor != 3 or vibor != 4:
			print('Введите номер действия из списка')





#os.chdir(r"E:\Програмирование\Программирование\Python")

#shutil.copy(r'ДЗ-5.e3.py',r'copy_ДЗ-5.e3.py')
#print('Копирование завершено')