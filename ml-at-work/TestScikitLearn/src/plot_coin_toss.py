import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from matplotlib.font_manager import FontProperties
import pandas as pd

font_prop = FontProperties(fname=r'C:\WINDOWS\Fonts\YuGothM.ttc', size=12)


def plot_coin_toss():
    x = np.arange(0, 21)
    y = scipy.stats.binom.pmf(x, 20, 0.5)
    plt.figure(figsize=(8, 2))
    plt.bar(x, y)
    plt.xlabel('表が出る回数', fontproperties=font_prop)
    plt.ylabel('確率', fontproperties=font_prop)
    plt.show()

    p_value = pd.DataFrame({'表の出る回数': x, '確率': y}).query(
        '表の出る回数 >= 15'
    )['確率'].sum()
    print(p_value)


def iterate_testing():
    mu = 0.5  # 表が出る確率50%
    init_sample = list(scipy.stats.bernoulli.rvs(mu, size=20))
    sample = init_sample
    p_value_history = []
    for i in range(200):
        # 直近20回の結果を使って検定
        _, p_value = scipy.stats.ttest_1samp(sample[-20:], 0.5)
        p_value_history.append(p_value)
        # 新たにコインを投げて結果を保持
        sample.append(scipy.stats.bernoulli.rvs(mu))
    plt.figure(figsize=(10, 4))
    plt.plot(p_value_history)
    plt.xlabel('Test Epoch')
    plt.ylabel('p value')
    plt.show()


def sample_size_difference():
    max_sample = 3000000
    # 標本A 平均:45.1%
    a = scipy.stats.bernoulli.rvs(0.451, size=max_sample)
    # 標本B 平均:45.2%
    b = scipy.stats.bernoulli.rvs(0.452, size=max_sample)
    p_values = []
    # 5000づつ標本サイズを増やして検定を行う
    sample_sizes = np.arange(1000, max_sample, 5000)
    for sample_size in sample_sizes:
        _, p_value = scipy.stats.ttest_ind(a[:sample_size], b[:sample_size], equal_var=False)
        p_values.append(p_value)
    plt.figure(figsize=(10, 3))
    plt.plot(sample_sizes, p_values)
    plt.xlabel('sample size')
    plt.ylabel('p value')
    plt.show()


def main():
    # plot_coin_toss()
    # iterate_testing()
    sample_size_difference()


if __name__ == "__main__":
    main()
