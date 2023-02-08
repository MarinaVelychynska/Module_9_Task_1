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
            rates[currency] = (code, bid, ask)
    return rates

@app.route("/", methods=["GET", "POST"])
def currency():
    rates = open_csv()
    result = None

    if request.method == "POST":
        code = request.form['code']
        sum = float(request.form['sum'])
        action = request.form['action']
        if code in rates:
            code, bid, ask = rates[code]
        if action == 'ask':
            result = sum * ask
        elif action == 'bid':
            result = sum * bid
        
    return render_template('currency_calculator.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
