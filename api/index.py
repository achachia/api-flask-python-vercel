from flask import Flask, render_template, jsonify,Response
import numpy as np
import pandas as pd
import yfinance as yf
import pandas_ta as ta
from datetime import datetime, timedelta
import requests


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


@app.route('/data_onchain')
def dataOnchain():
    url = "https://www.oklink.com/api/v5/explorer/blockchain/summary?chainShortName=ETH"
    payload = ""
    headers = {
        # apiKey
        'Ok-Access-Key': 'fa318372-3362-4e1b-82ef-63dc2ad468c6'
    }
    data = requests.request("GET", url, headers=headers, data=payload)
    print(data.text)
    return jsonify(data)
   
