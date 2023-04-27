import os		
import pandas as pd

# удаляем файлы со словом РПД и формата .doc 
path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_к_16.02.23_2в'
filelist = []
counter = 0

for root, dirs, files in os.walk(path):
	for file in files:
		# counter += 1
		# print(counter, file)
		if file.endswith('.doc'):
			print(file)
			
		
				