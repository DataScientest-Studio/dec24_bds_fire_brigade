import streamlit as st
import pandas as pd
import modules.data_exploration as data_exploration
import modules.data_preparation as data_preparation
import modules.modelling as modelling

# Cache datasets
@st.cache_data
def load_data():
    path = "C:/datascientest/streamlit/"
    print("loading dataset")
    # load the preprocessed df
    df_merged = pd.read_csv(f"{path}merged/clean_merge_v2.xls", sep=";")
    
    return df_merged

# Load all datasets only once
df_merged = load_data()

# Sidebar Navigation
st.sidebar.title("Table of Contents")
pages = {
    "Data Exploration": data_exploration,
    "Data Preparation": data_preparation,
    "Modelling": modelling
}

page = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page and pass data
pages[page].show(df_merged)
