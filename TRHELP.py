from tradingview_ta import TA_Handler, Exchange, Interval

eth = TA_Handler(
    symbol='ETHUSD',
    screener='crypto',
    exchange='BITSTAMP',
    interval=Interval.INTERVAL_1_MINUTE
)

while True:
    if (eth.get_analysis().indicators['RSI'] > 50):
        print(round((eth.get_analysis().indicators['RSI'] - 50) * 5), "% sell", end="\r")
        #if (round((eth.get_analysis().indicators['RSI'] - 50) * 5) >= 75):
            #print("strong sell", end="\t")
        #elif (round((eth.get_analysis().indicators['RSI'] - 50) * 5) >= 50):
            #print("sell", end="\t")
        #elif (round((eth.get_analysis().indicators['RSI'] - 50) * 5) < 50):
            #print("weak sell", end="\t")
    elif (eth.get_analysis().indicators['RSI'] < 50):
        print(round((50 - eth.get_analysis().indicators['RSI']) * 5), "% buy", end="\r")
        #if (round((50 - eth.get_analysis().indicators['RSI']) * 5) >= 75):
            #print("strong buy", end="\t")
        #elif (round((50 - eth.get_analysis().indicators['RSI']) * 5) >= 50):
            #print("buy", end="\t")
        #elif (round((50 - eth.get_analysis().indicators['RSI']) * 5) < 50):
            #print("buy", end="\t")
            
    
        