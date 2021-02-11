# Find the International Space Station Current Location
# From Python Programmer YouTube Channel

import pandas as pd 
import plotly.express as px

# api de localização
url = 'http://api.open-notify.org/iss-now.json'

# leitura arquivo Json
df = pd.read_json(url)

# formatação das informações
df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)

# Exclusão colunas index e message
df = df.drop(['index', 'message'], axis=1)

# Criação do mapa e localização da ISS
fig = px.scatter_geo(df, lat='latitude', lon='longitude')

fig.show()