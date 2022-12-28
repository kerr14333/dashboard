# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output, dash_table
import plotly.express as px
import pandas as pd

app = Dash(__name__)

#series_df = pd.read_pickle("seriesdata.pkl")
alldata_df = pd.read_pickle("../alldata_final.pkl")
series_df = pd.read_pickle(r"../series_df_final.pkl")


choices = series_df[ ['series_id','series_title']].set_index('series_id').T.to_dict('list')

mycols = ['year','month','value']

app.layout = html.Div(children=[
	dcc.Dropdown(choices,list(choices.keys())[0],id="series_id"),
	dcc.Graph(id="output-graph"),	
	dash_table.DataTable(
    id='datatable-source',
    columns=[
        {"name": i, "id": i} for i in mycols
    	]
    )]
    )


@app.callback(
    Output('datatable-source', 'data'),
    Input(component_id='series_id', component_property='value'))
def update_table(input_value):
    df = alldata_df.loc[ alldata_df['series_id'] == input_value, mycols ]

    return df.to_dict('records')



@app.callback(
	Output(component_id='output-graph', component_property='figure'),
	Input(component_id='series_id', component_property='value')
	)
def seriesplot(input_value):
		
		df = alldata_df.loc[ alldata_df['series_id'] == input_value ]
		fig = px.line(df, x='date', y="value",title = choices[input_value][0])
		return fig

if __name__ == '__main__':
    app.run_server(debug=False)