from flask import Flask, render_template, request
from flask_script import Manager
from retrieveData import retriveStockData
import pandas as pd
import plotly
from plotly import figure_factory as FF
from plotly.graph_objs import *
import plotly.graph_objs as go
from database import *

# Set up application
app = Flask(__name__)

manager = Manager(app)

@app.route('/')
def index():
	conn, cur = get_connection_and_cursor()
	cur.execute("""select name from StockList""")
	stocks = cur.fetchall()
	return render_template('index.html', rows = stocks)

@app.route('/plot')
def candlestick_plot():
	ticker = request.args.get('stock')
	stock = retriveStockData(ticker)
	df = stock.info
	fig = FF.create_candlestick(df.open, df.high, df.low, df.close, dates = df.daytime)
	# Create Line of open values
	add_line = Scatter(
		x = df.daytime,
		y = df.open,
		name = 'Open Vals',
		line = Line(color='black')
		)
	fig['data'].extend([add_line])
	plotly.offline.plot(fig, filename = 'candlestick.html', validate=False, auto_open=False)
	file = open('candlestick.html', 'r')
	return file.read()

if __name__ == '__main__':
	manager.run() # Runs the flask server in a special way that makes it nice to debug




