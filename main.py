
# (1) Import the required libraries

import streamlit as st
import plotly as pt 
import pandas as pd
import os               # for file handling
import warnings         # incase there is some kind of warring’s so i want to ignore those
warnings.filterwarnings('ignore')

# (2) Page Configuration and Dashboard Tittle

# set the tittle of the page 
st.set_page_config(page_title="Dashboard!!!", page_icon=":bar_chart:", layout="wide", )

# set the title of Dashboard 
st.title("EDA of Superstore Data :bar_chart:")

st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# (3) setting File uploader option on dashboard

fl = st.file_uploader(":file_folder: Upload a File", type=(["csv", "txt", "xlsx", "xls"]))
if fl is not None:
    fileName = fl.name
    st.write(fileName)
    df = pd.read_csv(fileName, encoding ="ISO-8859-1")
else:
    os.chdir(r"C:\Users\hp\Google Drive\Fiverr Work\2023\57. Interactive Data Dashboard for Superstor Data (EDA)")
    df = pd.read_csv("Superstore.csv", encoding ="ISO-8859-1")