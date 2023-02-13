import streamlit
import pandas as pd

streamlit.title('My Parents new Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Dies, Das, verschiedene Dinge')

streamlit.header('Customize Your Own Smoothie')


my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect('Pick Fruits: ', list(my_fruit_list.index), ['Avocado', 'Strawberries'])

streamlit.dataframe(my_fruit_list.loc[fruits_selected])

