from flask import Flask, render_template
from flask import request, jsonify
import json
from yahoofinancials import YahooFinancials
import requests
from bs4 import BeautifulSoup

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
	
@app.route("/plant_image", methods=["GET"])
def plant_image():
	#requested_plant = "pine tree"
	query_parameters = request.args
	requested_plant = query_parameters.get('plant')
	page_url = "https://www.bhg.com/bin/plants/?name=" + requested_plant + "&zipZone="
	page = requests.get(page_url)
	soup = BeautifulSoup(page.content, "html.parser")
	results_container = soup.find(class_ = "search-results-content-container")
	img = results_container.find("img")
	plant_photo_url = img["src"]
	return plant_photo_url

if __name__ == "__main__":
	app.run()