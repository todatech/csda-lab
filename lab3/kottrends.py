import logging
import pickle

import string

import numpy as np
import pandas as pd

import io
import os
import base64


# pytrends -- Google Trends API
from pytrends.request import TrendReq


# Scikit-learn
from sklearn.metrics import mean_squared_error

# Stats Models
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from pylab import rcParams
import statsmodels.api as sm

# graphing
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight') 
#%matplotlib inline

import seaborn as sns


# logger for displaying object builiding status on server
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------- static variables ------------------------
# DATASET
TRAIN_SIZE = 0.8

# GRAPH
GRAPH_PARAMS_FIGSIZE = (20,10)
GRAPH_PARAMS_LINEWIDTH = 5
GRAPH_PARAMS_FONTSIZE = 20

# TIME SERIES CONSTANTS
ROLLING_AVG = 52  ### WEEKS

# ARIMA P, d, Q
ARIMA_ORDER =(5, 1, 0)

# ARIMA/SARIMA - Trends P D Q
# SARIMA - Seasonal p d q
SARIMA_ORDER = (1, 1, 1)
SARIMA_SEASONAL_ORDER = (1, 1, 0, 52)
SARIMA_PREDICTION_STEPS = 104


def get_file_path(path):
    this_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(this_path, path)

def plt_to_html(plt):
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    data = base64.b64encode(buf.getbuffer()).decode("utf8") # encode to html elements
    return "data:image/png;base64,{}".format(data)

# KeywordOverTimeTrends Class
class KeywordOverTimeTrends:
    '''KeywordOverTimeTrends
    This class library will try to dissect time information for a given keyword.
    By extracting time series data from google trend for a particular keyword,
    we wish to learn about the time characteristics of this keyword and to see
    if there is any seasonal or trends with such keyword.
    '''

    def __init__(self):
        plt.switch_backend('Agg')
        # matplotlib.use('agg')

        self.pytrends = TrendReq()
        self.keyword = None
        self.df = None 
        self.smodel = None
        self.sresult = None
        self.amodel = None
        self.aresult = None

    def start_search(self, keyword):
        self.keyword = keyword
        log_msg = 'starting keyword search for:' + self.keyword
        logger.info(log_msg)
        self.get_pytrend_data()
        self.clean_df()
        logger.info('building SARIMA...')
        self.build_SARIMA()
        # logger.info('building ARIMA...')
        # self.build_ARIMA()
        # logger.info('finish computing kot analysis!')

    def get_pytrend_data(self):
        self.pytrends.build_payload(kw_list=[self.keyword])
        self.df = self.pytrends.interest_over_time()

    def get_test_data(self, n=5):
        return self.df.sample(n)

    def clean_df(self):
        self.df.drop(['isPartial'], axis=1, inplace=True)
        self.df.index.freq = 'W'
        # Use the above instead of resampling it, which takes time.
        # self.df = self.df.resample('W').mean()

    def show_time_series_plot(self):
        self.df.plot(figsize=GRAPH_PARAMS_FIGSIZE, linewidth=GRAPH_PARAMS_LINEWIDTH, fontsize=GRAPH_PARAMS_FONTSIZE)
        plt.xlabel('Year', fontsize=GRAPH_PARAMS_FONTSIZE)
        return plt

    def show_time_series_plot_in_html(self):
        return plt_to_html(self.show_time_series_plot())

    def show_rolling_average_plot(self):
        self.df.rolling(ROLLING_AVG).mean().plot(figsize=GRAPH_PARAMS_FIGSIZE, linewidth=GRAPH_PARAMS_LINEWIDTH, fontsize=GRAPH_PARAMS_FONTSIZE)
        plt.xlabel('Year', fontsize=GRAPH_PARAMS_FONTSIZE)
        plt.legend(['Rolling Avg 52wks'])
        return plt

    def show_rolling_average_plot_in_html(self):
        return plt_to_html(self.show_rolling_average_plot())

    def show_first_order_diff_plot(self):
        self.df.diff().plot(figsize=GRAPH_PARAMS_FIGSIZE, linewidth=GRAPH_PARAMS_LINEWIDTH, fontsize=GRAPH_PARAMS_FONTSIZE)
        plt.xlabel('Year', fontsize=GRAPH_PARAMS_FONTSIZE)
        return plt
    
    def show_first_order_diff_plot_in_html(self):
        return plt_to_html(self.show_first_order_diff_plot())

    def show_autocorrelation_plot(self):
        return pd.plotting.autocorrelation_plot(self.df)
    
    def show_autocorrelation_plot_in_html(self):
        return plt_to_html(self.show_autocorrelation_plot())
    
    def show_decomposition_plot(self):
        rcParams['figure.figsize'] = 12, 10
        decomposition = sm.tsa.seasonal_decompose(self.df, model='additive')
        # fig = decomposition.plot()
        decomposition.plot()
        # plt.show();
        return plt
    
    def show_decomposition_plot_in_html(self):
        return plt_to_html(self.show_decomposition_plot())

    def build_SARIMA(self):
        self.smodel = sm.tsa.statespace.SARIMAX(self.df,
                                order=SARIMA_ORDER,
                                seasonal_order=SARIMA_SEASONAL_ORDER,
                                enforce_stationarity=False,
                                enforce_invertibility=False)
        self.sresult = self.smodel.fit()
        # print(results.summary().tables[1])

    def show_SARIMA_diagnostics_plot(self):
        self.sresult.plot_diagnostics(figsize=GRAPH_PARAMS_FIGSIZE)
        return plt

    def show_SARIMA_diagnostics_plot_in_html(self):
        return plt_to_html(self.show_SARIMA_diagnostics_plot())

    def show_SARIMA_prediction_plot(self):
        pred_uc = self.sresult.get_forecast(steps=SARIMA_PREDICTION_STEPS)
        pred_ci = pred_uc.conf_int()
        ax = self.df.plot(label='Observed', figsize=GRAPH_PARAMS_FIGSIZE)
        pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
        ax.fill_between(pred_ci.index,
                        pred_ci.iloc[:, 0],
                        pred_ci.iloc[:, 1], color='k', alpha=.25)
        ax.set_xlabel('Year')
        ax.set_ylabel(self.keyword)
        plt.legend()
        #plt.show()
        return plt
    
    def show_SARIMA_prediction_plot_in_html(self):
        return plt_to_html(self.show_SARIMA_prediction_plot())

    def clear_all_plots(self):
        plt.close('all')
    
    # def build_ARIMA(self):
    #     # fit model
    #     self.amodel = ARIMA(self.df, order=ARIMA_ORDER)
    #     self.aresult = self.amodel.fit(disp=0)
    #     # print(model_fit.summary())
    #     # plot residual errors
    #     # residuals = pd.DataFrame(model_fit.resid)
    #     # print(residuals.describe())
        
    # def show_ARIMA_prediction_plot(self):
    #     X = self.df.values
    #     size = int(len(X) * 0.66)
    #     train, test = X[0:size], X[size:len(X)]
    #     history = [x for x in train]
    #     predictions = list()
    #     #my_order = (5, 1, 0)
    #     #my_order = (1, 0, 1)
    #     for t in range(len(test)):
    #         model = ARIMA(history, order=ARIMA_ORDER)
    #         model_fit = model.fit(disp=0)
    #         output = model_fit.forecast()
    #         yhat = output[0]
    #         predictions.append(yhat)
    #         obs = test[t]
    #         history.append(obs)
    #         print('predicted=%f, expected=%f' % (yhat, obs))
    #     error = mean_squared_error(test, predictions)
    #     print('Test MSE: %.3f' % error)

    #     # plt.plot(test)
    #     # plt.plot(predictions, color='red')
    #     test.plot()
    #     predictions.plot(color='red')
    #     plt.legend 
    #     # plt.show()
    #     return plt
    
    # def show_ARIMA_prediction_plot_in_html(self):
    #     return plt_to_html(self.show_ARIMA_prediction_plot())
    
