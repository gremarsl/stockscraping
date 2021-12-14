import os
import requests
import json
from keys import api_key
from requests import Response
from general_functions import write_to_file_in_json_format, reverse_lists

api_url = "https://finnhub.io/api/v1/stock/metric?"


def calling_finnhub_api(symbols: str) -> Response:
    # 'https://finnhub.io/api/v1/stock/metric?symbol=DAI.DE&metric=all&token=buk3id748v6r2017iuog'

    for s in symbols:
        data = {
            "symbol": s,
            "metric": "all",
            "token": api_key}

        filename = "fundamental_data_finnhub_" + s + ".json"


        fundamental_data_response = requests.get(api_url, data)
        fundamental_data_response_json: requests.models.Response = fundamental_data_response.json()  # maybe redundant
        write_to_file_in_json_format(fundamental_data_response_json, filename)

        print("Successful finnhub api scraping for {}".format(s))

    return


def get_one_absolute_indicator_from_finnhub(data_json: dict,period :str, indicator: str, symbol: str) -> list:

    data = data_json['series'][period][indicator]
    time_points = []
    value_points = []
    for i in data:
        # i ist ein  Array
        value_points.append(i['v'])
        time_points.append(i['period'])

    value_points, time_points = reverse_lists(value_points, time_points)

    data_list = [time_points, value_points, symbol, indicator]

    return data_list


def get_one_ratio_indicator_from_finnhub(data_json: dict,period:str, indicator: str, symbol: str) -> list:
    data = data_json['series'][period][indicator]
    time_points = []
    value_points = []
    for i in data:
        # i ist ein  Array
        value_points.append(i['v'])
        time_points.append(i['period'])

    value_points, time_points = reverse_lists(value_points, time_points)

    data_list = [time_points, value_points, symbol, indicator]

    return data_list


def get_one_relative_indicator_from_finnhub(data_json: dict,period:str, indicator: str, symbol: str) -> list:
    data = data_json['series'][period][indicator]
    time_points = []
    value_points = []
    for i in data:
        # i ist ein  Array
        value_points.append(i['v'] * 100)
        time_points.append(i['period'])

    value_points, time_points = reverse_lists(value_points, time_points)

    data_list = [time_points, value_points, symbol, indicator]

    return data_list
