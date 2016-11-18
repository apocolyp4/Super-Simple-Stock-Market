from stock import *
from trade import *
from calculations import *
import time

class StockExchange:
	def __init__(self, name):
		self.name = name
		self.stocks = []
		self.stockTrades = []
		self.calc = Calculations()
		
	def addStockToExchange(self, symbol, type, lastDividend, fixedDividend, parValue, price):
		newStock = Stock(symbol, type, lastDividend, fixedDividend, parValue, price)
		isValid = newStock.checkStockIsValid(self.stocks)		
		if isValid == True:
			self.stocks.append(newStock)
		return isValid
		
	def buyStock(self, stockNumber, quantity):
		if stockNumber >= 0 and stockNumber < len(self.stocks):
			newTrade = Trade(self.stocks[stockNumber].symbol, quantity, "Buy", self.stocks[stockNumber].price)
			isValid = newTrade.checkTradeIsValid(self.stocks)
			if isValid == True:
				self.stockTrades.append(newTrade)
			return isValid
		else:
			return False

	def sellStock(self, stockNumber, quantity):
		if stockNumber >= 0 and stockNumber < len(self.stocks):
			newTrade = Trade(self.stocks[stockNumber].symbol, quantity, "Sell", self.stocks[stockNumber].price)
			isValid = newTrade.checkTradeIsValid(self.stocks)
			if isValid == True:
				self.stockTrades.append(newTrade)
			return isValid
		else:
			return False
		
	def calcWeightedStockPrice(self, stockSymbol, tradeList):
		weightedStockPrice = 0.0
		sigmaTradePriceXQuantity = 0.0
		sigmaTradeQuantity = 0.0
		
		for trade in tradeList:
			if trade.symbol == stockSymbol:
				sigmaTradePriceXQuantity += (trade.price * trade.quantity)
				sigmaTradeQuantity += trade.quantity
		
		if sigmaTradeQuantity > 0:
			weightedStockPrice = sigmaTradePriceXQuantity / sigmaTradeQuantity
			
		return weightedStockPrice
				
	def calcDividendYield(self, stockNumber):
		dividendYield = 0.0
		
		if stockNumber >= 0 and stockNumber < len(self.stocks):
			if self.stocks[stockNumber].type == "Common":
				dividendYield = self.stocks[stockNumber].lastDividend / float(self.stocks[stockNumber].price)
			elif self.stocks[stockNumber].type == "Preferred":
				dividendYield = (self.stocks[stockNumber].fixedDividend * self.stocks[stockNumber].parValue) / float(self.stocks[stockNumber].price)
		return dividendYield
			
	def calcPERatio(self, stockNumber):
		peRatio = 0.0
		dividendYield = self.calcDividendYield(stockNumber)
		if dividendYield > 0:
			peRatio = float(self.stocks[stockNumber].price) / dividendYield
		
		return peRatio
		
	def getTradesWithinDuration(self, duration):
		tradeList = []
		minTradeDateTime = datetime.datetime.now() - duration
		for trade in self.stockTrades:
			tradeTimeDelta = trade.timeStamp - minTradeDateTime
			if tradeTimeDelta <= duration:
				tradeList.append(trade)
		return tradeList
		
	
	def calcShareIndex(self):
		shareIndex = 0.0
		weightedStockPriceList = []
		for stock in self.stocks:
			weightedStockPriceList.append(self.calcWeightedStockPrice(stock.symbol, self.stockTrades))
			
		shareIndex = self.calc.getGeometricMean(weightedStockPriceList)

		return shareIndex

