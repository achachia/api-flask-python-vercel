from flask import Flask, render_template
import numpy as np

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world'


@app.route('/test')
def test():
    return str(np.random.choice([1, 2, 3, 4, 5, 6]))

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
