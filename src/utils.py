from math import sin, cos, exp

FUNCTIONS = [
    lambda x, y: x + y,
    lambda x, y: sin(x) + y,
    lambda x, y: y + exp(x)
]

CONSTANTS = [
    lambda x0, y0: (x0 + y0 + 1) / (exp(x0)),
    lambda x0, y0: (y0/exp(x0)) + (sin(x0) + cos(x0)) / (2*exp(x0)),
    lambda x0, y0: y0/exp(x0) - x0
]

EXACT_SOLUTION = [
    lambda x, x0, y0: CONSTANTS[0](x0, y0) * exp(x) - x -1,
    lambda x, x0, y0: -(sin(x)+cos(x)) / 2 + CONSTANTS[1](x0, y0) * exp(x),
    lambda x, x0, y0: (x + CONSTANTS[2](x0, y0)) * exp(x)
]


def select_odu() -> int:
    print("Choose ODU:")
    print("1. x + y")
    print("2. sin(x) + y")
    print("3. y + e^x")
    odu = int(input("(Enter a number of ODU) "))

    if odu < 1 or odu > len(FUNCTIONS):
        raise Exception("ODU input out of range")

    return odu

def select_boundaries() -> tuple:
    x0 = float(input("Input x0: "))
    xn = float(input("Input xn: "))
    x0, xn = min(x0, xn), max(x0, xn)

    n = int(input("Input number of intervals: "))
    if n <= 1:
        raise ValueError("Nuber of intervals can't be <= 1")
    
    y0 = float(input("Input y0: "))
    eps = float(input("Input accuracy (espilon): "))

    xs = [x0 + i * ((xn - x0) / n) for i in range(n)]

    return xs, y0, eps


