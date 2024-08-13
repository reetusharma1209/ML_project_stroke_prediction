import pandas as pd
import streamlit as st
import pandas as pd
from backend import *
from datetime import datetime

#############################################################################################################################
######################################################## CSS ################################################################
#############################################################################################################################

# Apply custom theme
st.set_page_config(
    page_title="Health Stroke",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)



#############################################################################################################################
################################################## Load Data ################################################################
#############################################################################################################################

# Load the datasets
data_health = pd.read_csv('healthcare-dataset-stroke-data.csv')

# App title
st.title('Health Stroke')
st.markdown("### The Digital Challenge")
st.markdown("**Created by Mahshid Khatami and Faheem Khan**")
st.markdown("**The digital world is evolving, and so are Vanguard’s clients. Vanguard believed that a more intuitive and modern User Interface (UI), coupled with timely in-context prompts (cues, messages, hints, or instructions provided to users directly within the context of their current task or action), could make the online process smoother for clients. The critical question was: Would these changes encourage more clients to complete the process?**")

#############################################################################################################################
################################################## Filter ###################################################################
#############################################################################################################################

# Sidebar for navigation
st.sidebar.title('Filters')

################################################ Data Filter #######################################################

options = st.sidebar.radio('Select a dataset to explore:', ['User Log', 'Client Information', 'Experiment Clients'])


################################################ Age Filter #######################################################


# Create a radio button for selecting age range
age_range = st.sidebar.slider(
    'Select Age Range', min_value=int(data_health['age'].min()), 
    max_value=int(data_health['age'].max()), 
    value=(int(data_health['age'].min()), 
           int(data_health['age'].max()))
)


################################################ Gender Filter #######################################################
# Create a radio button for selecting Gender
age_range = st.sidebar.radio(
    "Select Gender",
    ('All', 'Female', 'Male', 'Other')
)

# Filter data based on selected age range
if age_range == 'Female':
    user_info_variation = data_health[data_health['gender'] == 'F']
elif age_range == 'Male':
    user_info_variation = data_health[data_health['gender'] == 'M']
elif age_range == 'Other':
    user_info_variation = data_health[data_health['gender'] == 'O']   
else:
    user_info_variation = data_health



################################################ Related link #######################################################

database_link_dict = {
    "Ironhack": "https://www.ironhack.com/de",
    "GitHub Page for Mahshid Khatami": "https://github.com/mahshid1373",
    "GitHub Page for Reetu": "",
    "GitHub Page for Faheem Khan": "https://github.com/fjkhan86",
}

st.sidebar.markdown("## Contributors Related Links")
for link_text, link_url in database_link_dict.items():
    create_st_button(link_text, link_url, st_col=st.sidebar)

#############################################################################################################################
################################################## Plot #####################################################################
#############################################################################################################################
