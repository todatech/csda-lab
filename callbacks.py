import json
import dash
import dash_html_components as html

from dash.dependencies import Input, Output

from app import app, rec

# For Debugging

@app.callback(
   Output(component_id='element-to-hide', component_property='style'),
   [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')])

def show_hide_element(visibility_state):
    if visibility_state == 'on':
        return {'display': 'block'}
    if visibility_state == 'off':
        return {'display': 'none'}

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
    t = rec.get_movie_id_by_title(value)
    return 'You\'ve entered "{}", Clicked: "{}"'.format(t, n_clicks)


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
    t = rec.get_movie_id_by_title(title)
    return 'You\'ve entered "{}", "{}", clicked: "{}"'.format(t, userid, n_clicks)


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
    else:
        pass


# --- Lab 2 Callbacks
@app.callback(
    Output('lab2app-display-value', 'children'),
    [Input('lab2app-dropdown', 'value')])
def display_value2(value):
    return 'In Lab 2, you have selected "{}"'.format(value)
