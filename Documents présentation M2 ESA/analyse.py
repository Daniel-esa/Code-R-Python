# Importing Necessary Python libraries
import pandas as pd
#print("get working directory", pd.__file__)

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# set new working directory as current working directory
import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# reading the data
data = pd.read_csv('Netflix-Subscriptions.csv')
print(data.head())

data['Time Period'] = pd.to_datetime(data['Time Period'], 
                                     format='%d/%m/%Y')
print(data.head())

fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Time Period'],
                         y=data['Subscribers'],
                         mode='lines', name='Subscribers'))
fig.update_layout(title='Netflix Quarterly Growth in Subscriptions',
                  xaxis_title='Date',
                  yaxis_title='Netflix Subscriptions')
fig.show()

# Calculate the quarterly growth rate
data['Quarterly Growth Rate'] = data['Subscribers'].pct_change() * 100

# Create a new column for bar color (green for positive growth, red for negative growth)
data['Bar Color'] = data['Quarterly Growth Rate'].apply(lambda x: 'green' if x > 0 else 'red')

# Plot the quarterly growth rate using bar graphs
fig = go.Figure()
fig.add_trace(go.Bar(
    x=data['Time Period'],
    y=data['Quarterly Growth Rate'],
    marker_color=data['Bar Color'],
    name='Quarterly Growth Rate'
))
fig.update_layout(title='Netflix Quarterly Subscriptions Growth Rate',
                  xaxis_title='Time Period',
                  yaxis_title='Quarterly Growth Rate (%)')
fig.show()
print("fichier A en cours d'édition avec un a majuscule...")
# Calculate the yearly growth rate
data['Year'] = data['Time Period'].dt.year
yearly_growth = data.groupby('Year')['Subscribers'].pct_change().fillna(0) * 100
print("fichier A en cours d'édition avec un a majuscule...")
# Create a new column for bar color (green for positive growth, red for negative growth)
data['Bar Color'] = yearly_growth.apply(lambda x: 'green' if x > 0 else 'red')
print("fichier A en cours d'édition avec un a majuscule...")
# Plot the yearly subscriber growth rate using bar graphs
fig = go.Figure()
fig.add_trace(go.Bar(
    x=data['Year'],
    y=yearly_growth,
    marker_color=data['Bar Color'],
    name='Yearly Growth Rate'
))
print("fichier A en cours de modification pour créer un conflit")
print("fichier AAA en cours de modification pour créer un conflit")
fig.update_layout(title='Netflix Yearly Subscriber Growth Rate',
                  xaxis_title='Year',
                  yaxis_title='Yearly Growth Rate (%)',
                  xaxis=dict(dtick=1))
fig.show()
print("fichier A en cours d'édition avec un a majuscule...")
# Crer automatiquement un fichier requireents pour les dépendances:
# pipreqs . --encoding=utf-8 --force --ignore .venv --mode no-pin
# Mais la bonne pratique est plutot de créer un fichier toml. 
# On peut leur dire qu'il ya la vieille école --> requierements
# et mtn les toml