import json
import dash
import dash_html_components as html

from dash.dependencies import Input, Output

from app import app, rec


# --- Lab 1 Callbacks
# --------------------- Input Testing --------------------------
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
    #t = rec.get_movie_id_by_title(value)
    t = ''
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
    [
        Output('table', 'data'),
        Output('lab1app-status', 'children'),
        Output('rating', 'data'),
        Output('lab1app-rating-status', 'children'),
    ],
    [
        #buttons
        Input('lab1app-tc-button', 'n_clicks'),
        Input('lab1app-cb-button', 'n_clicks'),
        Input('lab1app-cf-button', 'n_clicks'),
        Input('lab1app-hr-button', 'n_clicks'),

        Input('lab1app-tc-dropdown', 'value'),

        Input('lab1app-cb-title', 'value'),
        Input('lab1app-cf-userid', 'value'),

        Input('lab1app-hr-userid', 'value'),
        Input('lab1app-hr-title', 'value'),
    ],
)
def update_p(btn1, btn2, btn3, btn4, tc, cb, cf, hr_uid, hr_title):

    # See Dash Advanced callbacks
    # https://dash.plotly.com/advanced-callbacks

    ctx = dash.callback_context

    table = None
    rating_table = None    
    status = ''
    rating_status = ''

    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]


    if button_id == 'lab1app-tc-button':
        table = rec.list_topchart(tc).head(10).to_dict('records')
    elif button_id == 'lab1app-cb-button':
        c = rec.get_movie_id_by_title(cb)
        if not len(c):
            # print("nothing")
            status = 'Cannot find your movie title in the database'
        else:
            # print("something")
            table = rec.list_cb_recommender_by_title(cb).head(10).to_dict('records')
    elif button_id == 'lab1app-cf-button':
        # table = rec.list_topchart(tc).head(10).to_dict('records')
        #rating_table = rec.get_sample_df2().to_dict('records')
        table = rec.list_cf_recommender_by_uid(cf).head(10).to_dict('records')
        rating_table =rec.list_cf_user_rated_list_by_uid(cf).head(10).to_dict('records')
        rating_status = 'Based on your rating history:'
    elif button_id == 'lab1app-hr-button':
        c = rec.get_movie_id_by_title(hr_title)
        if not len(c):
            # print("nothing")
            status = 'Cannot find your movie title in the database'
        else:
            # print("something")
            table = rec.list_hybrid_recommender(hr_uid, hr_title).head(10).to_dict('records')
    else:
        pass

    return [table, status, rating_table, rating_status, ]

# For Debugging
@app.callback(
    [
        Output('lab1app-tc-display-value', 'style'),
        Output('lab1app-cb-display-value', 'style'),
        Output('lab1app-cf-display-value', 'style'),
        Output('lab1app-hr-display-value', 'style'),
    ],
    [
        Input('debug-show-hide', 'value'),
    ],
)
def show_hide_element(value):
    result = {}

    if value == 'on':
        result = {'display': 'block'}
    if value == 'off':
        result = {'display': 'none'}

    return result, result, result, result, 


# --- Lab 2 Callbacks
@app.callback(
    Output('lab2app-display-value', 'children'),
    [Input('lab2app-dropdown', 'value')])
def display_value2(value):
    return 'In Lab 2, you have selected "{}"'.format(value)
