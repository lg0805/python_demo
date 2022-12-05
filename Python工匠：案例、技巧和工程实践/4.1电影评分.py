# @FileName : 4.1电影评分
# @Time     : 2022/12/5 19:20
# @Author   : ligg
import random

movies = [
    {'name': 'The Dark Knight', 'year': 2008, 'rating': '9'},
    {'name': 'Kaili Blues', 'year': 2015, 'rating': '7.3'},
    {'name': '战狼', 'year': 2018, 'rating': '9.2'}
]


class Movie:
    """电影对象数据类"""

    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating

    @property
    def rank(self):
        """
        按评分对电影分级：
        - S：８.５分及以上
        - A: 8 - 8.5
        - B：7 - ８
        - C: 6 - 7
        - C: 6分以下
        """
        rating_num = float(self.rating)
        if rating_num >= 8.5:
            return 'S'
        elif rating_num >= 8:
            return 'A'
        elif rating_num >= 7:
            return 'B'
        elif rating_num >= 6:
            return 'C'
        else:
            return 'D'


def get_sorted_movies(movies: list, sorting_type: str) -> list:
    """对电影列表进行排序并返回"""
    if sorting_type == 'name':
        sorted_movies = sorted(movies, key=lambda movie: movie.name.lower())
    elif sorting_type == 'rating':
        sorted_movies = sorted(movies, key=lambda movie: float(movie.rating), reverse=True)
    elif sorting_type == 'year':
        sorted_movies = sorted(movies, key=lambda movie: movie.year, reverse=True)
    elif sorting_type == 'random':
        sorted_movies = sorted(movies, key=lambda movie: random.random())
    else:
        raise RuntimeError(f'Unknown sorting type: {sorting_type}')

    return sorted_movies


# m1 = Movie('aa', 2022, '82')
# print(m1.rank)

def main():
    # 接收用户输入的排序选项
    sorting_type = input('Please input sorting type: ')
    all_sorting_types = ['name', 'rating', 'year', 'random']
    if sorting_type not in all_sorting_types:
        print('Sorry, "{}" is not a valid sorting type, '
              'please choose from "{}", '
              'exit now'.format(sorting_type, '/'.join(all_sorting_types)))
        return

    # 初始化电影数据对象
    movies_items = []
    for movie_json in movies:
        movie = Movie(**movie_json)
        movies_items.append(movie)

    # 排序并输出电影列表
    sorted_movies = get_sorted_movies(movies_items, sorting_type)

    for movie in sorted_movies:
        print(f'- [{movie.rank}] {movie.name}({movie.year}) | rating: {movie.rating}')
    # Please input sorting type: year
    # - [S] 战狼(2018) | rating: 9.2
    # - [B] Kaili Blues(2015) | rating: 7.3
    # - [S] The Dark Knight(2008) | rating: 9

    # Please input sorting type: rating
    # - [S] 战狼(2018) | rating: 9.2
    # - [S] The Dark Knight(2008) | rating: 9
    # - [B] Kaili Blues(2015) | rating: 7.3


if __name__ == "__main__":
    main()



