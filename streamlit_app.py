import streamlit
import pandas as pd
import requests

streamlit.title('My Parents new Healthy Diner')

streamlit.header('Breakfast Menu')



streamlit.header('Customize Your Own Smoothie')


my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect('Pick Fruits: ', list(my_fruit_list.index), ['Avocado', 'Strawberries'])

streamlit.dataframe(my_fruit_list.loc[fruits_selected])


streamlit.header("Fruityvice Advice")

streamlit.text_input('Which fruit interests you?', 'Kiwi')

fruityvice_response = pd.json_normalize(requests.get("https://fruityvice.com/api/fruit/watermelon").json())

streamlit.dataframe(fruityvice_response)

