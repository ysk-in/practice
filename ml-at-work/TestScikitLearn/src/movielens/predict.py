import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from fastFM import mcmc
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler

import lens_data


def load_data(filename, path="/mnt/c/tmp/ml-100k/"):
    """ dataファイルからパラメタとラベルを取得する
    :param filename: dataファイル名
    :param path: dataファイルのあるディレクトリパス
    :return: [0] data: dataファイルから取得したパラメタのリスト。各要素は各パラメタをfeature->value dictsで保持。
     [1] np.array(y): dataファイルから取得したラベルのnumpy.ndarray
    """
    data = []
    y = []
    with open(path + filename) as f:
        for line in f:
            (user, movie_id, rating, ts) = line.split('\t')
            # user_idとmovie_idをカテゴリカル変数として扱うため文字列に変換
            data.append({"user_id": str(user), "movie_id": str(movie_id)})
            y.append(float(rating))
    return data, np.array(y)


def fm_n_iter(X_train, X_dev_test, y_train, y_dev_test):
    """ fastFMで機械学習を行う
    :param X_train: 訓練データ
    :param X_dev_test: 検証データ
    :param y_train: 訓練データの評価値(ラベル?)
    :param y_dev_test: 検証データの評価値(ラベル?)
    :return:
    """
    # fastFMに指定するパラメタ
    n_iter = 300
    step_size = 1
    seed = 123
    rank = 4
    # MCMCのFMモデルを初期化
    fm = mcmc.FMRegression(n_iter=0, rank=rank, random_state=seed)
    fm.fit_predict(X_train, y_train, X_dev_test)
    # aaa
    rmse_dev_test = []
    rmse_test = []
    hyper_param = np.zeros((n_iter - 1, 3 + 2 * rank), dtype=np.float64)
    # TODO イテレーション回数を変化させて、予測結果の性能とハイパーパラメタを得る
    for nr, i in enumerate(range(1, n_iter)):
        fm.random_state = i * seed
        # (MCMCで)パラメタフィッティングおよび予測を行う
        y_pred = fm.fit_predict(X_train, y_train, X_dev_test, n_more_iter=step_size)
        rmse_test.append(np.sqrt(mean_squared_error(y_pred, y_dev_test)))
        hyper_param[nr, :] = fm.hyper_param_
    # 最初の5回は値が落ち着いていないので無視する
    values = np.arange(1, n_iter)
    x = values * step_size
    burn_in = 5
    x = x[burn_in:]
    # RMSEとハイパーパラメータをプロットする
    fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, figsize=(15, 8))
    axes[0, 0].plot(x, rmse_test[burn_in:], label='dev test rmse', color="r")
    axes[0, 0].legend()
    axes[0, 1].plot(x, hyper_param[burn_in:, 0], label='alpha', color="b")
    axes[0, 1].legend()
    axes[1, 0].plot(x, hyper_param[burn_in:, 1], label='lambda_w', color="g")
    axes[1, 0].legend()
    axes[1, 1].plot(x, hyper_param[burn_in:, 3], label='mu_w', color="g")
    axes[1, 1].legend()
    # 検証データのラベル値の標準偏差を出力。予測値の標準偏差がこの値より小さければ
    print("np.std(y_dev_test) = {}".format(np.std(y_dev_test)))
    plt.show()


def fm_rank(X_train, X_dev_test, y_train, y_dev_test):
    n_iter = 100
    seed = 333
    rmse_test = []
    ranks = [4, 8, 16, 32, 64]
    for rank in ranks:
        fm = mcmc.FMRegression(n_iter=n_iter, rank=rank, random_state=seed)
        y_pred = fm.fit_predict(X_train, y_train, X_dev_test)
        rmse = np.sqrt(mean_squared_error(y_pred, y_dev_test))
        rmse_test.append(rmse)
        print("rank:{}\trmse:{:.3f}".format(rank, rmse))
    plt.plot(ranks, rmse_test, label="dev test rmse", color="r")
    plt.legend()
    plt.show()
    pass


def fm(X_train, X_dev_test, y_train, y_dev_test, X_test, y_test):
    seed = 333
    fm = mcmc.FMRegression(n_iter=300, rank=32, random_state=seed)
    y_pred = fm.fit_predict(X_train, y_train, X_test)
    np.sqrt(mean_squared_error(y_pred, y_test))
    scaler = StandardScaler()
    y_train_norm = scaler.fit_transform(y_train.reshape(-1, 1)).ravel()
    fm = mcmc.FMRegression(n_iter=300, rank=32, random_state=seed)
    y_pred = fm.fit_predict(X_train, y_train_norm, X_test)
    print(np.sqrt(mean_squared_error(scaler.inverse_transform(y_pred), y_test)))


def fm_candidate_columns():
    lens, _, _, _ = lens_data.get_lens_data()
    lens['user_id'] = lens['user_id'].astype(str)
    lens['movie_id'] = lens['movie_id'].astype(str)
    lens['year'] = lens['date'].apply(str).str.split('-').str.get(0)
    lens['release_year'] = lens['release_date'].apply(str).str.split('-').str.get(2)
    candidate_columns = [
        ['user_id', 'movie_id', 'release_year', 'age', 'sex', 'year', 'rating'],  # A
        ['user_id', 'movie_id', 'age', 'sex', 'year', 'rating'],  # B
        ['user_id', 'movie_id', 'sex', 'year', 'rating'],  # C
        ['user_id', 'movie_id', 'age', 'sex', 'rating'],  # D
        ['user_id', 'movie_id', 'rating'],  # E
    ]
    rmse_test = []
    n_iter = 500
    seed = 123
    rank = 8
    for column in candidate_columns:
        filtered_lens = lens[column].dropna()
        v = DictVectorizer()
        X_more_feature = v.fit_transform(list(filtered_lens.drop('rating', axis=1).T.to_dict().values()))
        y_more_feature = filtered_lens['rating'].tolist()
        X_mf_train, X_mf_test, y_mf_train, y_mf_test = train_test_split(X_more_feature, y_more_feature, test_size=0.1,
                                                                        random_state=42)
        scaler = StandardScaler()
        y_mf_train_norm = scaler.fit_transform(np.array(y_mf_train).reshape(-1, 1)).ravel()
        fm = mcmc.FMRegression(n_iter=n_iter, rank=rank, random_state=seed)
        # Allocates and initalizes the model and hyper parameter.
        fm.fit_predict(X_mf_train, y_mf_train_norm, X_mf_test)
        y_pred = fm.fit_predict(X_mf_train, y_mf_train_norm, X_mf_test)
        rmse_test.append(np.sqrt(mean_squared_error(scaler.inverse_transform(y_pred.reshape(-1, 1)), y_mf_test)))
    print(rmse_test)
    # RMSEをプロットする
    ind = np.arange(len(rmse_test))
    bar = plt.bar(ind, height=rmse_test)
    plt.xticks(ind, ('A', 'B', 'C', 'D', 'E'))
    plt.ylim((0.88, 0.90))
    plt.show()


def main():
    # import pdb; pdb.set_trace()
    # dataファイルからパラメタとラベルを取得
    (dev_data, y_dev) = load_data("ua.base")
    (test_data, y_test) = load_data("ua.test")
    # DictVectorizerのtransformで、ダミー変数への変換 および dictsのリストをcsr_matrixに変換 を行う。
    v = DictVectorizer()
    # fit_transformしたあと、transformすることで、devとtestで
    # 同じv.feature_names_(feature name -> indices mappings)を使うことができる(という理解で正しい...?)
    X_dev = v.fit_transform(dev_data)
    X_test = v.transform(test_data)
    # dataを訓練データ:検証データ(パラメータの調整に使用する検証用のデータ)に 9:1で分割
    X_train, X_dev_test, y_train, y_dev_test = train_test_split(X_dev, y_dev, test_size=0.1, random_state=42)
    # Factorization Machinesで学習
    # fm_iterator(X_train, X_dev_test, y_train, y_dev_test)
    # fm_rank(X_train, X_dev_test, y_train, y_dev_test)
    # fm(X_train, X_dev_test, y_train, y_dev_test, X_test, y_test)
    fm_candidate_columns()


if __name__ == "__main__":
    main()
