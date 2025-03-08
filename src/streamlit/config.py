# config.py
import pandas as pd

# Google image URL
lfb_logo = "https://www.london-fire.gov.uk/media/3282/london-fire-brigade-hompage-firefighter-ladder-new-ppe.jpg"

# Facts DataFrame
data = {
    "Facts": [
        "Stations", 
        "Firefighters", 
        "Boroughs Covered", 
        "Population Served", 
        "Annual Emergency Calls", 
        "Coverage Area (km²)"
    ],
    "Details": [
        "103", 
        "Over 5,000", 
        "13", 
        "8 million", 
        "100,000 - 130,000", 
        "1,587"
    ]
}

df_facts = pd.DataFrame(data)

# Incident
data_inc = [
    ["IncidentNumber", "LFB Incident Number", "object", "0.00%", "Unique Value"],
    ["DateOfCall", "Date of 999 call", "object", "0.00%", "Date"],
    ["CalYear", "Year of 999 call", "int64", "0.00%", "Date"],
    ["TimeOfCall", "Time of 999 call", "object", "0.00%", "Date"],
    ["HourOfCall", "Hour of 999 call", "int64", "0.00%", "Date"],
    ["IncidentGroup", "High level incident category", "object", "0.00%", "Categorical - 3 to 5 categories"],
    ["StopCodeDescription", "Detailed incident category", "object", "0.00%", "Categorical - more than 10 categories"],
    ["SpecialServiceType", "Further detail for special services incident categories", "object", "67.39%", "Categorical - more than 10 categories"],
    ["PropertyCategory", "High level property descriptor", "object", "0.00%", "Categorical - 6 to 10 categories"],
    ["PropertyType", "Detailed property descriptor", "object", "0.00%", "Categorical - more than 10 categories"],
    ["AddressQualifier", "Qualifies location of actual incident relevant to category above", "object", "0.00%", "Categorical - more than 10 categories"],
    ["Postcode_full", "Postcode", "object", "50.14%", "Categorical - more than 10 categories"],
    ["Postcode_district", "Postcode Districs", "object", "0.00%", "Categorical - more than 10 categories"],
    ["UPRN", "Unique Property Reference Number", "int64", "7.88%", "Categorical - more than 10 categories"],
    ["USRN", "Unique Street Reference Number", "object", "9.08%", "Categorical - more than 10 categories"],
    ["IncGeo_BoroughCode", "Borough Code", "object", "0.00%", "Categorical - more than 10 categories"],
    ["IncGeo_BoroughName", "Borough Name", "object", "0.00%", "Categorical - more than 10 categories"],
    ["ProperCase", "Wrong description in metadata", "object", "0.00%", "Categorical - more than 10 categories"],
    ["IncGeo_WardCode", "Ward Code", "object", "0.03%", "Categorical - more than 10 categories"],
    ["IncGeo_WardName", "Ward Name", "object", "0.03%", "Categorical - more than 10 categories"],
    ["IncGeo_WardNameNew", "New Ward Name", "object", "0.03%", "Categorical - more than 10 categories"],
    ["Easting_m", "Easting", "float64", "50.14%", "Categorical - more than 10 categories"],
    ["Northing_m", "Northing", "float64", "50.14%", "Categorical - more than 10 categories"],
    ["Easting_rounded", "Easting rounded up to nearest 50", "object", "0.00%", "Categorical - more than 10 categories"],
    ["Northing_rounded", "Northing rounded up to nearest 50", "object", "0.00%", "Categorical - more than 10 categories"],
    ["Latitude", "Latitude", "float64", "50.14%", "Categorical - more than 10 categories"],
    ["Longitude", "Longitude", "float64", "50.14%", "Categorical - more than 10 categories"],
    ["FRS", "Fire Service ground", "object", "0.00%", "Single Value"],
    ["IncidentStationGround", "LFB Station ground", "object", "0.00%", "Categorical - more than 10 categories"],
    ["FirstPumpArriving_AttendanceTime", "First Pump attendance time in seconds", "int64", "7.63%", "Quantitative"],
    ["FirstPumpArriving_DeployedFromStation", "First Pump deployed from station", "object", "7.63%", "Categorical - more than 10 categories"],
    ["SecondPumpArriving_AttendanceTime", "Second Pump attendance time in seconds", "int64", "64.21%", "Quantitative"],
    ["SecondPumpArriving_DeployedFromStation", "Second Pump deployed from station", "object", "64.21%", "Categorical - more than 10 categories"],
    ["NumStationsWithPumpsAttending", "Number of stations with pumps in attendance", "int64", "0.80%", "Categorical - more than 10 categories"],
    ["NumPumpsAttending", "Number of pumps in attendance", "int64", "0.80%", "Categorical - more than 10 categories"],
    ["PumpCount", "", "int64", "0.00%", "Categorical - more than 10 categories"],
    ["PumpMinutesRounded", "Time spent at incident by pumps, rounded up to 60 if less than an hour", "float64", "0.00%", "Quantitative"],
    ["Notional Cost (£)", "Time spent multiplied by notional annual cost of a pump", "float64", "0.00%", "Quantitative"],
    ["NumCalls", "Number of calls received about the incident", "int64", "0.10%", "Categorical - more than 10 categories"]
]

# Create the DataFrame
df_inc = pd.DataFrame(data_inc, columns=["name", "description", "type","%nan", "Cat/Quant"])

# Mobilisation
data_mob = [
    ["IncidentNumber", "LFB Incident Number", "object", "0.00%", "Unique Value"],
    ["CalYear", "Year of the 999 call", "int64", "0.00%", "Date"],
    ["HourOfCall", "Hour of the 999 call", "int64", "0.00%", "Categorical - more than 10 categories"],
    ["ResourceMobilisationId", "LFB Resource Mobilisation ID", "int64", "0.00%", "Categorical - more than 10 categories"],
    ["Resource_Code", "LFB Resource Code", "object", "0.00%", "Categorical - more than 10 categories"],
    ["PerformanceReporting", "First Pump arrived at incident", "object", "0.00%", "Categorical - 3 to 5 categories"],
    ["DateAndTimeMobilised", "Date and time of mobilised (GMT)", "object", "0.00%", "Date"],
    ["DateAndTimeMobile", "Date and time of mobile (GMT)", "object", "1.14%", "Date"],
    ["DateAndTimeArrived", "Date and time arrived (GMT)", "object", "0.00%", "Date"],
    ["TurnoutTimeSeconds", "Time to mobilize and leave after alerted in seconds", "float64", "1.14%", "Quantitative"],
    ["TravelTimeSeconds", "Travel time in seconds", "float64", "1.14%", "Quantitative"],
    ["AttendanceTimeSeconds", "Time it takes after mobilization and be fully operational in seconds", "int64", "0.00%", "Quantitative"],
    ["DateAndTimeLeft", "Date and time left the incident (GMT)", "object", "1.85%", "Date"],
    ["DateAndTimeReturned", "Date and time returned to station (GMT)", "datetime64[ns]", "61.28%", "Date"],
    ["DeployedFromStation_Code", "Deployed from station code", "object", "0.00%", "Categorical - more than 10 categories"],
    ["DeployedFromStation_Name", "Deployed from station name", "object", "0.00%", "Categorical - more than 10 categories"],
    ["DeployedFromLocation", "Deployed from location", "object", "0.05%", "Categorical - more than 10 categories"],
    ["PumpOrder", "Pump order", "int64", "0.00%", "Categorical - 3 to 5 categories"],
    ["PlusCode_Code", "Code of Plus Code", "object", "0.00%", "Categorical - more than 10 categories"],
    ["PlusCode_Description", "Description of Plus Code", "object", "75.05%", "Categorical - more than 10 categories"],
    ["DelayCodeId", "Delay code ID", "float64", "75.05%", "Categorical - more than 10 categories"],
    ["DelayCode_Description", "Delay code description", "object", "71.15%", "Categorical - more than 10 categories"],
    ["BoroughName", "Name of the Borough", "object", "71.15%", "Categorical - more than 10 categories"],
    ["WardName", "Name of the Ward", "object", "0.00%", "Categorical - more than 10 categories"]
]

# Create DataFrame
df_mob = pd.DataFrame(data_mob, columns=["name", "description", "type","%nan", "Cat/Quant"])
