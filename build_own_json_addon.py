## begin file 2
from build_own_json import parameter_list
from general_functions import read_data_from_file, delete_object_key, write_to_file_in_json_format

print("BEFORE1")

s = "AAPL"
print("BEFORE")
balance_sheet = read_data_from_file("reduced_balance_" + s + ".json")
add_on_file_object = delete_object_key(balance_sheet, "annualReports")

print(add_on_file_object["quarterlyReports"])
data = {
    "symbol": "AAPL",
    "quarterlyReports": [
        {
            "fiscalDateEnding": "2021-09-30",
            "grossProfit": "35174000000",
            "totalRevenue": "82688000000",
            "researchAndDevelopment": "5772000000",
            "ebit": "23920000000",
            "netIncome": "20551000000"
        },
        {
            "fiscalDateEnding": "2021-06-30",
            "grossProfit": "35255000000",
            "totalRevenue": "80769000000",
            "researchAndDevelopment": "5717000000",
            "ebit": "25034000000",
            "netIncome": "21744000000"
        }
    ]
}

# gehe jeden quaterly report durch (quarter ist ein object

#introduce counter to ensure, that addon file quarter matches with the already existing quarter
counter = 0
for quarter in add_on_file_object["quarterlyReports"]:
    # für jeden key in einem quater - filter jeden parameter weg, der nicht teil von parameterlist ist

    list_extracted = list(filter(lambda x: x[0] in parameter_list, quarter.items()))

    print("list extraced: {}: ".format(list_extracted))

    #controlle ob schon enthalten
    for i in list_extracted:

        # counter used to
        if list_extracted[0][1] == data["quarterlyReports"][counter]['fiscalDateEnding']:
            print("same quarter ")
            if i in data["quarterlyReports"][counter].items():
                print("key value pair of object is already added as a parameter to the object: {}".format(i))

            # wenn nicht enthalte
            else:
                #wenn nicht enthalten, füge diese key value paar zu dem object quarter hinzu
                data["quarterlyReports"][counter][i[0]] = i[1]
        else:
            print("not same quater")

    counter+=1

filepath = "D://Desktop//Finanzreporte//json//" + s + "_addon" + ".json"
write_to_file_in_json_format(data, filepath)



    # wenn enthalten
        #vergleiche beide werte
