import pandas as pd
import streamlit as st
import yfinance as yf
from datetime import date

st.write ('''
#                Google Stock Ticker

Shows **Close price** and **Volume**.

''')

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

df = tickerData.history(period = 'id', start = '2020-7-31', end = date.today())
# Open, High, Low, Close, Volume, Dividends, Stock splits
st.line_chart(df.Close)
st.line_chart(df.Volume)
