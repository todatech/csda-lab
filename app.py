import dash
import flask
import dash_bootstrap_components as dbc
from lab1.movies import Recommender

server = flask.Flask(__name__) # define flask app.server

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED], server=server)
app.config.suppress_callback_exceptions = True

# run following in command to load gunicorn server
# gunicorn app:app.server -b :8050 -c gunicorn.py

# Lab 1
rec = Recommender()

# For Production only - save ML model to disk after calcluation
# faster server reload time
# rec.load_ml_objects()

# For Production only - DO NOT SAVE ML model to disk, calculate and load into memory
# save memory when loading
rec.start_recommender_engine()

df = rec.get_sample_df()