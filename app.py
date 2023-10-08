import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import pickle

import streamlit as st

#reading data
df = pd.read_csv('Data/salary_data.csv')
df = df.round(2)
plt.style.use('ggplot')

st.title('Salary predictor')

# creating modules to show in sidebar
nav = st.sidebar.radio("Select module ",['Visualize Trend','Prediction','Improve our Data'])

# visualization page  or homepage
if nav == 'Visualize Trend':
    st.write('Visualization')

    # showing logo
    st.image('Data/salary.png',width = 500)

    #showing sample table
    if st.checkbox("Show sample data"):
        st.table(df.round(2).sample(5))

    # showing scatterplot
    graph = st.selectbox('Select kind of graph:',['Interactive', 'Non-interactive'])

    # adding slider for drill down
    val = st.slider('filter the vicinity of your experience: ',min_value=0,max_value=15,step=1)

    data = df.copy()
    data = df[(df['YearsExperience']>val-3) & (df['YearsExperience']<val+3)]

    # matplotlib static plot
    if graph == 'Non-interactive':
        fig,ax = plt.subplots(figsize =(10,6))
        ax.scatter(data['YearsExperience'],data['Salary'])
        ax.set_xlim(data['YearsExperience'].min()-3,data['YearsExperience'].max()+3)

        ax.set_xlabel('Years of exp')
        ax.set_ylabel('Salary')
        ax.set_title('Salary with work Exp.')
        plt.tight_layout()
        st.pyplot(fig)

    # plotly dynamic
    if graph == 'Interactive':
        fig = px.scatter(data, x='YearsExperience', y='Salary',
                         labels={'YearsExperience': 'Years of Exp', 'Salary': 'Salary'},
                         title='Salary with Work Experience')

        # Adjust the Y-axis limits based on your data range
        fig.update_yaxes(range=[data['Salary'].min(), data['Salary'].max()])

        # Show the plotly figure
        st.plotly_chart(fig)


# prediction module
elif nav == 'Prediction':
    st.header('Know your Salary')
    val = st.number_input("Enter your exp in yrs",min_value=0.0, max_value= 20.0,step=0.1)
    val = [[val]]

    # load pickle model
    with open('linear_regression_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    predicted_sal = loaded_model.predict(val)[0]

    if st.button("Predict"):
        st.success('your salary should be {}'.format(round(predicted_sal)))

# adding more data from users to training dataset
elif nav == 'Improve our Data':
    st.header('Contribute and improve our dataset')

    # take user input
    exp = st.number_input('Enter your experience in yrs(0.1 yr step): ',min_value=0.0,max_value=20.0,step=0.1)
    sal = st.number_input('Enter your salary: ',min_value=1000,max_value= 1000000,step=5000)

    if st.button("Submit"):
        to_add = {"YearsExperience":[exp],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv('Data/salary_data.csv',mode='a',header=False,index=False)
        st.success('Submitted')