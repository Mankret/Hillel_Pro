import urllib.parse as urlparse


def parse(query: str) -> dict:
    result = {}
    pars_res = urlparse.urlparse(query)
    query_ = pars_res.query
    dict_from_query = urlparse.parse_qs(query_)
    for index, elem in dict_from_query.items():
        result.update({index: str(*elem)})
    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?name=wolf&color=white') == {'name': 'wolf', 'color': 'white'}
    assert parse('https://example.com/path/to/page?name=bee&color=black&&') == {'name': 'bee', 'color': 'black'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/!') == {}
    assert parse('http://example.com/?name=Albert') == {'name': 'Albert'}
    assert parse('http://example.com/?color=Green') == {'color': 'Green'}
    assert parse('http://example.com/path/to/watch?channel=A-one') == {'channel': 'A-one'}
    assert parse('http://example.com/?non=True&status=False') == {'non': 'True', 'status': 'False'}
    assert parse('http://example.com/+-&6534623463Bhretys=') == {}
    assert parse('http://example.com/+-&FGRE()462//=') == {}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
