import dash

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table as dt

import lab1.movies

from app import app, rec, df
from app import rec

from layouts import navbar


genre_list = [ '', 'Drama', 'Comedy', 'Thriller', 'Romance', 'Action', 'Horror', 
                'Crime', 'Documentary', 'Adventure', 'Science Fiction', 'Family', 
                'Mystery', 'Fantasy', 'Animation', 'Music', 'Foreign', 'History',
                'War', 'Western', 'TV Movie']

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
                        html.Div(
                            [
                                dcc.Dropdown(
                                    id='debug-show-hide',
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
                        html.H4("1. Top Chart by Genre"),
                        html.P(
                            """\
                            May we suggest Top Movies that are highly acclaimed under each genre."""
                        ),
                        html.Br(),
                        html.Label(
                            'Please select a Genre of your choice (or clear for Overall Top Movies)'),
                        html.Br(),
                        dcc.Dropdown(
                            id='lab1app-tc-dropdown',
                            options=[{'label': i, 'value': i}
                                     for i in genre_list],
                            value=''
                        ),
                        dbc.Button("List Movies", id="lab1app-tc-button", color="default",
                                   style={
                                       'float': 'right'}
                                   ),
                        html.Div(
                            [
                                html.Div("Placeholder", id='lab1app-tc-display-value', )
                            ], style={'display': 'block'},
                        ), 
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        html.H4(
                            "2. Recommending Movies based on a title you've picked"),
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
                        html.Div(
                            [
                                html.Div("Placeholder", id='lab1app-cb-display-value', )
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
                        html.H4(
                            "3. Recommending Movies based on Your Previous Ratings"),
                        html.P(
                            """\
                            Please enter your UserID. We will find your rating history and will suggest titles you might like."""
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
                                                      value='2', type='number',
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
                        html.Br(),
                        html.Div(
                            [
                                html.Div("Placeholder", id='lab1app-cf-display-value'),
                            ], style={'display': 'block'}
                        ),
                        html.Div(
                            children="", id='lab1app-rating-status'
                        ),                        
                        dt.DataTable(
                            id='rating',
                            columns=[{"name": i, "id": i} for i in df.columns],
                            # data=df.to_dict('records'),
                            data=None,
                        ),

                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        html.H4("4. Based on what you are watching and what you've rated, may we suggest..."),
                        html.P(
                            """\
                            Please enter your userid and the title you are watching now, and we will suggest highly acclaimed titles you would most likely love."""
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
                                                      value='Avatar', type='text'),
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
                                                      value='2', type='number',
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
                        html.Div(
                            [
                                html.Div('Placeholder', id='lab1app-hr-display-value'),
                            ], style={'display': 'block'}
                        ),
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
                            children="", id='lab1app-status'
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
