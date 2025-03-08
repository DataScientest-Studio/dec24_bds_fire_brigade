import streamlit as st
from config import df_inc, df_mob
from PIL import Image

def show(df_merged):
    # load images
    map = Image.open("./images/incident_map.png")
    
    st.title("Data Preparation")
    # dataframe feature description
    st.title("Feature Table Incidents")
    st.dataframe(df_inc, height=300)
    st.title("Feature Table Mobilisation")
    st.dataframe(df_mob, height=300)
    
    # dropping the first features
    st.subheader("Feature Selection")
    st.write(
    "To refine our dataset for analysis, we removed several columns that were not relevant to our study. "
    "These columns contained information such as location codes, property types, and other attributes that did not contribute to our insights.")
    st.markdown("### **Dropped Columns**")
    st.markdown("#### **Incidents Dataset**")
    st.code(
    "['PropertyType', 'IncGeo_BoroughCode', 'IncGeo_BoroughName', 'IncGeo_WardName', "
    "'IncGeo_WardNameNew', 'IncGeo_WardCode', 'Postcode_full', 'Easting_m', 'Northing_m', "
    "'FRS', 'NumCalls', 'UPRN', 'USRN', 'Latitude', 'Longitude']",
    language="python")
    st.markdown("#### **Mobilisation Dataset**")
    st.code(
    "['WardName', 'PlusCode_Code', 'PlusCode_Description', 'Resource_Code', "
    "'DeployedFromStation_Code', 'DelayCodeId']",
    language="python")
    st.write("By filtering out these columns, we focused on the most meaningful data for our analysis.")
    
    # delay cide imputation
    st.subheader("Imputing Missing Delay Codes")
    st.write(
    "Nearly **50%** of `DelayCode_Description` was missing. Since it's crucial for analysis, "
    "we used **probability-based imputation** based on travel and attendance times.")
    st.markdown("### **Delay Category Probabilities**")
    st.json({
        'Not held up': 0.60, 'Traffic/Roadworks': 0.20, 'Traffic calming': 0.06, 
        'Wrong address': 0.06, 'Radio issues': 0.02, 'Weather': 0.01, 
        'Equipment defect': 0.005, 'At drills': 0.004})
    st.write(
    "Missing values were filled based on **predefined time ranges**, ensuring consistency "
    "with known patterns in the data.")
    st.success("This approach preserved `DelayCode_Description` for better analysis.")
    st.subheader("Cleaning the Dataset")
    st.write(
    "After imputing missing delay codes, we **removed all remaining missing rows** to ensure data integrity. "
    "This step helped maintain a **clean and complete dataset** for further analysis.")
    st.success("Final dataset is free of missing values and ready for modeling.")
    
    # distance feature engineering
    st.subheader("Feature Engineering: Distance Calculation")
    st.write(
    "To improve our model, we calculated the **distance** between the **fire station** and the **incident location**. "
    "Using the **great-circle distance formula**, we derived an additional feature: **distance in kilometers**.")
    st.success("A new **distance_km** column was added, providing a crucial feature for predicting attendance time.")
    st.image(map, caption="Figure 1. Map showing all incidents (red) and the fire stations (blue).")