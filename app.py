from flask import Flask, render_template
from yahoo_finance import Share
import json
from flask import request
import yfinance as yf
from alpha_vantage.timeseries import TimeSeries

ALPHA_VANTAGE_API_KEY = 'TTZ38CINRJYC1KGO' 

app = Flask(__name__)

@app.route("/")
def index():
	f = open('nasdaq_100_stock_list.json',)
	stock_list = json.load(f)

	return render_template("index.html", stocks=stock_list)

@app.route("/data_query", methods=["POST"])
def data_query():
	req = request.get_json()
	
	ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='json')
	print(help(ts))
	#testing = ts.get_daily_adjusted('AAPL', outputsize='compact')
	print(testing)
	
	#for i in req:
#		print(i)
		#print(yf.download(i,'2018-01-01','2018-01-04'))
	
	
	
	return "test"

if __name__ == "__main__":
	app.run()