from json import dumps

def json_encode(data, ensure_ascii=False, encoding="utf-8"):
    return dumps(data, ensure_ascii=ensure_ascii).encode('utf-8')