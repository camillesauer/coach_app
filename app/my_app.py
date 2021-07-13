import streamlit as st
import numpy as np
import pandas as pd
from app_functions import login, app1, app2, create_user

st.sidebar.markdown("### first page")
create_user()
login()
# app.run()

