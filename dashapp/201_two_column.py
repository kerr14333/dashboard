# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.



###### conda install -c conda-forge dash-bootstrap-components

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd



################# Read in data and get series #########################

alldata_df = pd.read_pickle("../alldata_final.pkl")

choices = alldata_df['series_id'].unique().tolist()



################ Begin Dash App #######################################

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])



######### CSS ######################

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}



###########Create app layout ######

sidebar = html.Div(
    [
        dcc.Dropdown(choices, choices[0],id="series_id")
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div([dcc.Graph(id="output-graph")],id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([sidebar, content])


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

