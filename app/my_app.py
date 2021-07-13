import streamlit as st
import numpy as np
import pandas as pd
from app_functions import login, create_user, display_all_user, create_feeling, display_feeling_by_cust
from app_functions import  *

st.sidebar.markdown("### first page")
# create_user()
login()
display_all_user()
# app.run()
create_feeling()
display_feeling_by_cust('user_id')
