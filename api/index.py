from flask import Flask, render_template, jsonify
import numpy as np

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
