import sys
import os


print(os.getcwd())

os.chdir(r"E:\Програмирование\Программирование\Python")

os.mkdir('Созданная папка')

os.chdir(r"E:\Програмирование\Программирование\Python\Созданная папка")

os.mkdir('dir_1')
os.mkdir('dir_2')
os.mkdir('dir_3')
os.mkdir('dir_4')
os.mkdir('dir_5')
os.mkdir('dir_6')
os.mkdir('dir_7')
os.mkdir('dir_8')
os.mkdir('dir_9')

print('Директории созданы :', os.listdir())


