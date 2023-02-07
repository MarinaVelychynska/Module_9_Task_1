from flask import Flask, render_template, request

app = Flask(__name__)

import csv

from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def open_csv():
    rates = {}
    with open('rates.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            currency = row['currency']
            code = row['code']
            bid = float(row['bid'])
            ask = float(row['ask'])
            rates[code] = (currency, bid, ask)
    return rates

@app.route("/currency", methods=["GET", "POST"])
def currency():
    rates = open_csv()

    if request.method == "POST":
      code = request.form['code']
      sum = float(request.form['sum'])
      action = request.form['action']

    if code in rates:
     rates[code] = [code, sum, action]
    if action == "buy":
     result = sum * ask
    elif action == "sell":
     result = sum * bid
        

    return render_template("Currency_calculator.html", result=result)

   

if __name__ == '__main__':
    app.run(debug=True)
