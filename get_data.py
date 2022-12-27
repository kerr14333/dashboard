#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
from datetime import date



print("""
	  *********************** Getting Data for Tutorial *************************************
	  Data is originally from "https://download.bls.gov/pub/time.series/ln/ln.data.1.AllData"
	  The download is about 350MB and may take a moment to finish. Maybe get a cup of coffee
	  Note that I only take monthly series.
	  ***************************************************************************************


	  """)

alldata_df = pd.read_csv(r"https://download.bls.gov/pub/time.series/ln/ln.data.1.AllData", delimiter="\t",)

print("""
	  *********************** Cleaning Data *********************************************
	  

	  """)

#remove space from columns
alldata_df.columns = alldata_df.columns.str.strip()

#convert values to numeric
alldata_df['value'] = pd.to_numeric( alldata_df['value'], errors='coerce')

#remove other extra spaces
df_obj = alldata_df.select_dtypes(['object'])
alldata_df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())

#extract frequency and month from period
alldata_df['freq'] = alldata_df['period'].str[0]
alldata_df['month'] = pd.to_numeric( alldata_df['period'].str[1:], errors='coerce' )


#subset to only monthly data
alldata_df = alldata_df.loc[ alldata_df['freq'] == "M" ]

#create date variable
alldata_df['date'] = pd.to_datetime(alldata_df[['year', 'month']].assign(day=1), errors='coerce')


print("""
	  *********************** Pickling Data ********************************************
	  The final file we will use will be 'alldata_final.pkl'
	  

	  """)

#send final dataset to pickle
alldata_df.to_pickle("alldata_final.pkl")



print("""
	  *********************** Downloading Series IDs and Labels  ************************
	  Data is originally from "https://download.bls.gov/pub/time.series/ln/ln.series"
	  This download shouldn't take as long.
	  ***********************************************************************************


	  """)


series_df = pd.read_csv(r"https://download.bls.gov/pub/time.series/ln/ln.series", delimiter="\t")


print("""
	  *********************** Cleaning Data ********************************************
	  
	  """)

series_df.columns = series_df.columns.str.strip()


df_obj = series_df.select_dtypes(['object'])
series_df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())


# In[19]:


mycols = ['series_id','periodicity_code', 'series_title']
series_df_final = series_df.loc[ series_df['periodicity_code']=='M', mycols]


print("""
	  *********************** Pickling Series ID/Label Data **************************
	  The final series id/label file will be "'series_df_final.pkl'
	  ********************************************************************************

	  """)

series_df_final.to_pickle("series_df_final.pkl")


print("""
	  *********************** Finished. THANKS! You should be all set. ***************
	  

	  """)

