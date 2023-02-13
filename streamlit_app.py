import streamlit
import pandas as pd

streamlit.title('My Parents new Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Dies, Das, verschiedene Dinge')

streamlit.header('Customize Your Own Smoothie')


my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

streamlit.multiselect('Pick Fruits: ', list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)

