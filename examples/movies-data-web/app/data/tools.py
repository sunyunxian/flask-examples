import json
from pathlib import Path

p = Path(__file__).absolute().parent


class MoviesData:
    def __init__(self, keyword: str) -> None:
        self.keyword = keyword
        self.movies = None
        self.total = 0

    def get_data(self) -> dict:
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
        return_result = {
            'movies': self.movies,
            'total': self.total,
            'keyword': self.keyword,
        }
        with open(f'{p}/data.json', 'r') as f:
            data = json.load(f)
        id_or_title = 'title'
        if len(self.keyword) == 8 and self.keyword.isdigit():
            # if keyword is id, search by id
            id_or_title = 'id'
            result = [i for i in data if self.keyword in i[id_or_title]]
        else:
            result = [i for i in data if self.keyword in i[id_or_title]]
        if result:
            total = len(result)
            return_result['total'] = total
        return_result['movies'] = result
        return return_result


if __name__ == '__main__':
    print(MoviesData('阳光').get_data())
