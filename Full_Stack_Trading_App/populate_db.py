import alpaca_trade_api as tradeapi
api = tradeapi.REST('yourapikeyid', 'yourapisecret', base_url='https://paper-api.alpaca.markets') # or use ENV Vars shown below
assets = api.list_assets()
for asset in assets:
    print(asset)
