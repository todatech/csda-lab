from dash.dependencies import Input, Output

from app import app

@app.callback(
    Output('lab1app-display-value', 'children'),
    [Input('lab1app-dropdown', 'value')])
def display_value(value):
    return 'In Lab 1, you have selected "{}"'.format(value)

@app.callback(
    Output('lab2app-display-value', 'children'),
    [Input('lab2app-dropdown', 'value')])
def display_value2(value):
    return 'In Lab 2, you have selected "{}"'.format(value)