import MetaTrader5 as mt5
import datetime
import pytz
symbol = "EURUSD"

Model_type = "v2_SimpleRNN"
timeframe = mt5.TIMEFRAME_M1
time_series = 15
Debug =False


timezone = pytz.timezone("Etc/UTC")
utc_from = datetime.datetime(2022, 10, 1, tzinfo=timezone)