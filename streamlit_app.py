import streamlit
import pandas as pd
import requests
import snowflake.connector

streamlit.title('My Parents new Healthy Diner')

streamlit.header('Breakfast Menu')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list;")
my_data = my_cur.fetchall()
streamlit.dataframe(my_data_row)



streamlit.header('Customize Your Own Smoothie')


my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect('Pick Fruits: ', list(my_fruit_list.index), ['Avocado', 'Strawberries'])

streamlit.dataframe(my_fruit_list.loc[fruits_selected])


streamlit.header("Fruityvice Advice")

fruit_choice = streamlit.text_input('Which fruit interests you?', 'Kiwi')
streamlit.text(f'The user entered {fruit_choice}')

fruityvice_response = pd.json_normalize(requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}").json())

streamlit.dataframe(fruityvice_response)

