import streamlit

streamlit.header('Breakfast Favorites')
streamlit.text(' Burger')
streamlit.text('綾 Salad')
streamlit.header('Build your own Fruit Smoothie')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here
fruits_selected = streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# display the table on the page                      
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')

import requests

streamlit.text(fruityvice_response.json())

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)
