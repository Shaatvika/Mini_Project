import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO

home_tab, tab1, tab2, tab3, tab4 = st.tabs(["Companies alotted","Alotted company 1","Alotted Company 2", "Alotted Company 3","Alotted Company 4"])

with home_tab:
    st.header("SUITABLE COMPANIES")
    st.write("Company 1")
    st.write("Company 2")
    st.write("Company 3")
    st.write("Company 4")

with tab1:
    st.header("Company 1")
    st.write("-------ABOUT THE COMPANY--------")
    st.write("-------POSITIONS AVAILABLE (in the preferred location-------")
    st.write("-------EXPECTED SALARY FOR EACH POSITION-------")
    st.write("-------CONTACT DETAILS (to send in resume)--------")

with tab2:
    st.header("Company 2")
    st.write("-------ABOUT THE COMPANY--------")
    st.write("-------POSITIONS AVAILABLE (in the preferred location)-------")
    st.write("-------EXPECTED SALARY FOR EACH POSITION-------")
    st.write("-------CONTACT DETAILS (to send in resume)--------")

with tab3:
    st.header("Company 3")
    st.write("-------ABOUT THE COMPANY--------")
    st.write("-------POSITIONS AVAILABLE (in the preferred location-------")
    st.write("-------EXPECTED SALARY FOR EACH POSITION-------")
    st.write("-------CONTACT DETAILS (to send in resume)--------")

with tab4:
    st.header("Company 4")
    st.write("-------ABOUT THE COMPANY--------")
    st.write("-------POSITIONS AVAILABLE (in the preferred location-------")
    st.write("-------EXPECTED SALARY FOR EACH POSITION-------")
    st.write("-------CONTACT DETAILS (to send in resume)--------")
