from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
import requests
app = Flask (__name__)

@app.route("/count-wiki-table")
def root():
	data = request.args
	resp = requests.get(data["url"])
	soup = BeautifulSoup(resp.content, 'lxml')
	table = soup.find("table")
	rows = table.find_all("tr")

	return jsonify({"line": len(rows)})


