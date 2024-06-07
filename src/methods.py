
def euler(func, xs, y0) -> list[float]:
    h = xs[1] - xs[0]
    ys = [y0]
    
    for i in range(1, len(xs)):
        y_next = ys[i-1] + h*func(xs[i-1], ys[i-1])
        ys.append(y_next)

    return ys


def runge_kutta_4(func, xs, y0) -> list[float]:
    ys = [y0]
    h = xs[1] - xs[0]
    for i in range(1, len(xs)):
        k1 = h * func(xs[i-1], ys[i-1])
        k2 = h * func(xs[i-1] + h / 2, ys[i-1] + k1 / 2)
        k3 = h * func(xs[i-1] + h / 2, ys[i-1] + k2 / 2)
        k4 = h * func(xs[i-1] + h, ys[i-1] + k3)
        ys.append(ys[i-1] +  (k1 + 2 * k2 + 2 * k3 + k4) / 6)
    return ys


def milne(func, xs, y0, eps) -> list[float]:
    n = len(xs)
    h = xs[1] - xs[0]
    ys = [y0]
    for i in range(1, 4):
        k1 = h * func(xs[i - 1], ys[i - 1])
        k2 = h * func(xs[i - 1] + h / 2, ys[i - 1] + k1 / 2)
        k3 = h * func(xs[i - 1] + h / 2, ys[i - 1] + k2 / 2)
        k4 = h * func(xs[i - 1] + h, ys[i - 1] + k3)
        ys.append(ys[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    for i in range(4, n):
        # predict
        yp = ys[i - 4] + 4 * h * (2 * func(xs[i - 3], ys[i - 3]) - func(xs[i - 2], ys[i - 2]) + 2 * func(xs[i - 1], ys[i - 1])) / 3

        # correct
        y_next = yp
        while True:
            yc = ys[i - 2] + h * (func(xs[i - 2], ys[i - 2]) + 4 * func(xs[i - 1], ys[i - 1]) + func(xs[i], y_next)) / 3
            if abs(yc - y_next) < eps:
                y_next = yc
                break
            y_next = yc

        ys.append(y_next)

    return ys

    