from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash()

df = pd.read_csv(r'data\merged_processed_data.csv')

fig_sales = px.line(df, x = 'date', y = 'sales', title='Sales over time')

app.layout = html.Div(children=[html.H1(children='Sales Dashboard'), 
                                html.Div(children='''Dash: A web app for Sales Visualisation'''),
                                dcc.Graph(id='sales-graph_1', figure=fig_sales)])

if __name__ == '__main__':
    app.run(debug=True, port=8050)