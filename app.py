import dash
import dash_bootstrap_components as dbc
from lab1.movies import Recommender


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
app.config.suppress_callback_exceptions = True

# Lab 1
rec = Recommender()

# For Production only - save ML model to disk after calcluation
# faster server reload time
# rec.load_ml_objects()

# For Production only - DO NOT SAVE ML model to disk, calculate and load into memory
# save memory when loading
rec.start_recommender_engine()

df = rec.get_sample_df()