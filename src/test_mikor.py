from pymikor import *


def f(x):
    df = 0
    for d in range(len(x)):
        df += x[d]
    return df


def main():
    integral = Mikor()
    integral.set_values(13, 5, 10000)
    integral.result()


if __name__ == "__main__":
    main()