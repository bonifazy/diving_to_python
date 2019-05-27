import os
import tempfile


class File:
	def __init__(self, filename):
		self.file = open(filename, 'a+')  # file descriptor
		self.file.seek(0)  # step to start of file
		self.filename = filename  # file name

	def read(self):
		data = self.file.read()
		self.file.seek(0)
		return data

	def __iter__(self):
		return self

	def __next__(self):  # iterator, return next string
		data = self.file.readline()
		if data == '':
			self.file.seek(0)
			raise StopIteration
		return data.strip('\n')

	def write(self, string):  # task: Класс должен поддерживать метод write.
		self.file.seek(0, 2)  # step to end of file
		self.file.write('\n'+string)
		self.file.seek(0)

	def __add__(self, another):  # task: Объекты типа File должны поддерживать сложение.
		data = self.read()
		with open(another.filename, 'r') as file_2:
			data = data + '\n' + file_2.read()
		new_file = File(os.path.join(tempfile.gettempdir(), '~week4_class_magic_methods.tmp'))
		new_file.write(data)

		return new_file

	def __str__(self):  # при выводе файла с помощью функции print должен печататься его полный путь, как в инициализац.
		return self.filename


if __name__ == "__main__":
	first = File('week4_magic01.txt')
	second = File('week4_magic02.txt')
	new_obj = first + second
	new_obj.write('7')

	for line in new_obj:
		print(line)

	print(first)
