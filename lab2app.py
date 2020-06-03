import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table as dt

# import lab2.spammer
from app import app, spam, df

from layouts import navbar


body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2(
                            children="Spam Message Identifier",
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
                            style={'display': 'block'}
                        )
                    ], className="m-4",
                ),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("1. Sample Valid Messages"),
                        html.P(
                            """\
                            These are some of the messages that have been marked as Valid from DB."""
                        ),
                        html.Br(),
                        dt.DataTable(
                            id='ham-msg',
                            columns=[{"name": i, "id": i} for i in spam.get_sample_ham().columns],
                            data=spam.get_sample_ham().to_dict('records'),
                            style_cell={
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                                'maxWidth': 0,
                                'textAlign': 'left',
                            },
                            style_data={
                                'whiteSpace': 'normal',
                                'height': 'auto',
                            },                                    
                            css=[{
                                'selector': '.dash-spreadsheet td div',
                                'rule': '''
                                    line-height: 15px;
                                    max-height: 30px; min-height: 30px; height: 30px;
                                    display: block;
                                    overflow-y: hidden;
                                '''
                            }],
                            # data=None,
                        ),                        
                        html.Br(),
                        dbc.Button("List Valid Messages", id="lab2app-ham-button", color="default",
                                   style={
                                       'float': 'right'}
                                   ),
                        html.Div(
                            [
                                html.Div("Placeholder", id='lab2app-ham-display-value', )
                            ], style={'display': 'block'},
                        ), 
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        html.H4(
                            "2. Sample Spam Message"),
                        html.P(
                            """\
                            These are some of the messages that have been marked as SPAM from DB."""
                        ),
                        html.Br(),
                        dt.DataTable(
                            id='spam-msg',
                            # columns=[{"name": i, "id": i} for i in df.columns],
                            # data=df.to_dict('records'),
                            # data=None,
                            columns=[{"name": i, "id": i} for i in spam.get_sample_spam().columns],
                            data=spam.get_sample_spam().to_dict('records'),
                            style_cell={
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                                'maxWidth': 0,
                                'textAlign': 'left',
                            },
                            style_data={
                                'whiteSpace': 'normal',
                                'height': 'auto',
                            },                                    
                            css=[{
                                'selector': '.dash-spreadsheet td div',
                                'rule': '''
                                    line-height: 15px;
                                    max-height: 30px; min-height: 30px; height: 30px;
                                    display: block;
                                    overflow-y: hidden;
                                '''
                            }],

                        ),                        
                        html.Br(),
                        dbc.Button("List Spam Messages", id="lab2app-spam-button", color="default",
                                   style={
                                       'float': 'right'

                                   }),
                        html.Div(
                            [
                                html.Div("Placeholder", id='lab2app-spam-display-value', )
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
                        html.H4("3. Test Your Message"),
                        html.P(
                            """\
                            Type your own message below to see if the system will flag it as Spam or not."""
                        ),
                        dcc.Input(id='lab2app-user-msg',
                            value='Write Message Here...', 
                            type='text',
                            style={'width': '80%'},
                        ),
                        html.Br(),
                        html.Div(
                            [
                                html.Span(
                                    id='lab2app-spam-not-spam',
                                ),
                            ]
                        ),
                        html.Br(),
                        dbc.Button("Send Me Message", id="lab2app-msg-button", color="default",
                            style={'float': 'left'},
                        ),
                    ],
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
