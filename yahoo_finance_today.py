# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import yahoo_fin.stock_info as si
from datetime import date
 
  
 
 
class take_home_ISRG:
    def __init__(self):
        
        # union all tickers
        dow = si.tickers_dow()
        nasdaq = si.tickers_nasdaq()
        other = si.tickers_other()
        sp500 = si.tickers_sp500()
        self.tickers =  set(dow+nasdaq+other+sp500)
        #get today's date
        self.today = date.today()
    
    def findTickerInfoToday(self,ticker="ISRG"):
        
        #scape ticker stock price info today
        target=si.get_data(ticker,start_date =self.today)
        
        #parsing and print the info
        print("Today "+ticker+"'s Stock Price Info:")
        print('open price: '+str(target.iloc[0]['open']))
        print('high price: '+str(target.iloc[0]['high']))
        print('low price:  '+str(target.iloc[0]['low']))
        print('close price:'+str(target.iloc[0]['close']))
        print('')
  
def notFoundMsg(ticker):
    # the ticker cannot be found by yahoo finance
    print(ticker+": No data found, symbol may be delisted\n")
    
def app():
    
    print("Initilizing the take_home application based on yahoo finance")
    print("This application is based on yahoo finance offer's python package 'yahoo_fin'")
    # explanation to not found case
    notFoundMsg("If ticker")
    
    take_home=take_home_ISRG()

    while(1):
        
        print("Type 'end' to close the take_home application",end="")
        comd=input("Please type ticker (ex:ISRG) to get info or type 'test' to test over all ticker: ")
        
        if comd=="test":
            for ticker in  list(take_home.tickers)[1:]:
                try:
                    take_home.findTickerInfoToday(ticker)
                except:
                    notFoundMsg(ticker)
                    
        elif comd=="end":
            break
                      
        elif comd in take_home.tickers:
            ticker=comd
            try:
                take_home.findTickerInfoToday(comd)
            except:
                notFoundMsg(ticker)
        else:
            print("Invid input, please try again\n")
            
if __name__ == '__main__':
    
    app()
            