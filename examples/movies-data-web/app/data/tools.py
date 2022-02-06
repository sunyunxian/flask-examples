import json
from pathlib import Path

p = Path(__file__).absolute().parent


def get_data(keyword: str) -> list:
    '''
    data format like this
    [
        {
        "title": "\u6210\u4e3a\u7b80\u00b7\u5965\u65af\u6c40",
        "original_title": "Becoming Jane",
        "is_tv": false,
        "year": "2007",
        "id": "1920805",
        "poster": "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1284506783.webp"
        },
    ]
    '''
    with open(f'{p}/data.json', 'r') as f:
        data = json.load(f)
    id_or_title = 'title'
    if len(keyword) == 8 and keyword.isdigit():
        # if keyword is id, search by id
        id_or_title = 'id'
        result = [i for i in data if keyword in i[id_or_title]]
    else:
        result = [i for i in data if keyword in i[id_or_title]]

    return result


if __name__ == '__main__':
    print(get_data('阳光'))
