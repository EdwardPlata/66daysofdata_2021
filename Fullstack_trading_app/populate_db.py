import alpaca_trade_api as tradeapi
import sqlite3
connection=sqlite3.connect('/User/anthonyplata/Google\ Drive/Projects/Fullstack_trading_app/app.db')
print("Successfully connected to Database")
cursor = connection.cursor()
#----------- Scheduler job-----------
cursor.execute("""
    SELECT symbol, company FROM stock
""")
rows = cursor.fetchall()

symbols = [row[0] for row in rows] # list comprehension
#print(symbols)
# Connecting to alpaca_trade_api
api = tradeapi.REST('PKHITD3S928PZ8XAHLX6','goptGCIpXs40d5tQtFFp6KO3MXFRnSTv46snc6C8','https://paper-api.alpaca.markets')

assets = api.list_assets()
##Asset object example
# Asset({   'class': 'us_equity',
#     'easy_to_borrow': False,
#     'exchange': 'NYSE',
#     'id': '53f4d07f-dfcc-48d5-bb73-d8a4bab76a10',
#     'marginable': True,
#     'name': 'Nokia Corporation',
#     'shortable': False,
#     'status': 'active',
#     'symbol': 'NOK',
#     'tradable': True})


for asset in assets:
    #print(asset.name)
    #cursor.execute("Insert into stock (symbol,company) VALUES (?,?)",(asset.symbol,asset.name
    # Are there new stocks available? This should be ran daily to catch any new IPOs
    try:
        if asset.status == 'active' and asset.tradable and asset.symbol not in symbols:
            print(f"Added a new stock {asset.symbol} {asset.name}")
            cursor.execute("Insert into stock (symbol,company) Values (?,?)",(asset.symbol,asset.name))
    except Exception as e:
        print(e)
        print(asset.symbol)
connection.commit()
