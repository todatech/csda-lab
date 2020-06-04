# dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# apps
from app import app, server
from layouts import navbar
import callbacks

import homepage
import lab1app
import lab2app
import lab3app
import settingsapp
from layouts import layout1


app.layout = html.Div([
   dcc.Location(id='url', refresh=False),
   html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
   if pathname == '/lab1':
      return lab1app.App()
   elif pathname == '/lab2':
      return lab2app.App()
   elif pathname == '/lab3':
      return lab3app.App()
   elif pathname == '/settings':
      return settingsapp.App()
   elif pathname == '/layout1':
      layout = html.Div([
        navbar,
        layout1
      ])
      return layout
    # elif pathname == '/time-series':
    #    return testapp.App()
   else:
     return homepage.App()


if __name__ == "__main__":
   # For Testing only
   app.run_server(host='0.0.0.0', debug=True, port=8050)
   # For Production only
   # app.run_server(host='0.0.0.0', use_reloader=False, port=8050)
