from general_functions import read_data_from_file, write_to_file_in_json_format, delete_object_key

# build own json data based on extracting data from alpha vantage files

# paramter I want to get be inserted in my file:
# input

parameter_list = ["fiscalDateEnding", "totalRevenue"]
parameter_list = ["fiscalDateEnding", "totalRevenue", "costOfRevenues",
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

# Die Funktion filter(funktion, liste) bietet eine elegante Möglichkeit diejenigen Elemente aus der Liste liste herauszufiltern, für die die Funktion funktion True liefert.
# Die Funktion filter(f,l) benötigt als erstes Argument eine Funktion f die Wahrheitswerte liefert. Diese Funktion wird dann auf jedes Argument der Liste l angewendet. Liefert f True für ein x, dann wird x in der Ergebnisliste übernommen.
# x ist ein element in der liste data_lists

s = "AAPL"
income_statement = read_data_from_file("reduced_" + s + ".json")
json_data_object = delete_object_key(income_statement, "annualReports")

# create own empty file
d = {}
d['symbol'] = s
d["quarterlyReports"] = []
array = d["quarterlyReports"]

# gehe jeden quaterly report durch
for quarter in json_data_object["quarterlyReports"]:
    # für jeden key in einem quater - filter jeden parameter weg, der nicht teil von parameterlist ist

    print(quarter.items())
    list_extracted = list(filter(lambda x: x[0] in parameter_list, quarter.items()))
    obj = {}

    for elem in list_extracted:
        obj[elem[0]] = elem[1]

    # füge das object mit allen parametern in dieser datei zu dem array - als ein object (pro quarter) hinzu
    array.append(obj)

filepath = "D://Desktop//Finanzreporte//json//" + s + ".json"
write_to_file_in_json_format(d, filepath)

print(d)

## begin file 2
balance_sheet = read_data_from_file("reduced_balance_" + s + ".json")
add_on_file_object = delete_object_key(balance_sheet, "annualReports")

# gehe jeden quaterly report durch
for quarter in add_on_file_object["quarterlyReports"]:
    # für jeden key in einem quater - filter jeden parameter weg, der nicht teil von parameterlist ist

    list_extracted = list(filter(lambda x: x[0] in parameter_list, quarter.items()))
    print("listextraced: {}".format(list_extracted))

    # überprüfe für jeden parameter in list_extracted, ob schon hinzugefügt zu ersten datei die erstellt wurde

    for quarterA in d["quarterlyReports"]:
        list_extracted_fileA = list(filter(lambda x: x[0] in list_extracted, quarterA.items()))
        print("list_extracted_fileA: {}".format(list_extracted_fileA))

    # erstelle ein object
    obj = {}
    # befülle das object mit jedem gefilterten parameter
    for elem in list_extracted:
        obj[elem[0]] = elem[1]

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
