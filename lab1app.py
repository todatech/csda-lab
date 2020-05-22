import dash

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table as dt

import lab1.movies

from app import app, rec, df
from app import rec

from layouts import navbar

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2(
                            children="Movies Recommender System",
                            style={
                                'textAlign': 'center'
                            }
                        ),
                    ], className="m-4",
                ),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("1. Top Chart by Genre"),
                        html.P(
                            """\
                            May we suggest Top Movies that are highly acclaimed under each genres."""
                        ),
                        html.Br(),
                        html.Label(
                            'Please select a Genre of your choice (or clear for Overall Top Movies)'),
                        html.Br(),
                        dcc.Dropdown(
                            id='lab1app-tc-dropdown',
                            options=[{'label': i, 'value': i}
                                     for i in ['LA', 'NYC', 'MTL']],
                            value='LA'
                        ),
                        dbc.Button("List Movies", id="lab1app-tc-button", color="default",
                            style={
                                'float': 'right'}
                        ),
                        html.Div(id='lab1app-tc-display-value'),
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        html.H4(
                            "2. Recommended Movies based on a Similar Title you've picked"),
                        html.P(
                            """\
                            Please enter a movie title and we will suggest similar titles to you."""
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div(
                                        [
                                            html.Label('Movie Title'),
                                        ]
                                    ), width=3
                                ),
                                dbc.Col(
                                    [
                                        dcc.Input(id='lab1app-cb-title',
                                                  value='Avatar', type='text',
                                                  className="mb-3"),
                                    ]
                                ),
                            ]
                        ),
                        dbc.Button("List Movies", id="lab1app-cb-button", color="default",
                                   style={
                                       'float': 'right'

                                   }),
                        html.Div(id='lab1app-cb-display-value'),
                    ],
                    md=6,
                ),
            ],  className="m-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4(
                            "3. Recommended Movies based on Your Previous Ratings"),
                        html.P(
                            """\
                            Enter your userid and we will find your rating history and we will suggest titles you might like."""
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div(
                                        [
                                            html.Label('UserID'),
                                        ]
                                    ), width=3
                                ),
                                dbc.Col(
                                    html.Div(
                                        [
                                            dcc.Input(id='lab1app-cf-userid',
                                                      value='1', type='number',
                                                      min=0, step=1),
                                        ],
                                        id="styled-numeric-input",
                                    ),
                                ),
                            ]
                        ),
                        dbc.Button("List Movies", id="lab1app-cf-button", color="default",
                                   style={
                                       'float': 'right'}
                                   ),
                        html.Div(id='lab1app-cf-display-value'),
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        html.H4("4. Based on what you are watching, we suggest"),
                        html.P(
                            """\
                            Enter your userid and title you are watching now, and we will suggest highly acclaimed titles you most likely would love."""
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div(
                                        [
                                            html.Label('Movie Title'),
                                        ]
                                    ), width=3
                                ),
                                dbc.Col(
                                    html.Div(
                                        [
                                            dcc.Input(id='lab1app-hr-title',
                                                      value='Batman', type='text'),
                                        ]
                                    )
                                ),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div(
                                        [
                                            html.Label('UserID'),
                                        ]
                                    ), width=3
                                ),
                                dbc.Col(
                                    html.Div(
                                        [
                                            dcc.Input(id='lab1app-hr-userid',
                                                      value='1', type='number',
                                                      min=0,
                                                      step=1),
                                        ],
                                        id="styled-numeric-input",
                                    ),
                                ),
                            ]
                        ),
                        html.Br(),
                        dbc.Button("List Movies", id="lab1app-hr-button", color="default",
                                   style={'float': 'right'}),
                        html.Div(id='lab1app-hr-display-value'),

                    ],
                    md=6,
                ),
            ], className="m-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4(
                            children="Movies Recommendations",
                        ),
                        html.Div(
                            children="Hello, This is the result.", id='testp'
                        ),
                        dt.DataTable(
                            id='table',
                            columns=[{"name": i, "id": i} for i in df.columns],
                            # data=df.to_dict('records'),
                            data=None,
                        ),

                    ]
                ),
            ], className="m-4",
        ),
    ], className="mt-4",
)


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# body = html.Div(style={'backgroundColor': colors['background']}, children=[
#     html.H1(
#         children='Lab 1 Dash',
#         style={
#             'textAlign': 'center',
#             'color': colors['text']
#         }
#     ),
#     dcc.Dropdown(
#         id='lab1app-dropdown',
#         options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
#         value='LA'
#     ),
#     html.Div(id='lab1app-display-value')
# ])


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
