import csv
import json
import requests


def get_rates():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    return data[0]['rates']

def save_rates_to_csv(rates):
    with open('rates.csv', 'w', newline='') as csvfile:
        fieldnames = ['currency', 'code', 'bid', 'ask']
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for rate in rates:          
            writer.writerow({'currency': rate["currency"], 
                              'code': rate["code"],
                              'bid': rate["bid"], 
                              'ask': rate["ask"]})

rates = get_rates()
save_rates_to_csv(rates)