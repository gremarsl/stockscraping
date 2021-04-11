import os
import requests
import json
from keys import api_key
from requests import Response
from general_functions import write_to_file_in_json_format, reverse_lists

api_url = "https://finnhub.io/api/v1/stock/metric?"


def fundamental_data_from_finnhub(symbol: str) -> Response:
    data = {
        "symbol": symbol,
        "metric": "all",
        "token": api_key}

    filename = "fundamental_data_" + symbol + ".json"

    if os.path.isfile(filename):
        with open(filename) as json_file:
            fundamental_data_response_json = json.load(json_file)

    else:
        fundamental_data_response = requests.get(api_url, data)
        fundamental_data_response_json: requests.models.Response = fundamental_data_response.json()  # maybe redundant

        write_to_file_in_json_format(fundamental_data_response_json, filename)

    return fundamental_data_response_json


def get_one_absolute_indicator_from_finnhub(data_json: dict, indicator: str, symbol: str) -> list:
    data = data_json['series']['annual'][indicator]
    time_points = []
    value_points = []
    for i in data:
        # i ist ein  Array
        value_points.append(i['v'])
        time_points.append(i['period'])

    value_points, time_points = reverse_lists(value_points, time_points)

    data_list = [time_points, value_points, symbol, indicator]

    return data_list


def get_one_ratio_indicator_from_finnhub(data_json: dict, indicator: str, symbol: str) -> list:
    data = data_json['series']['annual'][indicator]
    time_points = []
    value_points = []
    for i in data:
        # i ist ein  Array
        value_points.append(i['v'])
        time_points.append(i['period'])

    value_points, time_points = reverse_lists(value_points, time_points)

    data_list = [time_points, value_points, symbol, indicator]

    return data_list


def get_one_relative_indicator_from_finnhub(data_json: dict, indicator: str, symbol: str) -> list:
    data = data_json['series']['annual'][indicator]
    time_points = []
    value_points = []
    for i in data:
        # i ist ein  Array
        value_points.append(i['v'] * 100)
        time_points.append(i['period'])

    value_points, time_points = reverse_lists(value_points, time_points)

    data_list = [time_points, value_points, symbol, indicator]

    return data_list
