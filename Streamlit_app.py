import streamlit

streamlit.header('Breakfast Favorites')
streamlit.text(' Burger')
streamlit.text('綾 Salad')
streamlit.header('Build your own Fruit Smoothie')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
