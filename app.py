 #!/usr/bin/env python 
# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, abort, render_template, request, jsonify, Response 
import json
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('home.html')

@app.route('/download',methods=['GET', 'POST'])
def download():
	try:
		url = request.form.get('urltodownload')
		print(url)
		soup = BeautifulSoup(requests.get(url).content, 'html.parser')
		data = json.loads(soup.video['data-sources'])
		return render_template('download.html',source=data[0]['src'])
	except:
		return 'error'
		
	
   
if __name__ == '__main__':
	app.run(debug=False)

