import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from layouts import navbar
from app import app


body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        # html.H2("Graph"),
                        # dcc.Graph(
                        #     figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        # ),
                        html.Div(
                            [
                                html.H1("Advanced Methods of Data Analysis"),
                            ], style={'textAlign':'center'}

                        ),
                        html.Br(),
                        html.Div(
                            [
                                html.Img(src='/assets/school_logo.png'), 
                            ], style={ 'textAlign': 'center', 'vertical-align': 'middle' }

                        )
                    ]
                ),                
                dbc.Col(
                    [
                        html.A(
                            html.H4("Lab 1 - Recommender System for Movies"),
                            href='/lab1'
                        ),
                        html.P(
                            """\
                            Description for Lab 1"""
                        ),
                        html.Br(),
                        html.A(
                            html.H4("Lab 2 - TBD"), 
                            href='/lab2'
                        ),
                        html.P(
                            """\
                            Description for Lab 2"""
                        ),
                        html.Br(),
                        html.A(
                            html.H4("Lab 3 - TBD"), 
                            href='/lab3'    
                        ),
                        html.P(
                            """\
                            Description for Lab 3"""
                        ),
                        # dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
            ]
        )
    ], className="mt-4",
)


def App():
    layout = html.Div([
        navbar,
        body
    ])
    return layout


if __name__ == "__main__":
    app.run_server()
