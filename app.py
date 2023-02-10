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

@app.route("/", methods=["GET", "POST"])
def currency():
    rates = open_csv()
    codes = rates.keys()
    result = None

    if request.method == "POST":
        code = request.form['code']
        sum = request.form['sum']

        if code in rates:
            currency, bid, ask = rates[code]
        
        calculation = float(sum) * float(ask)
        result = f"{calculation:.2f}"
        
    return render_template('currency_calculator.html', codes=codes, result=result)


if __name__ == '__main__':
    app.run(debug=True)