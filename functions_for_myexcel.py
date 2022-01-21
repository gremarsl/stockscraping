def filter_my_json_data_origin(data_list, options):
    indicators = list(filter(
        lambda x: x[3] == "totalRevenue" or "netIncome",
        data_list))
    return indicators
