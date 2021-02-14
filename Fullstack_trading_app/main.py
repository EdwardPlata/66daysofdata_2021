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
