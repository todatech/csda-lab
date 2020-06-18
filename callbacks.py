import json
import dash
import dash_html_components as html
import time

from dash.dependencies import Input, Output

from app import app, rec, spam, sti
from app import kot

# --- Lab 1 Callbacks
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

# ----------------- Button Clicked and Table Processing ------------------
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
# --------------------- Input Testing --------------------------
# Ham Message
@app.callback(
    Output('lab2app-ham-display-value', 'children'),
    [
        Input('lab2app-ham-button', 'n_clicks'),
    ],
)
def update_lab2_tc(n_clicks):
    return 'You\'ve clicked: "{}"'.format(n_clicks)

# Spam Message
@app.callback(
    Output('lab2app-spam-display-value', 'children'),
    [
        Input('lab2app-spam-button', 'n_clicks'),
    ],
)
def update_lab2_cb(n_clicks):
    return 'You\'ve clicked: "{}"'.format(n_clicks)


# ----------------- Button Clicked and Table Processing ------------------
@app.callback(
    [
        Output('ham-msg', 'data'),
        Output('spam-msg', 'data'),
        Output('lab2app-spam-not-spam', 'children')
    ],
    [
        #buttons
        Input('lab2app-ham-button', 'n_clicks'),
        Input('lab2app-spam-button', 'n_clicks'),
        Input('lab2app-msg-button', 'n_clicks'),
        Input('lab2app-user-msg', 'value')
    ],
)
def update_msg(btn1, btn2, btn3, user_msg):

    # See Dash Advanced callbacks
    # https://dash.plotly.com/advanced-callbacks

    ctx = dash.callback_context

    ham_msg_table = None
    spam_msg_table = None    
    msg = ''
    spam_id_msg = ''
    sti_msg = ''

    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]


    if button_id == 'lab2app-ham-button':
        ham_msg_table = spam.get_sample_ham().to_dict('records')
    elif button_id == 'lab2app-spam-button':
        spam_msg_table = spam.get_sample_spam().to_dict('records')
    elif button_id == 'lab2app-msg-button':
        result = spam.identify_message(user_msg)
        result2 = sti.predict(user_msg)

        # Unpacking spam engine results
        a = result.tolist()
        if a[0]:
            spam_id_msg = 'Your message seems like a SPAM to me...'
        else:
            spam_id_msg = 'Your message seems OK to me...'
        #msg = user_msg

        # Unpacking sentiment engine results
        if result2['label'] == 'POSITIVE':
            sti_msg = 'You sound POSITIVE to me'
        elif result2['label'] == 'NEGATIVE':
            sti_msg = 'You sound NEGATIVE to me'
        elif result2['label'] == 'NEUTRAL':
            sti_msg = 'You seem NEUTRAL with your topic'
        else:
            pass

        msg = sti_msg + ' and ' + spam_id_msg

    else:
        pass

    return [ham_msg_table, spam_msg_table, msg]

# For Debugging - Lab 2
@app.callback(
    [
        Output('lab2app-ham-display-value', 'style'),
        Output('lab2app-spam-display-value', 'style'),
    ],
    [
        Input('debug-show-hide-lab2', 'value'),
    ],
)
def show_hide_element_lab2(value):
    result = {}

    if value == 'on':
        result = {'display': 'block'}
    if value == 'off':
        result = {'display': 'none'}

    return result, result, 



# --- Settings Page Callbacks
# --------------------- Input Testing --------------------------
# lab1 button
@app.callback(
    Output('settings-lab1-display-value', 'children'),
    [
        Input('settings-lab1-button', 'n_clicks'),
    ],
)
def update_settings_lab1_tc(n_clicks):
    return 'You\'ve clicked: "{}"'.format(n_clicks)

# lab2 button
@app.callback(
    Output('settings-lab2-display-value', 'children'),
    [
        Input('settings-lab2-button', 'n_clicks'),        
    ],
)
def update_settings_lab2_tc(n_clicks):
    return 'You\'ve clicked: "{}"'.format(n_clicks)

# lab3 button
@app.callback(
    Output('settings-lab3-display-value', 'children'),
    [
        Input('settings-lab3-button', 'n_clicks'),
    ],
)
def update_settings_lab3_tc(n_clicks):
    return 'You\'ve clicked: "{}"'.format(n_clicks)

# General Setting Buttons
@app.callback(
    Output('settings-gen-display-value', 'children'),
    [
        Input('settings-gen-button', 'n_clicks'),
    ],
)
def update_settings_gen_tc(n_clicks):
    return 'You\'ve clicked: "{}"'.format(n_clicks)

# ----------------- Button Clicked and Table Processing ------------------
@app.callback(
    Output("settings-lab1-loading1-output", "children"),
    [
        Input("settings-lab1-button", "n_clicks"),
        Input('settings-lab1-button2', 'n_clicks'),
        Input('settings-lab1-button3', 'n_clicks'),        
    ],
)
def settings_lab1_engine(btn1, btn2, btn3):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'settings-lab1-button':
        # time.sleep(1)
        rec.start_recommender_engine()
        return 'Load Engine Completed'
    elif button_id == 'settings-lab1-button2':
        # time.sleep(1)
        return 'Disabled Function'
    elif button_id == 'settings-lab1-button3':
        return 'Disabled Function'
    else:
        pass

# For Debugging - General Settings
@app.callback(
    [
        Output('settings-lab1-display-value', 'style'),
        Output('settings-lab2-display-value', 'style'),
        Output('settings-lab3-display-value', 'style'),
        Output('settings-gen-display-value', 'style'),
    ],
    [
        Input('debug-show-hide-lab2', 'value'),
    ],
)
def show_hide_element_settings(value):
    result = {}

    if value == 'on':
        result = {'display': 'block'}
    if value == 'off':
        result = {'display': 'none'}

    return result, result, result, result,

# --- Lab 3 Callbacks
# ------------------- Processing Graphic ------------------
@app.callback(
    [
        Output('lab3app-test-span', 'children'),
        Output('lab3app-trends-img', 'src'),
        Output('lab3app-rolling-img', 'src'),
        Output('lab3app-decomposition-img', 'src'),
        Output('lab3app-SARIMA-diag-img', 'src'),
        Output('lab3app-SARIMA-pred-img', 'src'),
        # Output('lab3app-ARIMA-pred-img', 'src'),
    ],
    [
        Input('lab3app-search', 'n_clicks'),
        Input('lab3app-clear', 'n_clicks'),
        Input('lab3app-search-term', 'value'),
    ]
)
def update_graphs(btn1, btn2, kw):

    ctx = dash.callback_context

    trend_img = ''
    rolling_img = ''
    decompose_img = ''
    sarima_diag_img = ''
    sarima_pred_img = ''
    arima_pred_img = ''
    test_txt = ''

    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'lab3app-search':
        kot.start_search(kw)
        # test_txt = kw
        # test_txt = 'Search Button Clicked'
        trend_img = kot.show_time_series_plot_in_html()
        rolling_img = kot.show_rolling_average_plot_in_html()
        decompose_img = kot.show_decomposition_plot_in_html()
        sarima_diag_img = kot.show_SARIMA_diagnostics_plot_in_html()
        sarima_pred_img = kot.show_SARIMA_prediction_plot_in_html()
        # arima_pred_img = kot.show_ARIMA_prediction_plot_in_html()

    elif button_id == 'lab3app-clear':
        test_txt = 'Clear Button Clicked'
    else:
        pass
    
    return test_txt, trend_img, rolling_img, decompose_img, sarima_diag_img, sarima_pred_img, #arima_pred_img, 
