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
	yf = YahooFinancials(req['stocks'])

	stock_data = yf.get_historical_price_data(req['start_date'], req['end_date'], "daily")
	return jsonify(stock_data)

if __name__ == "__main__":
	app.run()