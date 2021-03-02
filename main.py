import pandas as pd 
import plotly.express as px

dataF = pd.read_csv('Copy+of+data+-+data.csv')

graph = px.scatter(dataF,x='date',y='cases', color='country')


graph.show()