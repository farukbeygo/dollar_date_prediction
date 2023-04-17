import numpy as np


def linear_regression(x, y, iterations):
    y_pred = 0

    for iteration in range(iterations):
        mean_x = np.mean(x)
        mean_y = np.mean(y)

        deviations_x = x - mean_x
        deviations_y = y - mean_y

        beta_1 = np.sum(deviations_x * deviations_y) / np.sum(deviations_x ** 2)
        beta_0 = mean_y - beta_1 * mean_x

        y_pred = beta_0 + beta_1 * x

    return y_pred
