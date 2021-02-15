import sqlite3, config
#import alpaca_trade_api as tradeapi
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")
# We'll want a dashboard route,
# Analysis Route
# Stream Lib PAge
@app.get("/")
def index(request:Request):
    print(dir(request))
    connection = sqlite3.connect("app.db")
    connection.row_factory = sqlite3.Row
    cursor=connection.cursor()
    cursor.execute(""" SELECT id,symbol,name FROM stock order by symbol """)
    rows=  cursor.fetchall()
    # This is in JSON format
    return templates.TemplateResponse("index.html", {"request": request, "stocks": rows})
    #return {"title":"Dashboard","stocks":rows}
@app.get("/stock/{symbol}")
def index(request:Request,symbol):
    connection = sqlite3.connect("app.db")
    connection.row_factory = sqlite3.Row
    cursor=connection.cursor()
    cursor.execute(""" SELECT id,symbol,name FROM stock WHERE symbol = ? """,(symbol,))
    row =  cursor.fetchone()
    # This is in JSON format
    #Let's get price data
    cursor.execute("""
            SELECT distinct Date, Open, High, Low, Close, Volume FROM stock_price where stock_id = ? ORDER BY date desc
    """,(row['id'],))
    prices = cursor.fetchall()

    return templates.TemplateResponse("stock_detail.html", {"request": request, "stock": row, "bars":prices})
