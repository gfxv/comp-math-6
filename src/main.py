import utils
import methods

import matplotlib.pyplot as plt
# Метод Эйлера
# Метод Рунге-Кутта 4- го порядка.
# Метод Милна

def main() -> None:
    odu_number = utils.select_odu() - 1
    odu = utils.FUNCTIONS[odu_number]
    xs, y0, e = utils.select_boundaries()

    y_exact = [utils.EXACT_SOLUTION[odu_number](x, xs[0], y0) for x in xs]

    _, ax = plt.subplots()

    print("===== Euler =====")
    ys = methods.euler(odu, xs, y0)
    print(list(map(lambda y: round(y, 4), ys)))
    eps = [abs(exact - y) for exact, y in zip(y_exact, ys)]
    print("Accuracy:", max(eps))
    ax.plot(xs, ys, label="Euler")

    print()

    print("===== Runge Kutta (4) =====")
    ys = methods.runge_kutta_4(odu, xs, y0)
    print(list(map(lambda y: round(y, 4), ys)))
    eps = [abs(exact - y) for exact, y in zip(y_exact, ys)]
    print("Accuracy:", max(eps))
    # print(len(ys))
    # print(len(xs))
    ax.plot(xs, ys, label="Runge Kutta")
    
    print()

    print("===== Milne =====")
    ys = methods.milne(odu, xs, y0, e)
    print(list(map(lambda y: round(y, 4), ys)))
    eps = [abs(exact - y) for exact, y in zip(y_exact, ys)]
    print("Accuracy:", max(eps))
    ax.plot(xs, ys, label="Milne")

    print()

    print("===== Exact Values =====")
    print(list(map(lambda y: round(y, 4), y_exact)))
    ax.plot(xs, y_exact, label="Exact")

    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()