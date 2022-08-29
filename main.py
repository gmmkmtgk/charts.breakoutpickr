#dashboard to show some stock charts and data
from nsepy import get_history
from datetime import date
import streamlit as st
import pandas as pd 
from PIL import Image
from datetime import datetime

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.write("""
# Stocks Charts Web Application
### Get the Stock Chart of your Choice
""")



#Create sidebar header

image = Image.open("logo.png")

st.sidebar.image(image, width= 150)

st.sidebar.header('User Input')


#Create a fuction to get the users input 
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-1-1")
    end_date = st.sidebar.text_input("End Date", "2022-8-26")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "SBIN")
    return start_date, end_date, stock_symbol


def get_data(sym, start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    data = get_history(symbol=sym,start=start_date,end=end_date)
    return data

#Get User Input 
start , end ,  symbol = get_input()

#Get the data
df = get_data(symbol, start, end)

#Display the Close Price 
st.header(symbol + " Close Price Chart\n")
st.line_chart(df['Close'])


