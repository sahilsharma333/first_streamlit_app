import streamlit

streamlit.header('Breakfast Favorites')
streamlit.text(' Burger')
streamlit.text('綾 Salad')
streamlit.header('Build your own Fruit Smoothie')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here
streamlit.multiselect("Pick Some Fruits :, list(my_fruit_list.index))

# display the table on the page                      
streamlit.dataframe(my_fruit_list)
