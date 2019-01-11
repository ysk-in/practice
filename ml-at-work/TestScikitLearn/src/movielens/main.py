import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# pandasの表示が省略表示(...)になるのを抑止するための設定
# 列がの表示数を増やす
pd.set_option("display.max_columns", 10)
# フィールドの表示文字数を伸ばす
pd.set_option("display.max_colwidth", 80)
# 行の表示文字数を伸ばす
pd.set_option("display.width", 800)

path_user = r'C:\tmp\ml-100k\u.user'
path_data = r'C:\tmp\ml-100k\u.data'
path_item = r'C:\tmp\ml-100k\u.item'


def add_date(data):
    key = 'unix_timestamp'
    if key not in data:
        return
    data['date'] = pd.to_datetime(data[key], unit='s')


def print_data(file_path, columns, separator, usecols=None, encoding=None):
    if usecols is not None and encoding is not None:
        data = pd.read_csv(file_path, sep=separator, names=columns, usecols=usecols, encoding=encoding)
    else:
        data = pd.read_csv(file_path, sep=separator, names=columns)
    add_date(data)
    print(data.head())
    return data


def main():
    # 各データをカラム名を付けて表示する
    columns = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
    users = print_data(path_user, columns, '|')
    columns = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    ratings = print_data(path_data, columns, '\t')
    columns = ['movie_id', 'title', 'release_data', 'video_release_date', 'imbd_url']
    movies = print_data(path_item, columns, '|', range(5), 'latin1')
    # 各データをmergeする 結合方法(on=, how=)は指定していないため，既定値(共通のキー, 内部結合)でマージされる。
    movie_ratings = pd.merge(movies, ratings)
    lens = pd.merge(movie_ratings, users)
    # print(lens)
    # titleが多く出現する上位25個を表示
    print(lens.title.value_counts()[:25])
    # 平均点が高い映画の上位を表示 -> 評価数が少ない，ノイズが乗りやすいものが上位に集まってしまう。
    movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
    print(movie_stats.sort_values(by=[('rating', 'mean')], ascending=False).head())
    # 100件以上の評価が付いているもののなからから，評価値の平均が高い順に表示。
    at_least_100 = movie_stats['rating']['size'] >= 100
    print(movie_stats[at_least_100].sort_values(by=[('rating', 'mean')], ascending=False)[:15])

    # 評価回数の分布のヒストグラムを表示
    # plt.style.use('ggplot')
    # lens.groupby('user_id').size().sort_values(ascending=False).hist()
    # plt.xlabel('rating size')
    # plt.ylabel('count of rating')
    # plt.show()

    # ユーザごとの評価数と評価値の平均を表示
    user_stats = lens.groupby('user_id').agg({'rating': [np.size, np.mean]})
    print(user_stats['rating'].describe())


if __name__ == "__main__":
    main()
