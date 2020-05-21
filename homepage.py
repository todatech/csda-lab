import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


# from comp.navbar import Navbar
# nav = Navbar()
from layouts import navbar

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Advanced Methods of Data Analysis"),
                        html.Br(),
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
                dbc.Col(
                    [
                        # html.H2("Graph"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        ),
                    ]
                ),
            ]
        )
    ], className="mt-4",
)


def Homepage():
    layout = html.Div([
        navbar,
        body
    ])
    return layout


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
app.layout = Homepage()

if __name__ == "__main__":
    app.run_server()
