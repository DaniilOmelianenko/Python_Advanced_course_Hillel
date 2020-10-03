def parse(query: str) -> dict:
    query_temp_list = ((query.partition('?'))[-1]).split('&')
    query_temp_dict = {}
    for i in query_temp_list:
        if '=' in i:
            query_temp_dict[(i.partition('=')[0])] = (i.partition('='))[-1]
    return query_temp_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
print(parse('https://example.com/path/to/page?name=ferret&color=purple&'))
