class Stock:
	def __init__(self, symbol, type, lastDividend, fixedDividend, parValue, price):
		self.symbol = symbol
		self.type = type
		self.lastDividend = lastDividend
		self.fixedDividend = fixedDividend 
		self.parValue = parValue
		self.price = price

	def checkStockIsValid(self, stockExchange):
		isValid = True
		
		#Check to see if stock symbol is valid by checking if symbol is left blank or not a string(full naming restrictions need specified for futher update)
		if self.symbol == "" or type(self.symbol) != str:
			return False
		
		#Check to see if stock already exists to prevent duplication
		for stock in stockExchange: 
			if self.symbol == stock.symbol:
				return False
				
		#check if stock type is valid 
		if self.type != "Common" and self.type != "Preferred":
			return False
		
		#Check to see if Last Dividend is a float or integer
		if type(self.lastDividend) != int and type(self.lastDividend) != float:
			return False
		
		#Check to see if Fixed Dividend is a float or integer
		if type(self.fixedDividend) != int and type(self.fixedDividend) != float:
			return False
			
		#Check to see if Pat Value is a float or integer
		if type(self.parValue) != int and type(self.parValue) != float:
			return False
	
		#Check to see if Pat Value is a float or integer
		if type(self.price) != int and type(self.price) != float or self.price <= 0:
			return False
		
		return True
