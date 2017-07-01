# Web app to graph share prices against each other
# Extend to portfolio later

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas_datareader import data as pd_data
from datetime import datetime

app = dash.Dash('Market Price Graph')

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='TSLA'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})


@app.callback(
    Output('my-graph', 'figure'),
    [Input('my-dropdown', 'value')]
)
def update_graph(selected_dropdown_value):
    df = pd_data.DataReader(
        selected_dropdown_value,
        'google',
        datetime(2016, 1, 1),
        datetime.now()
    )

    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

if __name__ == '__main__':
    app.run_server()
