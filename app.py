import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Salary predictor')

nav = st.sidebar.radio("Select module ",['Visualize Trend','Prediction','Improve our Data'])

if nav == 'Visualize Trend':
    st.write('Visualization')
elif nav == 'Prediction':
    st.write('Predict')
elif nav == 'Improve our Data':
    st.write('adding')