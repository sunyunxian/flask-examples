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
    result = []
    with open(f'{p}/data.json', 'r') as f:
        data = json.load(f)

    for i in data:
        if keyword in i['title']:
            result.append(i)

    return result


if __name__ == '__main__':
    print(get_data('阳光'))
