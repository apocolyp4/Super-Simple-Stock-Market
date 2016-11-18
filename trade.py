import datetime

class Trade:
	def __init__(self, symbol, quantity, buyOrSell, price):
		self.symbol = symbol
		self.quantity = quantity
		self.buyOrSell = buyOrSell
		self.price = price
		self.timeStamp = datetime.datetime.now()
		
	def checkTradeIsValid(self, stockExchange):
		#check if stock is valid
		isValid = False
		for stock in stockExchange: 
			if self.symbol == stock.symbol:
				isValid = True
				
		if isValid == True:
			#Check if quantity is an integer and is greater than 0
			if type(self.quantity) != int or self.quantity < 1:
				return False
			#Check if type of trade is either buy or sell
			if self.buyOrSell != "Buy" and self.buyOrSell != "Sell":
				return False
		else:
			return False
			
		return True
