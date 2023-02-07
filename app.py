
import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

from flask import Flask, render_template, request

app = Flask(__name__)

import csv

with open('rates.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
 
    currency_list = [code, ask, bid]

@app.route("/currency", methods=["GET", "POST"])
def currency():
  if request.method == "POST":
      data = request.form
      sum = data.get('sum')
      code = data.get('code') 
  
  for i in currency_list:
    
    if i == ask:
      return  sum * ask
    if i == bid:
      return sum * bid


  return render_template("Currency_calculator.html")

if __name__ == '__main__':
    app.run(debug=True)