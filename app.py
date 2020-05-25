import dash
import flask
import dash_bootstrap_components as dbc
from lab1.movies import Recommender


# ------------- General Startup -----------------------
# 
server = flask.Flask(__name__) # define flask app.server

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED], server=server)
app.config.suppress_callback_exceptions = True

# run following in command to load gunicorn server
# gunicorn index:server -b :8050 -c gunicorn.py 


# -------------- Lab 1 -------------------------------
# affixing a recommender object that is visible to the whole project
rec = Recommender()

# You can stop loading ML objects inside the recommender engine by
# commenting out the following two lines of code. THIS WILL HELP
# TO MINIMUM startup time from 3 minutes to few seconds startup time.

# For Production only - save ML model to disk after calcluation
# faster server reload time by loading only the data file
# Note: requires a lot of memory and disk space. NOT recommended.
# rec.load_ml_objects()

# For Production only - NOT TO SAVE ML model to disk, calculate 
# and load into memory ON THE FLY
rec.start_recommender_engine()

# Dummy df 
df = rec.get_sample_df()