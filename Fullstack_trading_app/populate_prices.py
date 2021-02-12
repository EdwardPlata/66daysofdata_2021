import config
import alpaca_trade_api as tradeapi
api = tradeapi.REST(config.API_KEY,config.SECRET_KEY,config.BASE_URL)

#barsets = api.get_barset(['AAPL','MSFT'],'day')
barsets = api.get_barset('Z','minute')
print(barsets)

for symbol in barsets:
    print(f"processing symbol {symbol}")

    for bar in barsets[symbol]:
        print(bar.t,bar.o,bar.h,bar.l,bar.c,bar.v)
