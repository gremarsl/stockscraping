liste = ['45317000000.0', '51728000000.0', '49360000000.0', '51865000000.0']


def convert_list_elements_to_int(y):
    return [int(float(x)) for x in y]


a = convert_list_elements_to_int(liste)

print(a)
