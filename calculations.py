class Calculations:
	def getGeometricMean(self, nList):
		geometricMean = lambda n: reduce(lambda x,y: x*y, n) ** (1.0 / len(n))	
		return float(geometricMean(nList))
