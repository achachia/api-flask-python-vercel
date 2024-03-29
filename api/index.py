from flask import Flask, render_template, jsonify,Response, request
import numpy as np
import pandas as pd
import yfinance as yf
import pandas_ta as ta
from datetime import datetime, timedelta
import requests

key_api_oklink = 'fa318372-3362-4e1b-82ef-63dc2ad468c6'

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world'

@app.route('/json')
def json():
    dictionnaire = {
        'type': 'Prévision de température',
        'valeurs': [24, 24, 25, 26, 27, 28],
        'unite': "degrés Celcius"
    }
    return jsonify(dictionnaire)

@app.route('/numpy')
def numpy():
    return str(np.random.choice([1, 2, 3, 4, 5, 6]))

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/data_yfinance')
def data():
    # Define the stock symbol and timeframe
    symbol = 'ICP-USD'
    end_date = datetime.today()
    start_date = end_date - timedelta(days=120)  # 4 months   
    stock_data = yf.download(symbol, start=start_date,end=end_date)
    #print(stock_data)
    return Response(stock_data.to_json(orient="records"), mimetype='application/json')


@app.route('/data_onchain_oklink')
def dataOnchain():
    # GET /api/v5/explorer/blockchain/info?chainShortName=btc
    #  https://api-flask-python-vercel.vercel.app/data_onchain_oklink?sectionApi=blockchain&typeApi=summary   --->  /api/v5/explorer/blockchain/summary
    #  https://api-flask-python-vercel.vercel.app/data_onchain_oklink?sectionApi=blockchain&typeApi=info&chainShortName=btc  -->  /api/v5/explorer/blockchain/info?chainShortName=btc
    url = "https://www.oklink.com/api/v5/explorer/"
    _sectionApi  = request.args.get('sectionApi') # exemple blockchain
    _typeApi  = request.args.get('typeApi') # exemple info
    url +=  _sectionApi + "/"+ _typeApi
    compteur = 0
    _chainShortName  = request.args.get('chainShortName')
    if _chainShortName is not None:
      compteur = compteur +1
      if compteur > 1 :  
         url +=  "&chainShortName=" + _chainShortName
      else :    
         url +=  "?chainShortName=" + _chainShortName

    
    payload = ""
    headers = {
        # apiKey
        'Ok-Access-Key': key_api_oklink
    }
    data = requests.request("GET", url, headers=headers, data=payload)
    response_json = data.json()
    return response_json
   
