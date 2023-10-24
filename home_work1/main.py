def parse(query: str) -> dict:
    params = query.split('?')[-1].split('&')
    result = {}
    for param in params:
        if '=' in param:
            key, value = param.split('=')
            result[key] = value
    return result


def parse_cookie(query: str) -> dict:
    result = {}
    cookies = query.split(';')
    for cookie in cookies:
        key_value = cookie.strip().split('=', 1)
        if len(key_value) == 2:
            key, value = key_value
            result[key.strip()] = value
    return result


if __name__ == '__main':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}

    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}
