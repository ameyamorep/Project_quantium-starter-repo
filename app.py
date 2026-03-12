from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

app = Dash(__name__)

# Load data relative to this file's location
data_path = os.path.join(os.path.dirname(__file__), 'data', 'data\\merged_processed_data.csv')
df = pd.read_csv(data_path)

app.layout = html.Div([
    html.H1("Regional Sales Dashboard"),
    dcc.RadioItems(
        id='region-radio',
        options=['all', 'north', 'south', 'east', 'west'],
        value='all'
    ),
    dcc.Graph(id='region-graph')
])

@app.callback(Output('region-graph', 'figure'), Input('region-radio', 'value'))
def update(region):
    d = df if region == 'all' else df[df['region'] == region]
    return px.line(d, x='date', y='sales',
                   color='region' if region == 'all' else None,
                   title=f'Sales - {region}')

if __name__ == '__main__':
    app.run(debug=True)
