from general_functions import read_data_from_file

# build own json data based on extracting data from alpha vantage files

# paramter I want to get be inserted in my file:
# input

parameter_list = ["totalRevenue", "costOfRevenues",
             "grossProfit",
             "researchAndDevelopment",
             "operationsIncome",
             "ebit",
             "netIncome",
             "totalCurrentAssets",
             "goodwill",
             "totalNonCurrentAssets",
             "totalAssets",
             "totalCurrentLiabilities",
             "totalNonCurrentLiabilities",
             "totalLiabilities",
             "totalShareholdersEquity", "operatingCashflow"]

parameter_list = ["fiscalDateEnding","totalRevenue"]
#Die Funktion filter(funktion, liste) bietet eine elegante Möglichkeit diejenigen Elemente aus der Liste liste herauszufiltern, für die die Funktion funktion True liefert.
#Die Funktion filter(f,l) benötigt als erstes Argument eine Funktion f die Wahrheitswerte liefert. Diese Funktion wird dann auf jedes Argument der Liste l angewendet. Liefert f True für ein x, dann wird x in der Ergebnisliste übernommen.

#x ist ein element in der liste data_lists
def filter_relative_alpha_vantage_data(data_list):
    indicators = list(filter(
        lambda x: x[3] == "researchAndDevelopment_to_totalRevenue" or "totalLiabilities_to_totalAssets",
        data_list))
    return indicators

# filter
def filter_object_key(json_data_object,key):

    del json_data_object[key]

    return json_data_object

s = "AAPL"
income_statement = read_data_from_file("reduced_" + s + ".json")
json_data_object = filter_object_key(income_statement,"annualReports")


d = {}
d['symbol'] ="AAPL"
d["quarterlyReports"] =[]
array = d["quarterlyReports"]

print(json_data_object)
#gehe jeden quaterly report durch
for quarter in json_data_object["quarterlyReports"]:
    # für jeden key in einem quater - filter jeden parameter weg, der nicht teil von parameterlist ist

    list_extracted = list(filter(lambda x:  x[0] in parameter_list,quarter.items()))
    obj = {}
    print("list extraced: {}".format(list_extracted))


    print("array: {}".format(array))

    for elem in list_extracted:

        obj[elem[0]] = elem[1]

    array.append(obj)
print(d)
'''

print(json_data_object)
onlyquaterly = json_data_object["quarterlyReports"]
print(onlyquaterly)
print(len(onlyquaterly))
only_last_quater = onlyquaterly[0]
print(only_last_quater)
value = only_last_quater["fiscalDateEnding"]
print(value)
'''
