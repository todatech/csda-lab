import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app, kot 

from layouts import navbar

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2(
                            children="Time Series Analysis of Keywords from Google Trends",
                            style={
                                'textAlign': 'center'
                            }
                        ),
                        html.Div(
                            [
                                dcc.Dropdown(
                                    id='debug-show-hide-lab3',
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
                        html.H4("Enter a Search Term"),
                        html.P(
                            """\
                            Please enter a keyword or a phase of interest. First, \
                            we will pull time-series data using Google's API. Then, \
                            we will break down the time characteristics for that term."""
                        ),
                        html.Div(
                            [
                                dcc.Input(id='lab3app-search-term',
                                    value='diet', 
                                    type='text',
                                    style={'width': '75%'},
                                ),
                            ],
                            style=dict(display='flex', justifyContent='center'),
                            className="m-2",
                        ),
                        html.Div(
                            [
                                html.Span(
                                    id='lab3app-test-span',
                                ),
                                html.Div(
                                    [
                                        dcc.Loading(
                                            [
                                                html.Div(id="lab3app-loading1-output")
                                            ],
                                            id="lab3app-loading1", type="default",
                                        ),
                                    ],
                                    style={'margin': '30px'},
                                ),                                
                            ], 
                        ),
                        html.Br(),
                        html.Div(
                            [
                                dbc.Button("Show", id="lab3app-show", color="default",
                                    style={'float': 'right', 'display': 'none'}),
                                dbc.Button("Start Over", id="lab3app-clear", color="default",
                                    style={'float': 'right', 'display': 'block'}),
                                dbc.Button("Begin Search", id="lab3app-search", color="default",
                                    style={'float': 'right', 'display': 'block', "margin-right": "20px"}),
                            ], 
                        ), 
                    ],
                ),

            ], className="m-4",
        ),

        html.Div(
            [
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.Div(
                                    [
                                        html.H6("Trending History"),
                                        html.Img(id='lab3app-trends-img', width='500'),
                                    ],
                                )),
                                dbc.Col(html.Div(
                                    [
                                        html.H6("Rolling Average 52 Weeks"),
                                        html.Img(id='lab3app-rolling-img', width='500'),
                                    ],
                                )),
                            ], className="m-4",
                        ),

                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div(
                                    [
                                        html.H6("SARIMA Prediction"),
                                        html.Img(id='lab3app-SARIMA-pred-img', width='1000'),
                                    ],
                                )),    
                                # html.Div(
                                #     [
                                #         html.H6("ARIMA Prediction"),
                                #         html.Br(),
                                #         html.Img(id='lab3app-ARIMA-pred-img'),
                                #         html.Br(),
                                #     ],
                                # ),    
                            ], className="m-4",
                        ), 
                        
                        dbc.Row(
                            [
                                dbc.Col(html.Div(
                                    [
                                        html.H6("Seasonal Decomposition"),
                                        html.Img(id='lab3app-decomposition-img', width='500'),
                                    ],
                                )),
                                dbc.Col(html.Div(
                                    [
                                        html.H6("SARIMA diagnostics"),
                                        html.Img(id='lab3app-SARIMA-diag-img', width='500'),
                                    ],
                                )),                
                            ], className="m-4",
                        ),
                    ],
                ),
            ],
            id='lab3app-charts',
            style={'display': 'none'},
        ),
   
    ], className="mt-4",
)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

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
