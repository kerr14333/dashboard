# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.



###### conda install -c conda-forge dash-bootstrap-components

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd



################# Read in data and get series #########################

alldata_df = pd.read_pickle("../alldata_final.pkl")

series_df = pd.read_pickle("../series_df_final.pkl")

choices = { k:v for (k,v) in zip( series_df['series_id'].tolist() , series_df['series_title'].tolist() ) }

first_chioce = list(choices.keys())[0]
################ Begin Dash App #######################################

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])



###########Create app layout ######

sidebar = html.Div(
    [
        dcc.Dropdown(choices, first_chioce,id="series_id")
    ],
 )

content = html.Div([dcc.Graph(id="output-graph")],id="page-content")

app.layout = dbc.Container(
    [
        html.H1("Labor Force Data Plotter"),
        dbc.Row([
                dbc.Col(sidebar,md=4),
                dbc.Col(content,md=8)
            ])

    ],
    fluid=True
)




######### Call Backs  #################################################

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

