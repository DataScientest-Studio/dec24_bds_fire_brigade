import streamlit as st
from config import lfb_logo, df_facts
from PIL import Image

def show(df_merged):
    # Load images
    incident_time = Image.open("./images/incident_time.png")
    attendance_time = Image.open("./images/attendance_time.png")
    attendance_time_property = Image.open("./images/attendance_time_property.png")
    attendance_delay = Image.open("./images/attendance_delay.png")
    
    # Introduction
    st.title("Data Exploration")
    st.image(lfb_logo)
    st.write("This project aims to estimate the London Fire Brigade's attendance time. As the busiest fire service in the UK, understanding its response efficiency is key to improving performance.\n"
             "The study aims to provide insights into factors affecting response times and overall operational performance.")
    
    st.title("Context")
    st.markdown(df_facts.to_html(index=False, escape=False), unsafe_allow_html=True)
    
    st.write("The London Fire Brigade (LFB) is the world's largest fire service, operating 103 stations with over 5,000 firefighters across 13 boroughs, serving 8 million people.\n"
             "It responds to 100,000–130,000 emergency calls annually across 1,587 km². In life-threatening situations, every minute counts, and delays worsen outcomes.\n"
             "Predicting response times could optimize logistics, reassure callers, and improve dispatch efficiency, ultimately saving lives.")
    
    st.title("Data")
    st.write("This project relies on two datasets: [LFB's incident data](https://data.london.gov.uk/dataset/london-fire-brigade-incident-records)\n"
             "and [LFB's mobilization data](https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records).\n"
             "Both datasets are sourced from The London Datastore, a free and open data-sharing platform providing public access to various datasets related to London.")

    ## Exploration
    st.title("Visualization of Dataset")
    st.image(incident_time, caption="Figure 1. Histogram showing year-dependent (A), month-dependent (B), weekday-dependent (C) and hour of the day-dependent (D) fluctuations in emergency call (call) numbers.")
    st.image(attendance_time, caption="Figure 2. Visualisation of all histograms merged into a single graph to display differences in incident numbers.")
    st.image(attendance_time_property, caption="Figure 3. Histogram showing the mean first pump arrival time as a function of the property category.")
    st.image(attendance_delay, caption="Figure 4. Histograms showing the turnout time (binwidth = 30 s) at different delay code conditions.")
