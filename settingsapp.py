import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table as dt

# import lab2.spammer
from app import app, spam, df, rec

from layouts import navbar


def App():

    if rec.cosine_similarity_matrix is None:
        lab1EngineStatus = html.P(["Engine is not loaded. Please load engine..."])
    else:
        lab1EngineStatus = html.P(["Engine is loaded."])
            
    body = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2(
                                children="Settings for All Apps",
                                style={
                                    'textAlign': 'center'
                                }
                            ),
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        id='debug-show-hide-lab2',
                                        options=[
                                            {'label': 'Debug - Show element',
                                                'value': 'on'},
                                            {'label': 'Debug - Hide element',
                                                'value': 'off'}
                                        ],
                                        value='off'
                                    ),
                                ],
                                # for debugging 'block' = enable, 'none' = disable
                                style={'display': 'none'}
                            )
                        ], className="m-4",
                    ),
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Lab 1 Settings"),                       
                            html.P(
                                """\
                                To load recommender engine, it will take about 3-5 minutes and require 16G of RAM!"""
                            ),
                            html.Br(),
                            lab1EngineStatus, 
                            html.Br(),
                            dcc.Loading(
                                [
                                    html.Div(id="settings-lab1-loading1-output")
                                ],
                                id="settings-lab1-loading1", type="default",
                            ),
                            html.Br(),
                            dbc.Button("Load Engine", id="settings-lab1-button", color="default",
                                    style={
                                        
                                        'display': 'block',}
                                    ),
                            dbc.Button("Unload Engine", id="settings-lab1-button2", color="default",
                                    style={
                                        'display': 'none',
                                        }
                                    ),
                            dbc.Button("Check Engine", id="settings-lab1-button3", color="default",
                                    style={
                                        'display': 'none',
                                        }
                                    ),
                            html.Div(
                                [
                                    html.Div("Placeholder", id='settings-lab1-display-value', )
                                ], style={'display': 'block'},
                            ), 

                        ],
                        md=6,
                    ),
                    dbc.Col(
                        [
                            html.H4("Lab 2 Settings"),
                            html.Br(),
                            dbc.Button("Lab2", id="settings-lab2-button", color="default",
                                    style={
                                        'float': 'right'

                                    }),
                            html.Div(
                                [
                                    html.Div("Placeholder", id='settings-lab2-display-value', )
                                ], style={'display': 'block'},
                            ),
                        ],
                        md=6,
                    ),
                ],  className="m-4",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Lab 3 Settings"),
                            html.Br(),
                            dbc.Button("Lab3", id="settings-lab3-button", color="default",
                                    style={
                                        'float': 'right'}
                                    ),
                            html.Div(
                                [
                                    html.Div("Placeholder", id='settings-lab3-display-value', )
                                ], style={'display': 'block'},
                            ), 
                        ],
                        md=6,
                    ),
                    dbc.Col(
                        [
                            html.H4("General Settings"),
                            html.Br(),
                            dbc.Button("General", id="settings-gen-button", color="default",
                                    style={
                                        'float': 'right'

                                    }),
                            html.Div(
                                [
                                    html.Div("Placeholder", id='settings-gen-display-value', )
                                ], style={'display': 'block'},
                            ),
                        ],
                        md=6,
                    ),
                ],  className="m-4",
            ),
        ], className="mt-4",
    )

    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }

    layout = html.Div([
        navbar,
        body
    ])
    return layout


if __name__ == "__main__":
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
    app.layout = App()
    app.run_server()
