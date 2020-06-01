def parse_query_string(url: str) -> dict:

    i = 0
    while (i < len(url) - 1) and (url[i] != '?'):
        i += 1

    querry = url[i + 1:]
    parameters = querry.split('&')

    parameters_dict = {}
    for parameter in parameters:
        key, value = parameter.split('=')
        parameters_dict.update({key: value})

    return parameters_dict


print(parse_query_string("http://example.com/show_item.php?item=car&color=red"))
