import sys
import os


os.chdir(r"E:\Програмирование\Программирование\Python\Созданная папка")

os.rmdir('dir_1')
os.rmdir('dir_2')
os.rmdir('dir_3')
os.rmdir('dir_4')
os.rmdir('dir_5')
os.rmdir('dir_6')
os.rmdir('dir_7')
os.rmdir('dir_8')
os.rmdir('dir_9')



os.chdir(r"E:\Програмирование\Программирование\Python")

os.rmdir("E:\Програмирование\Программирование\Python\Созданная папка")

print('Директории удалены', os.listdir())