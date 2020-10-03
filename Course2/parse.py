# def parse(query: str) -> dict:
#     pars_dict = dict(parse.parse_qsl(parse.urlsplit(query).query))
#     return pars_dict


# if __name__ == '__main__':
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('http://example.com/') == {}
#     assert parse('http://example.com/?') == {}
#     assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

url = 'https://example.com/path/to/page?name=ferret&color=purple'
first_slice = (url.partition('?'))
print(first_slice)
print(first_slice[-1])
print((str(first_slice[-1])).partition('?'))
print(url[-1])
if (url[-1]) == '?' or (url[-1]) == '&':
    query_string = str((url.partition('?'))[-1])
else:
    query_string = str((url.partition('?'))[-2])
print(query_string)
query_list = query_string.split('&')
print(query_list)
final_dict = {}
for i in query_list:
    temp_list = (str(i)).split('=')
    print(temp_list)
    #final_dict.setdefault(temp_list[0], temp_list[1])
print(final_dict)
