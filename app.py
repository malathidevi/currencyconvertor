from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    data = requests.get(url).json()
    rates = data['rates']

    if from_currency != 'USD':
        amount = amount / rates[from_currency]

    converted_amount = round(amount * rates[to_currency], 4)

    return render_template('index.html', converted_amount=converted_amount)

if __name__ == '__main__':
   app.run()