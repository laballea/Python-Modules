import pandas

class FileLoader():
	def load(self, path):
		"""
			takes as an argument the file path of the dataset to load,
			displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
			returns the dataset loaded as a pandas.DataFrame.
		"""
		try:
			print(self, path)
			data = pandas.read_csv(path)
			print("Loading data set of dimensions {} x {}".format(data.shape[0], data.shape[1]))
			return data
		except Exception as inst:
			print(inst)
			return None
	def display(self, df:pandas.DataFrame, n):
		"""
			takes a pandas.DataFrame and an integer as arguments,
			displays the first n rows of the dataset if n is positive, or the last n rows if n is
			negative
		"""
		if (n > 0):
			print(df.head(n))
		else:
			print(df.tail(-n))

loader = FileLoader()
data = loader.load("athlete_events.csv")
loader.display(data, -12)