class FileReader:

	def __init__(self, filename):
		self.filename = filename

	def read(self):
		try:
			f = open(self.filename)
			solution_str = ''
			for line in f.read().strip():
				solution_str += line.strip('\n')  # print to one string without whitespaces
			return solution_str
		except IOError:
			return ""


if __name__ == "__main__":
	reader = FileReader('to_json.txt')
	print(reader.read())
