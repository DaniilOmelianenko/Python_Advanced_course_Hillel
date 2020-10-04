def parse_cookie(query: str) -> dict:
    query_temp_dict = {}
    for temp_value in query.split(';'):
        if '=' in temp_value:
            query_temp_dict[(temp_value.partition('=')[0])] = (temp_value.partition('='))[-1]
    return query_temp_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
print(parse_cookie('name=Dima=User;age=28;'))

