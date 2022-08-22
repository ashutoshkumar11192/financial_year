from dateutil.relativedelta import relativedelta
from functools import reduce

from datetime import date, timedelta, datetime
import warnings
from calendar import monthrange
import re
import ast
import gspread
import json
import gc
from google.cloud import bigquery
import calendar
import sys
import time
import numpy as np
from pandas.io import gbq
import os
import pymysql
from datetime import datetime
import datetime
import pandas as pd

warnings.filterwarnings(action='ignore')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)






today_date = date.today()
yesterday_date = today_date-timedelta(1)
print(today_date)
print(yesterday_date)
month_start_date = yesterday_date.replace(day=1)
print(month_start_date)

yesterday_day=yesterday_date.day
print(yesterday_day)
yesterday_month=yesterday_date.month
yesterday_year=yesterday_date.year

if yesterday_month >= 4:
    financial_year_start_date = month_start_date.replace(month=4)
else:
    financial_year_start_date = month_start_date.replace(year=yesterday_year-1,month=4)
print(financial_year_start_date)

financial_year = financial_year_start_date.year
previous_financial_year_start_date = financial_year_start_date.replace(year=financial_year-1)
previous_financial_year_end_date = financial_year_start_date - timedelta(1)
print(previous_financial_year_start_date)
print(previous_financial_year_end_date)
