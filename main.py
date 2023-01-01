from http.cookies import SimpleCookie


def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    cookies = {k: v.value for k, v in cookie.items()}
    return cookies


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('{ key: value}') == {}
    assert parse_cookie('color=Grey;name=Silver;') == {'color': 'Grey', 'name': 'Silver'}
    assert parse_cookie('name=Sam=Admin;status=False;') == {'name': 'Sam=Admin', 'status': 'False'}
    assert parse_cookie('[]') == {}
    assert parse_cookie('name=Valera;age=28;;!;') == {'name': 'Valera', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28=55;') == {'name': 'Dima=User', 'age': '28=55'}
    assert parse_cookie('//1 }{ \\//') == {}
    assert parse_cookie('name=Not_found;status=unknown;') == {'name': 'Not_found', 'status': 'unknown'}
    assert parse_cookie('123421=FFF=User;age=28;') == {'123421': 'FFF=User', 'age': '28'}
    assert parse_cookie('name=Sarah;age=28;status=blocked;') == {'name': 'Sarah', 'age': '28', 'status': 'blocked'}
    assert parse_cookie('SSSrSSS=!!!!=User=22565;age=28;') == {'SSSrSSS': '!!!!=User=22565', 'age': '28'}
    assert parse_cookie('//1 }{ \\      //') == {}
