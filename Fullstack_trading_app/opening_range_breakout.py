import sqlite3
import config
import alpaca_trade_api as tradeapi
from datetime import datetime as date

connection = sqlite3.connect('app.db')
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
    SELECT id from strategy where name = 'opening_range_breakout'
""")
# This is just to get the ID of the strategy to query
strategy_id = cursor.fetchone()['id']
#print(strategy)
cursor.execute("""
    SELECT symbol, name FROM stock
    JOIN stock_strategy ON stock_strategy.stock_id = stock.id
    where stock_Strategy.strategy_id = ?
    """, (strategy_id,))

stocks=  cursor.fetchall()
symbols = [stock['symbol'] for stock in stocks]

print(symbols)

api = tradeapi.REST(config.API_KEY,config.SECRET_KEY,config.BASE_URL)
current_date = date.today().isoformat()
start_minute_bar = f"{current_date} 09:30:00-4:00"
end_minute_bar = f"{current_date} 09:45:00-4:00"


for symbol in symbols:
    minute_bars = api.polygon.historic_agg_v2(symbol,1,'minute',_from=current_date,to =current_date).df
    opening_range_mask = (minute_bars.index >= start_minute_bar) & (minute_bars.index < end_minute_bar)
    opening_range_bars = minute_bars.loc[opening_range_mask]
    print(opening_range_bars)
    opening_range_low = opening_range_bars['low'].min()
    opening_range_high = opening_range_bars['high'].max()
    opening_range = opening_range_high - opening_range_low
    print(opening_range_low)
    print(opening_range_high)
    print(opening_range)
