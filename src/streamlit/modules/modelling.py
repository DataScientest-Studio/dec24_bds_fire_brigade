import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import xgboost as xgb
import pandas as pd

# Cache the preprocessing and training steps
@st.cache_data
def preprocess_data(df_merged):
    # Data Preprocessing (dropping columns, encoding, scaling, etc.)
    df_drop = df_merged.drop(["IncidentNumber", "DateAndTimeMobilised", "DateAndTimeMobile", "DateAndTimeArrived", 
                              "TurnoutTimeSeconds", "TravelTimeSeconds", "Incident_Date", "DateOfCall", "IncidentStationGround", 
                              "ProperCase", "FirstPumpArriving_AttendanceTime", "FirstPumpArriving_DeployedFromStation", 
                              "SecondPumpArriving_AttendanceTime", "SecondPumpArriving_DeployedFromStation", "Postcode_district", 
                              "PerformanceReporting", "Notional Cost (£)", "PumpMinutesRounded"], axis=1)

    # Target and features split
    target = "AttendanceTimeSeconds"
    X = df_drop.drop(columns=[target])  # Features
    y = df_drop[target]  # Target variable

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Encoding and scaling
    label_cols = ["DeployedFromLocation", "IncidentGroup", "Weekday_compat_mobs", "PropertyCategory", "AddressQualifier"]
    le = LabelEncoder()
    for col in label_cols:
        X_train[col] = le.fit_transform(X_train[col])
        X_test[col] = le.transform(X_test[col])

    # Target Encoding
    target_cols = ["DelayCode_Description", "StopCodeDescription", "DeployedFromStation_Name"]
    te = TargetEncoder(cols=target_cols)
    X_train[target_cols] = te.fit_transform(X_train[target_cols], y_train)
    X_test[target_cols] = te.transform(X_test[target_cols])

    # Scaling numerical features
    num_cols_to_scale = ["distance_km"]
    scaler = StandardScaler()
    X_train[num_cols_to_scale] = scaler.fit_transform(X_train[num_cols_to_scale])
    X_test[num_cols_to_scale] = scaler.transform(X_test[num_cols_to_scale])

    return X_train, X_test, y_train, y_test

# Cache the model training and prediction
@st.cache_data
def train_xgboost(X_train, y_train, X_test, y_test):
    # Initialize XGBoost Regressor with best parameters
    xgb_reg = xgb.XGBRegressor(subsample=1.0, reg_lambda=0, reg_alpha=0.1, n_estimators=300, max_depth=8, learning_rate=0.2, colsample_bytree=0.6, random_state=42)

    # Train the model
    xgb_reg.fit(X_train, y_train)

    # Predict on test set
    y_pred = xgb_reg.predict(X_test)

    # Calculate performance metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Predictions on training data
    y_train_pred = xgb_reg.predict(X_train)
    train_mae = mean_absolute_error(y_train, y_train_pred)
    train_mse = mean_squared_error(y_train, y_train_pred)
    train_r2 = r2_score(y_train, y_train_pred)

    return mae, mse, r2, train_mae, train_mse, train_r2, y_pred

# Streamlit application code
def show(df_merged):
    st.title("Modelling")
    # 1. linear regression default model
    st.write("### 1. Linear Regression Default Model")
    st.write(
        "In this section, we will train a **Linear Regression** model to predict `AttendanceTimeSeconds`."
        " The following steps include preparing the data, training the model, and evaluating its performance.")
    st.write("##### Data Preprocessing")
    st.write(
        "We begin by removing irrelevant columns that do not contribute to the model. This includes columns like `IncidentNumber`, `DateAndTimeMobilised`, etc."
        " Removing these helps simplify the model and ensures that only useful information is used.")
    
    # Preprocess the data using the cached function
    X_train, X_test, y_train, y_test = preprocess_data(df_merged)

    st.write("##### Training the Model")
    st.write(
        "We now initialize the **Linear Regression** model and train it using the processed data.")
    
    # Initialize the model
    lr = LinearRegression()

    # Train the model
    lr.fit(X_train, y_train)

    st.write("##### Making Predictions and Evaluating the Model")
    st.write(
        "Once the model is trained, we use it to make predictions on the test set. Then, we evaluate the model's performance using three key metrics:")

    # Make predictions
    y_pred = lr.predict(X_test)

    # Calculate performance metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Create a DataFrame for the Linear Regression model metrics
    lr_metrics = pd.DataFrame({
    "Metric": ["MAE (Mean Absolute Error)", "MSE (Mean Squared Error)", "R² Score"],
    "Value": [mae, mse, r2]})

    # Display the metrics
    st.table(lr_metrics)
    
    # 2. XGBOOST
    st.write("### 2. XGBoost Model")
    st.write(
        "In this section, we will train an **XGBoost Regressor** model to predict `AttendanceTimeSeconds`."
        " The following steps include initializing the model, training it, and evaluating its performance."
        " XGBoost is a powerful boosting algorithm commonly used for regression tasks due to its efficiency and performance.")
    
    # Display initial results of XGBoost with default parameters
    st.write("##### XGBoost Default Model Performance")
    st.write(
        "Initially, we executed the XGBoost model with the default parameters and evaluated its performance. "
        "The model's results were as follows:")

    xgb_default_metrics = pd.DataFrame({
    "Metric": ["MAE (Mean Absolute Error)", "MSE (Mean Squared Error)", "R² Score"],
    "Value": [69.54, 10431.16, 0.55]})
    st.table(xgb_default_metrics)

    st.write("##### Hyperparameter Tuning with RandomizedSearchCV")
    st.write(
        "Afterward, we executed **RandomizedSearchCV** with 5-fold cross-validation to find the optimal hyperparameters for the XGBoost model. "
        "The best parameters found were as follows:")

    st.write("**Best Parameters:**")
    st.write("`subsample=1.0, reg_lambda=0, reg_alpha=0.1, n_estimators=300, max_depth=8, learning_rate=0.2, colsample_bytree=0.6`")
    
    st.write("With these optimal parameters, the model was retrained and provided the following performance metrics:")

    # Train the XGBoost model with the cached function
    mae, mse, r2, train_mae, train_mse, train_r2, y_pred = train_xgboost(X_train, y_train, X_test, y_test)

    train_metrics = pd.DataFrame({
    "Metric": ["MAE (Mean Absolute Error)", "MSE (Mean Squared Error)", "R² Score"],
    "Value": [train_mae, train_mse, train_r2]})

    test_metrics = pd.DataFrame({
    "Metric": ["MAE (Mean Absolute Error)", "MSE (Mean Squared Error)", "R² Score"],
    "Value": [mae, mse, r2]})

    # Use columns to display the tables side by side
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Training Set Metrics")
        st.table(train_metrics)

    with col2:
        st.write("### Test Set Metrics")
        st.table(test_metrics)
