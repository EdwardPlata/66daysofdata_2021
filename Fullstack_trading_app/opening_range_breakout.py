import sqlite3
import config
import alpaca_trade_api as tradeapi
from datetime import datetime as date
# Let's set up notafications when things happen: IF trades are made with this indicator being kicked
# off
import smtplib, ssl
# this is how we connect to SSL
context = ssl.create_default_context()


#######
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
#print(current_date)
start_minute_bar = f"{current_date} 09:30:00-4:00"
end_minute_bar = f"{current_date} 09:45:00-4:00"
#print(f"{date.today()}T13:30:00Z")
after = (str(current_date)[:10])
orders = api.list_orders(status='open',limit = 500, after=f"{after}T13:30:00Z")
#EMpty orders for testing purposes
#orders = api.list_orders()

existing_order_symbols = [order.symbol for order in orders]


messages = []
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

    after_opening_range_mask = minute_bars.index >= end_minute_bar # Minute bars after 9:45
    after_opening_range_bars = minute_bars.loc[after_opening_range_mask]

    print(after_opening_range_bars)

    after_opening_range_breakout = after_opening_range_bars[after_opening_range_bars['close']> opening_range_high]

    if not after_opening_range_breakout.empty:
        if symbol not in existing_order_symbols:
            print(after_opening_range_breakout)
            limit_price = after_opening_range_breakout.iloc[0]['close']
            print(limit_price)

            print(f"placing order for {symbol} at {limit_price}, closed_above {opening_range_high} \n\n {after_opening_range_breakout.iloc[0]}\n\n")
            messages.append(f"placing order for {symbol} at {limit_price}, closed_above {opening_range_high} at {after_opening_range_breakout.iloc[0]}")
            # We're gonna make a brackat order.
            api.submit_order(
                symbol=symbol,
                side='buy',
                type='limit',
                qty='100',
                time_in_force='day',
                limit_price = limit_price,
                order_class='bracket',
                take_profit=dict(
                    limit_price=limit_price + opening_range,
                ),
                stop_loss=dict(
                    stop_price=limit_price - opening_range,
                )
            )
        else:
            print(f"Already an order for {symbol}, skipping")
print(messages)
with smtplib.SMTP_SSL(config.EMAIL_HOST, config.EMAIL_PORT, context=context) as server:
    server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
    # We'll be sending an email to myself
    email_message = f"Subject: Trade Notafications for {current_date}\n\n"
    email_message += "\n".join(messages)
    server.sendmail(config.EMAIL_ADDRESS,config.EMAIL_ADDRESS,email_message)
    server.sendmail(config.EMAIL_ADDRESS, config.SMS_EMAIL_ADDRESS, email_message)
## Add phone notafication feature later.
