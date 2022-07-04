import datetime as dt

from typing import Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI,Path,Query,HTTPException,status
from typing import Optional
from pydantic import BaseModel


#print(type(app))
#print(app) output-><fastapi.applications.FastAPI object at 0x0000024BA6F36F10>
#What is endpoints-->it is the point of entry in a communacation channel when two systems are interacting
#for ex-->/hello or /get-items in our case it will be localhost/hello
#-->HTTP methods-->GET-->POST-->PUT(update)-->DELETE
app=FastAPI()
class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")

    price: float = Field(description="The price of the Trade.")

    quantity: int = Field(description="The amount of units traded.")


class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")

    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")

    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")

    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")

    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")

    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")

    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")

    trader: str = Field(description="The name of the Trader")

myTrades={
    1:{"trade_id":1,
       "trader":"bob smith",
       "trade_details":"Regarding sports",
       "trade_date_time":3/4/2021,
       "instrument_name":"Ball",
       "instrument_id":3,
       "counterparty":"%",
       "asset_class":"Bond",
       "quantity":10,
       "price":400,
       "buysellIndicator":4000
       },
    2:{"trade_id":2,
       "trader":"smith",
       "trade_details":"Regarding education",
       "trade_date_time":5/4/2021,
       "instrument_name":"pen",
       "instrument_id":2,
       "counterparty":"/",
       "asset_class":"Equity",
       "quantity":190,
       "price":10,
       "buysellIndicator":4000
       },
    3:{"trade_id":3,
       "trader":"John",
       "trade_details":"Regarding education",
       "trade_date_time":6/4/2021,
       "instrument_name":"Books",
       "instrument_id":4,
       "counterparty":"%",
       "asset_class":"Equity",
       "quantity":1000,
       "price":50,
       "buysellIndicator":5000
       },
}
#In this assignment I have taken a Dictionary because I am not able to find a dataset on elasticseach
#Still I am searching for it but for this, I have taken the default Dictionary.
#Listing trades-->In this first question they asked to return a list of trades so
# I return all my Trades as it is.
@app.get("/fetch-all/")
def fetch_all():
    return myTrades

#Single trade
#Users would like to be able to retrieve a single trade from the API. Please provide an endpoint to fetch a trade by id.
@app.get("/single-trade/{trade_id}")
def single_trade(trade_id:int =Path(None,description="The ID of of the trade which you would like to view")):
    if trade_id not in myTrades:
        return "Trade_id dese not exists"
    return myTrades[trade_id]
#Searching Trade

@app.get("/Searching/{instrument_name}{counterparty}{instrument_id}{trader}")
def search(instrument_name:str,counterparty:str,instrument_id:int,trader:str):
    if(myTrades[instrument_name]==instrument_name and myTrades[counterparty]==counterparty and myTrades[instrument_id]==instrument_id and myTrades[trader]==trader):
       return myTrades
    else:
        return {"msg":"Not founnd"}
       #trader={trade_id:trade_id,"instrument_name":instrument_name,"counterparty":counterparty,instrument_id:instrument_id,"trade":trader}
    #return trader
#Advamnced Filtering

@app.post("/Advanced/{minPrice}/{maxPrice}")
def create_item(maxPrice:int=Path(None,description="Between max and min",GT=10,LT=2)):
    return MaxPrice

#create we can add new row 
@app.post("/create/{trader_id}")
def create(trade_id:int,trade:Trade):
    if trade_id in myTrades:
        raise HTTPException(status_code=400,detail="trade id Already Exists")
    myTrades[trade_id]=trade
    return  myTrades[trade_id]





