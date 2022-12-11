import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App         

Stock Closing Price and Volume of Google's Stock - **GOOGL**
         
""")

#Ticker Definition
tickerSymbol = 'GOOGL'

#Get Data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#Get Historical Prices
tickerDf = tickerData.history(period = 'id', start = '2010-5-31', end = '2022-11-30')

#Open High Close Low 

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

#APPLE

st.write("""        

Stock Closing Price and Volume of Apple's Stock - **AAPL**
         
""")


#Ticker Definition
tickerSymbol = 'AAPL'

#Get Data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#Get Historical Prices
tickerDf = tickerData.history(period = 'id', start = '2010-5-31', end = '2022-11-30')
#Open High Close Low 

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

