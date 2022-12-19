

import matplotlib.pyplot as plt
import pandas as pd
from shiny import App, render, ui

#series_df = pd.read_pickle("seriesdata.pkl")
alldata_df = pd.read_pickle("alldata_final.pkl")

choices = alldata_df['series_id'].unique().tolist()

app_ui = ui.page_fluid(
ui.panel_title("Series Plotter"),
ui.layout_sidebar(
	ui.panel_sidebar(
		ui.input_select("series_ids","Series:", choices )
		),
	ui.panel_main( 
		ui.output_plot("seriesplot")
		),
	),
)

def server(input, output, session):	
	@output
	@render.plot
	def seriesplot():
		
		df = alldata_df.loc[ alldata_df['series_id'] == input.series_ids() ]
		fig, ax = plt.subplots(figsize=(8, 6))
		ax.plot(df['date'], df['value']);

app = App(app_ui, server, debug=True )