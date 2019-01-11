import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

if __name__ == "__main__":
    # https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
    diabetes = datasets.load_diabetes()
    diabetes_X = diabetes.data[:, np.newaxis, 2]
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]

    regression = linear_model.LinearRegression()
    regression.fit(diabetes_X_train, diabetes_y_train)
    diabetes_y_predict = regression.predict(diabetes_X_test)
    print("diabetes_y_test: {}\ndiabetes_y_predict: {}".format(diabetes_y_test, diabetes_y_predict))
    print("Coefficients: {}".format(regression.coef_))


def print_root_mean_squared_error():
    mse = mean_squared_error(diabetes_y_test, diabetes_y_predict)
    print("Mean squared error: {}".format(mse))
    rmse = sqrt(mse)
    print("Root mean squared error: {}".format(rmse))


def print_r2_score():
    print("Variance score: {}".format(r2_score(diabetes_y_test, diabetes_y_predict)))


def plot_outputs():
    plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
    plt.plot(diabetes_X_test, diabetes_y_predict, color="blue", linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def main():
    print_root_mean_squared_error()
    print_r2_score()
    plot_outputs()


if __name__ == "__main__":
    main()
