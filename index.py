# dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# apps
from app import app
from layouts import navbar
import callbacks

from homepage import Homepage
import lab1app
import lab2app
import lab3app

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/lab1':
        # layout = html.Div([
        #     navbar,
        #     lab1app.body
        # ])
        # return layout
        return lab1app.App()
    elif pathname == '/lab2':
        layout = html.Div([
            navbar,
            lab2app.body
        ])
        return layout
        # return lab2app.App()
    elif pathname == '/lab3':
        layout = html.Div([
            navbar,
            lab3app.body
        ])
        return layout
        # return lab3app.App()
    # elif pathname == '/time-series':
    #    return testapp.App()
    else:
        return Homepage()


# @app.callback(
#     Output('output', 'children'),
#     [Input('pop_dropdown', 'value')]
# )
# def update_graph(city):
#     graph = testapp.build_graph(city)
#     return graph


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050)
