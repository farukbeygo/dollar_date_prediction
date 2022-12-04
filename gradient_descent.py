# now I will create a function for linear regression
def gradient_descend(current_m, current_b, data, learning_rate):
    # initializing gradients
    m_gradient = 0
    b_gradient = 0
    dim = len(data)
    # calculation for gradients
    for point in range(dim):
        x = data.iloc[point].["key_1"]
        y = data.iloc[point].["key_2"]
        m_gradient = m_gradient - ((2/dim) * x * (y - (current_m * x - current_b)))
        b_gradient = b_gradient - ((2/dim) * (y - (current_m * x - current_b)))
    # uptating the values
    new_m = current_m - learning_rate * m_gradient
    new_b = current_b - learning_rate * b_gradient
    return new_m, new_b
