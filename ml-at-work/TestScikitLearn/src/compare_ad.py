import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from matplotlib.font_manager import FontProperties

font_prop = FontProperties(fname=r'C:\WINDOWS\Fonts\YuGothM.ttc', size=12)
a = [40, 165]
b = [62, 228]
x = np.linspace(0, 1, 200)


def print_info(name, values):
    print("{}: size={}, converted={}, mean={:.3f}".format(name, sum(values), values[0], values[0] / sum(values)))


def get_y(values):
    n = sum(values)
    p = values[0] / n
    std = np.sqrt(p * (1 - p) / n)
    return scipy.stats.norm.pdf(x, p, std)


def compare_advertisement():
    print_info("Sample A", a)
    print_info("Sample B", b)

    # 流入元がAの標本
    y_a = get_y(a)
    # 流入元がBの標本
    y_b = get_y(b)

    plt.figure(figsize=(7, 2))
    plt.plot(x, y_a, label="Sample A")
    plt.plot(x, y_b, label="Sample B")
    plt.legend(loc="best")
    plt.xlabel("新規ユーザの継続化率", fontproperties=font_prop)
    plt.ylabel("尤度", fontproperties=font_prop)
    plt.show()

    _, p_value, _, _ = scipy.stats.chi2_contingency([a, b])
    print(p_value)


def main():
    compare_advertisement()


if __name__ == "__main__":
    main()
