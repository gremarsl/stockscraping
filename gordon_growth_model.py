
def fair_price_DDM(price, number_of_years, dividend, expected_return, expected_growth):
    if number_of_years == 0:
        print("calculated fair price: {}".format(price))
        return True

    dividend_year_n_plus1 = dividend * (1 + expected_growth)

    price_n_plus1 = dividend_year_n_plus1 / (expected_return-expected_growth)

    number_of_years = number_of_years - 1
    fair_price_DDM(price_n_plus1, number_of_years, dividend_year_n_plus1, expected_return, expected_growth)


def discounted_cash_flow_model(DCF, start_year, end_year, cash_flow,cash_flow_growth, discontierungssatz):

    DCF_this_year = cash_flow / ((1 + discontierungssatz)**start_year)

    #TODO disconstierungssatz in der formel ist gesamtkapitalkosten - ermittlung über WACC verfahren
    DCF_new = DCF + DCF_this_year

    start_year_new = start_year+1
    cash_flow_new = cash_flow*(1+cash_flow_growth)

    if start_year_new <= end_year:
        # print("start year: {}   end:{}  casg: {} dis {} ".format(start_year,end_year,cash_flow,discontierungssatz))
        # print("--------")
        # print("--------")
        discounted_cash_flow_model(DCF_new,start_year_new,end_year,cash_flow_new,cash_flow_growth,discontierungssatz)

    print("start year: {}   DCF:{}  DCF_this_year: {} DCF_new: {} ".format(start_year, DCF,DCF_this_year,DCF_new))

    return True



fair_price_DDM(price=0, number_of_years=5, dividend= 10, expected_return=0.06, expected_growth=0.03)

fair_price_DDM(price=0, number_of_years=5, dividend= 1000000, expected_return=0.05, expected_growth=0.00)


discounted_cash_flow_model(DCF=0,start_year=1,end_year=5,cash_flow=32,cash_flow_growth=0.03,discontierungssatz=0.01)
