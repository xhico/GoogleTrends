# -*- coding: utf-8 -*-
# !/usr/bin/python3

import plotly.express as px
from pytrends.request import TrendReq


if __name__ == '__main__':
    print("Crypto Google Trends")

    # connect to google
    pytrends = TrendReq(hl='en-US', tz=-360)

    # build payload
    # list of keywords to get data
    kw_list = ["machine learning"]
    pytrends.build_payload(kw_list, cat=0, timeframe='2021-06-03 2021-12-03')

    # 1 Interest over Time
    data = pytrends.interest_over_time()
    data = data.reset_index()

    fig = px.line(data, x="date", y=[
                  'machine learning'], title='Keyword Web Search Interest Over Time')
    fig.show()
