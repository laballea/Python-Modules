from array import array
import math


class TinyStatistician():
	def __init__(self):
		pass
	
	def sum(self, x):
		sum = 0
		for el in x:
			sum += el
		return float(sum)

	def mean(self, x):
		"""
			computes the mean of a given non-empty list or array x, using a for-loop.
			The method returns the mean as a float, otherwise None if x is an empty list or
			array.
		"""
		mean = 0
		for el in x:
			mean += el
		return float(mean / len(x))

	def median(self, x):
		"""
			computes the median of a given non-empty list or array x. The method
			returns the median as a float
		"""
		x.sort()
		if (len(x) % 2 == 1):
			return float(x[int((len(x) + 1) / 2 - 1)])
		else:
			return float((x[int(len(x) / 2)] + x[int(len(x) / 2 - 1)]) / 2)

	def quartile(self, x):
		"""
			computes the 1st and 3rd quartiles of a given non-empty array x.
			The method returns the quartile as a float
		"""
		x.sort()
		return[float(x[int((len(x) + 3) / 4) - 1]), float(x[int((3 * len(x) + 1) / 4) - 1])]

	def var(self, x):
		"""
			computes the variance of a given non-empty list or array x, using a for-
			loop. The method returns the variance as a float
		"""
		var = 0
		sum = self.sum(x)
		for el in x:
			var += (el - (1/len(x)*sum))**2
		return var / len(x)

	def std(self, x):
		"""
			computes the standard deviation of a given non-empty list or array x,
			using a for-loop. The method returns the standard deviation as a float,
		"""
		return math.sqrt(self.var(x))

tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(tstat.mean(a))
# Expected result: 82.4
print(tstat.median(a))
# Expected result: 42.0
print(tstat.quartile(a))
# Expected result: [10.0, 59.0]
print(tstat.var(a))
# Expected result: 12279.439999999999
print(tstat.std(a))
# Expected result: 110.8126346586886