import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from layouts import navbar

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

body = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Lab 1 Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Dropdown(
        id='lab1app-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='lab1app-display-value')
])

def App():
    layout = html.Div([
        navbar,
        body
    ])
    return layout

if __name__ == "__main__":
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
    app.layout = App()
    app.run_server()
