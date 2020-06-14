import pandas as pd
import streamlit as st
import numpy as np
st.title('Youtube Search History and Subscription Data Visualisation')

df= pd.read_json('history/search-history.json')
search_df = pd.read_json('history/search-history.json')
search_df['time']=pd.to_datetime(search_df['time'])
search_df['title']=search_df['title'].str.replace('Searched for ', '')


#print(search_df.columns())
#print(cleaned_titles.head())
#print(df.head())
#print(search_df['time'].head())
search_df['Year'],search_df['Month']=search_df['time'].dt.year,search_df['time'].dt.month_name()
search_df['Day']=search_df['time'].dt.day
search_df['Day_of_week']=search_df['time'].dt.day_name()
#print(search_df['Year'],search_df['Month'])
#print(search_df['Day'])
print(search_df.head())
search_df=search_df.drop(columns=['details','products','titleUrl'])

#keywords to look for in search title 
search_df['title']=search_df['title'].str.lower()
st.write(search_df)

#how many times i watch youtube in a year which is my businest month

#how many times i watch youtube in a month?

#how many times i watch youtube in a day?

#which are the hours where i watch youtube the most

