from flask import Flask, render_template
from yahoo_finance import Share
import json


app = Flask(__name__)

@app.route("/")
def index():
	f = open('nasdaq_100_stock_list.json',)
	stock_list = json.load(f)

	return render_template("index.html", stocks=stock_list)
	
if __name__ == "__main__":
	app.run()