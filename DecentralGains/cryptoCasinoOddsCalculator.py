import cryptocompare
import time
import os

cryptocompare.cryptocompare._set_api_key_parameter("Crypto_Compare_API_Key_Here")

currencies = []
prices = []
ratesRoulette = []
ratesBj = []

def setRates(currencies, rouletteAry, bjAry):
    fRates = open("rates.txt","r")
    fRates.readline()
    i=0
    for line in fRates.readlines():
        lineSplit=line.split(":")
        currencies.append(lineSplit[0])
        rouletteAry.append(float(lineSplit[1]))
        bjAry.append(float(lineSplit[2]))
        i+=1
        

def getPrices(prices, currencies):
    i=0
    for crypto in currencies:
        prices.append((cryptocompare.get_price(crypto, currency='USD', full=False))[crypto]["USD"])
        i+=1
    prices.append((cryptocompare.get_price("DG", currency='USD', full=False))["DG"]["USD"])

def printPrices(currencies, prices):
    print(f"DG  {prices[-1]}\t",end='')
    for i in range(len(currencies)):
        print(f"{currencies[i]}  {prices[i]}\t",end='')
    print('\n')
        

def priceToRate(dgPrice, coinPrice, ratio):
    rate = 100*(dgPrice/(ratio*coinPrice))
    return rate

    
def trueOdds(rate, game=0, bonus=0):
    multiplier = 1+(bonus/10)
    if (game==0):
        odds=-2.70
    elif (game==1):
        odds=-0.73
        
    #if (game==0):
        #rouletteOdds = 100-2.70
        #return (1+((multiplier*rate)/100))*rouletteOdds

    ourOdds =(multiplier*rate)
    return (100+odds+ourOdds)


setRates(currencies, ratesRoulette, ratesBj)
getPrices(prices, currencies)


while (0==0):
    print (time.asctime(time.localtime(time.time())))
    printPrices(currencies, prices)
    for i in range(len(currencies)):
        print(f"{currencies[i]}")
        print("\tRoulette Odds")
        print(f"\tNo Bonus:\t{round(trueOdds(priceToRate(prices[-1], prices[i], ratesRoulette[i])  , bonus=0),3)}")
        print(f"\t30% Bonus:\t{round(trueOdds(priceToRate(prices[-1], prices[i], ratesRoulette[i])  , bonus=3),3)}")
        print(f"\t60% Bonus:\t{round(trueOdds(priceToRate(prices[-1], prices[i], ratesRoulette[i])  , bonus=6),3)}")
        print("\n")
        print(f"\tBlackjack Odds")
        print(f"\tNo Bonus:\t{round(trueOdds(priceToRate(prices[-1], prices[i], ratesBj[i]),game=1 , bonus=0),3)}")
        print(f"\t30% Bonus:\t{round(trueOdds(priceToRate(prices[-1], prices[i], ratesBj[i]) ,game=1 , bonus=3),3)}")
        print(f"\t60% Bonus:\t{round(trueOdds(priceToRate(prices[-1], prices[i], ratesBj[i]), game=1, bonus=6),3)}")
        print("\n")


    goodGames=False
    for i in range(len(currencies)):
        for j in range(0,7):
            if (  trueOdds(priceToRate(prices[-1], prices[i], ratesRoulette[i]),bonus=j )>100  ):
                print(f"Play Roulette with {currencies[i]} and minimum {j*10}% DG Bonus")
                goodGames=True
                break
            
    for i in range(len(currencies)):
        for j in range(0,7):
            if (  trueOdds(priceToRate(prices[-1], prices[i], ratesBj[i]),game=1, bonus=j )>100  ):
                print(f"Play Blackjack with {currencies[i]} and minimum {j*10}% DG Bonus")
                goodGames=True
                break

    if (not goodGames):
        print("Stay away from the tables today!")

    time.sleep(290)
    getPrices(prices, currencies)
    time.sleep(10)
    os.system('cls' if os.name=='nt' else 'clear')
