# **********************************************************************************************************************
# Imports
# ********************************************************************************************************************
import global_vars
from general_functions import read_data_from_file, write_to_file_in_json_format, delete_object_key, \
    create_json_object_finance, add_keys_values_to_object


# **********************************************************************************************************************
# Functions
# **********************************************************************************************************************
def build_own_json_file(symbol_list):

    for s in symbol_list:
        parameter_list = ["fiscalDateEnding", "totalRevenue"]
        parameter_list = ["fiscalDateEnding", "totalRevenue", "costOfRevenue",
                          "grossProfit",
                          "researchAndDevelopment",
                          "operatingIncome",
                          "ebit",
                          "netIncome",
                          "totalCurrentAssets",
                          "goodwill",
                          "totalNonCurrentAssets",
                          "totalAssets",
                          "totalCurrentLiabilities",
                          "totalNonCurrentLiabilities",
                          "totalLiabilities",
                          "operatingCashflow"]

        income_statement = read_data_from_file(global_vars.filepath_alpha + "income_statement_alpha_" + s + ".json")
        input_object = delete_object_key(income_statement, "annualReports")

        # create empty json_object_finance
        output_object = create_json_object_finance(s)
        output_quarter_array = output_object["quarterlyReports"]

        for quarter in input_object["quarterlyReports"]:
            # filter nur die parameter mit dem wert heraus, der teil der parameter_list ist und speichere sie in filtered_list
            filtered_list = list(filter(lambda x: x[0] in parameter_list, quarter.items()))

            obj = add_keys_values_to_object(filtered_list)

            # füge das object mit allen parametern in dieser datei zu dem array - als ein object (pro quarter) hinzu
            output_quarter_array.append(obj)

        filepath = global_vars.filepath_my_json + s + ".json"
        write_to_file_in_json_format(output_object, filepath)

        # addonfile
        balance_sheet = read_data_from_file(global_vars.filepath_alpha + "balance_sheet_alpha_" + s + ".json")
        add_on_object = delete_object_key(balance_sheet, "annualReports")

        # gehe jeden quaterly report durch (quarter ist ein object
        # introduce counter to ensure, that addon file quarter matches with the already existing quarter
        counter = 0
        for quarter in add_on_object["quarterlyReports"]:
            # für jeden key in einem quater - filter jeden parameter weg, der nicht teil von parameterlist ist
            list_extracted = list(filter(lambda x: x[0] in parameter_list, quarter.items()))

            # kontrolle ob schon enthalten
            for i in list_extracted:

                # counter used to
                if list_extracted[0][1] == output_quarter_array[counter]['fiscalDateEnding']:
                    if i in output_quarter_array[counter].items():
                        print(f"key value pair of object is already added as a parameter to the object: {i}")

                    # wenn nicht enthalte
                    else:
                        # wenn nicht enthalten, füge diese key value paar zu dem object quarter hinzu
                        output_quarter_array[counter][i[0]] = i[1]
                else:
                    print("not same quarter")

            counter += 1

        filepath = global_vars.filepath_my_json + s + ".json"
        write_to_file_in_json_format(output_object, filepath)
