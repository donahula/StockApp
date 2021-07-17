from flask import Flask, render_template
from flask import request, jsonify
import json
from yahoofinancials import YahooFinancials

app = Flask(__name__)

@app.route("/")
def index():
	f = open('nasdaq_100_stock_list.json',)
	stock_list = json.load(f)

	return render_template("index.html", stocks=stock_list)

@app.route("/data_query", methods=["POST"])
def data_query():
	req = request.get_json()
	
	yf = YahooFinancials(req)
	stock_data = yf.get_historical_price_data("2021-07-09", "2021-07-16", "daily")
	print(json.dumps(stock_data, indent = 4))
	#test_data = [{'name': 'APPL', 'data': [43.34, 52.03, 57.77, 39.65]}, {'name': 'MSFT', 'data': [24.16, 40.64, 29.42, 36.54]}, {'name': 'AMZN', 'data': [117.44, 177.22, 160.05, 197.71]}]
	
	
	
	return jsonify(stock_data)

if __name__ == "__main__":
	app.run()