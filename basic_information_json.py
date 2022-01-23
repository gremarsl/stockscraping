
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


print(data)
onlyquaterly = data["quarterlyReports"]
print(onlyquaterly)
print(len(onlyquaterly))
only_last_quater = onlyquaterly[0]
print(only_last_quater)
value = only_last_quater["fiscalDateEnding"]
print(value)



#lambda
# Die Funktion filter(funktion, liste) bietet eine elegante Möglichkeit diejenigen Elemente aus der Liste liste herauszufiltern, für die die Funktion funktion True liefert.
# Die Funktion filter(f,l) benötigt als erstes Argument eine Funktion f die Wahrheitswerte liefert. Diese Funktion wird dann auf jedes Argument der Liste l angewendet. Liefert f True für ein x, dann wird x in der Ergebnisliste übernommen.
# x ist ein element in der liste data_lists