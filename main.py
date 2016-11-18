#Super Simple Stock Market
#Created by David Carr 16/11/16
#Created using Python 2.7.12

#This main file is just to demonstrate the functionality of the simple stock market.

from stockExchange import *
stockExchange = StockExchange("Global Beverage Corporation Exchange") #Creates instance of a simple stock exchange

def main():
	
	createStockExchange() #Adds stocks to the stock exchanged
	createTrades() #Creates stock trades
	getDividendYieldOfAllStock()
	getPERatioOfAllStock()
	getWeightedStockPriceLast5Mins()
	getGBCEIndex()
	
def createStockExchange():
	stockExchange.addStockToExchange("TEA", "Common", 0.0, 0, 100, 100)
	stockExchange.addStockToExchange("POP", "Common", 8, 0, 100, 120)
	stockExchange.addStockToExchange("ALE", "Common", 23, 0, 60, 80)
	stockExchange.addStockToExchange("GIN", "Preferred", 8, 2, 100, 90)
	stockExchange.addStockToExchange("JOE", "Common", 13, 0, 250, 150)
		
def createTrades():
	stockExchange.buyStock(0, 400)
	stockExchange.buyStock(1, 300)
	stockExchange.buyStock(2, 400)
	stockExchange.buyStock(3, 800)
	stockExchange.buyStock(4, 500)
	stockExchange.buyStock(0, 700)
	stockExchange.buyStock(1, 100)
	stockExchange.buyStock(2, 400)
	stockExchange.buyStock(3, 200)
	stockExchange.buyStock(0, 300)
	stockExchange.buyStock(1, 200)
	stockExchange.buyStock(2, 200)
	stockExchange.buyStock(0, 50)
	stockExchange.buyStock(0, 370)
	
def getDividendYieldOfAllStock():
	print "*************************"
	for i in range(len(stockExchange.stocks)):
		print "The Dividend Yield for " + stockExchange.stocks[i].symbol + " is " + str(stockExchange.calcDividendYield(i))

def getPERatioOfAllStock():
	print "*************************"
	for i in range(len(stockExchange.stocks)):
		print "The P/E Ratio for " + stockExchange.stocks[i].symbol + " is " + str(stockExchange.calcPERatio(i))

def getGBCEIndex():
	print "*************************"
	print "The GBCE All Share Index is: " + str(stockExchange.calcShareIndex())
	
def getWeightedStockPriceLast5Mins():
	print "*************************"
	tradeList = stockExchange.getTradesWithinDuration(datetime.timedelta(minutes=5))

	for i in range(len(stockExchange.stocks)):
		print "Volume Weighted Stock Price based on trades in past 5 minutes for " + stockExchange.stocks[i].symbol + " is " + str(stockExchange.calcWeightedStockPrice(stockExchange.stocks[i].symbol, tradeList))
	
if __name__ == "__main__":
    main()
