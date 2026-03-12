from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

df_2 = pd.read_csv(r'C:\Users\think\Downloads\Ameya UTS Masters\Projects\Project_quantium-starter-repo\data\merged_processed_data.csv')
app_2 = Dash()

fig_quantity = px.line(df_2, x = 'date', y = 'quantity', title='Quantity sold over time')

app_2.layout = html.Div(children=[html.H1(children='Quantity Dashboard'), 
                                   html.Div(children='''Dash: A web app for Quantity sold Visualisation'''),
                                   dcc.Graph(id='quantity-graph_1', figure=fig_quantity)])

if __name__ == '__main__':
    app_2.run(debug=True, port=8051)