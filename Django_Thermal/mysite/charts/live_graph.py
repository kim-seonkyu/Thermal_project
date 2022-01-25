from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import datetime
from django_plotly_dash import DjangoDash
from .models import TempData


app = DjangoDash('LiveGraph')

app.layout = html.Div([
	dcc.Graph(id = 'live-graph', animate = True),
	dcc.Interval(
	id = 'graph-update',
	interval = 1*5000,
	n_intervals = 0
	),
])

@app.callback(
Output('live-graph', 'figure'),
[ Input('graph-update', 'n_intervals') ]
)

def update_graph(n):
    	
	total_time = []
	max_temp = []
	min_temp = []
	avg_temp = []

	datas = TempData.objects.all()
	for data in datas:
		total_time.append(data.time)
		max_temp.append(data.maxtemp)
		min_temp.append(data.mintemp)
		avg_temp.append(data.avgtemp)
		last_time = data.time

	data1 = plotly.graph_objs.Scatter(
		x=total_time,
		y=max_temp,
		name='Max Temperature',
		mode= 'lines+markers'
	)
	data2 = plotly.graph_objs.Scatter(
		x=total_time,
		y=avg_temp,
		name='Min Temperature',
		mode= 'lines+markers'
	)
	data3 = plotly.graph_objs.Scatter(
		x=total_time,
		y=min_temp,
		name='Avg Temperature',
		mode= 'lines+markers'
	)
	data = [data1, data2, data3]
	layout = go.Layout(xaxis=dict(title='Datetime', range=([min(total_time), max(total_time)])), yaxis = dict(title='Temperature˚C', range=([min(min_temp)-1, max(max_temp)+1])),)
	
	return go.Figure(data=data, layout=layout)
