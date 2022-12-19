# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

#series_df = pd.read_pickle("seriesdata.pkl")
alldata_df = pd.read_pickle("../alldata_final.pkl")

choices = alldata_df['series_id'].unique().tolist()


app.layout = html.Div(children=[
	dcc.Dropdown(choices, choices[0],id="series_id"),
	dcc.Graph(id="output-graph")])


@app.callback(
	Output(component_id='output-graph', component_property='figure'),
	Input(component_id='series_id', component_property='value')
	)
def seriesplot(input_value):
		
		df = alldata_df.loc[ alldata_df['series_id'] == input_value ]
		fig = px.line(df, x='date', y="value")
		return fig

if __name__ == '__main__':
    app.run_server(debug=False)