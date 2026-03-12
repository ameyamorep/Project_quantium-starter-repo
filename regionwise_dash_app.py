from dash import dcc, html, Input, Output, callback, Dash
import plotly.express as px
import pandas as pd

app_3 = Dash()
df_3 = pd.read_csv(r'C:\Users\think\Downloads\Ameya UTS Masters\Projects\Project_quantium-starter-repo\data\merged_processed_data.csv')

app_3.layout = html.Div([
    html.H1("Regional Sales Dashboard"),
    dcc.RadioItems(
        id='region-wise-radio',
        options=['all', 'north', 'south', 'east', 'west'],
        value='all'
    ),
    dcc.Graph(id='region-wise-graph')
])

@app_3.callback(Output('region-wise-graph', 'figure'), Input('region-wise-radio', 'value'))
def update(region):
    df_region = df_3 if region == 'all' else df_3[df_3['region'] == region]
    return px.line(df_region, x='date', y='sales', color='region' if region == 'all' else None,
                   title=f'Sales - {region}')


if __name__ == '__main__':
    app_3.run(debug=True, port=8052)