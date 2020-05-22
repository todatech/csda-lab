import json
import dash
import dash_html_components as html

from dash.dependencies import Input, Output

from app import app, rec


# --- Lab 1 Callbacks
# Top Chart
@app.callback(
    Output('lab1app-tc-display-value', 'children'),
    [
        Input('lab1app-tc-dropdown', 'value'),
        Input('lab1app-tc-button', 'n_clicks'),
    ],
)
def update_tc(value, n_clicks):
    return 'You\'ve entered "{}", Clicked: "{}"'.format(value, n_clicks)


# Content Based
@app.callback(
    Output('lab1app-cb-display-value', 'children'),
    [
        Input('lab1app-cb-title', 'value'),
        Input('lab1app-cb-button', 'n_clicks'),
    ],
)
def update_cb(value, n_clicks):
    return 'You\'ve entered "{}", Clicked: "{}"'.format(value, n_clicks)


# Collaborative Filtering
@app.callback(
    Output('lab1app-cf-display-value', 'children'),
    [
        Input('lab1app-cf-userid', 'value'),
        Input('lab1app-cf-button', 'n_clicks'),
    ]
)
def update_cf(value, n_clicks):
    #df = rec.get_sample_df2()
    return 'You\'ve entered "{}", clicked: "{}"'.format(value, n_clicks)


# Hybrid Filtering
@app.callback(
    Output('lab1app-hr-display-value', 'children'),
    [
        Input('lab1app-hr-title', 'value'),
        Input('lab1app-hr-userid', 'value'),
        Input('lab1app-hr-button', 'n_clicks'),

    ],
)
def update_hr(title, userid, n_clicks):
    return 'You\'ve entered "{}", "{}", clicked: "{}"'.format(title, userid, n_clicks)


@app.callback(
    # Output('testp', 'children'),
    Output('table', 'data'),
    [
        Input('lab1app-tc-button', 'n_clicks'),
        Input('lab1app-cb-button', 'n_clicks'),
        Input('lab1app-cf-button', 'n_clicks'),
        Input('lab1app-hr-button', 'n_clicks'),
    ]
)
def update_p(btn1, btn2, btn3, btn4):

    # See Dash Advanced callbacks
    # https://dash.plotly.com/advanced-callbacks

    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'lab1app-tc-button':
        return None
    elif button_id == 'lab1app-cb-button':
        return rec.get_sample_df().to_dict('records')
    elif button_id == 'lab1app-cf-button':
        return rec.get_sample_df2().to_dict('records')
    elif button_id == 'lab1app-hr-button':
        return rec.get_sample_df3().to_dict('records')


# --- Lab 2 Callbacks
@app.callback(
    Output('lab2app-display-value', 'children'),
    [Input('lab2app-dropdown', 'value')])
def display_value2(value):
    return 'In Lab 2, you have selected "{}"'.format(value)
