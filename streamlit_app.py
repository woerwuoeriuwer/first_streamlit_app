import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents new Healthy Diner')

streamlit.header('Breakfast Menu')




streamlit.header('Customize Your Own Smoothie')


my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect('Pick Fruits: ', list(my_fruit_list.index), ['Avocado', 'Strawberries'])

streamlit.dataframe(my_fruit_list.loc[fruits_selected])


streamlit.header("Fruityvice Advice")

try:
  fruit_choice = streamlit.text_input('Which fruit interests you?', 'Kiwi')
  if not fruit_choice:
    streamlit.error("Enter a fruit!")
  else:
    streamlit.text(f'The user entered {fruit_choice}')
    fruityvice_response = pd.json_normalize(requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}").json())
    streamlit.dataframe(fruityvice_response)
except URLError as e:
  streamlit.error("urlerror")



if streamlit.button("Get fruit list"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_cur = my_cnx.cursor()
  my_cur.execute("select * from fruit_load_list;")
  my_data = my_cur.fetchall()
  streamlit.dataframe(my_data)


add_fruit = streamlit.text_input("Which fruit would you like to add?", 'jackfruit')
if streamlit.button("Add fruit to list"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_cur = my_cnx.cursor()
  my_cur.execute(f"insert into fruit_load_list (fruit_name) values ('{add_fruit}');")


