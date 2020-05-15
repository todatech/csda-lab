# dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# apps
from homepage import Homepage
import testapp
import lab1app
import lab2app
import lab3app

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/time-series':
        return testapp.App()
    elif pathname == '/lab1':
        return lab1app.App()
    elif pathname == '/lab2':
        return lab2app.App()
    elif pathname == '/lab3':
        return lab3app.App()
    else:
        return Homepage()


@app.callback(
    Output('output', 'children'),
    [Input('pop_dropdown', 'value')]
)
def update_graph(city):
    graph = testapp.build_graph(city)
    return graph


if __name__ == "__main__":
    server = app.run_server(host='0.0.0.0', port=8050)
