def f(x):
    df = 0
    for d in range(len(x)):
        df += x[d]
    return df


def f2(x):
    df = 0
    for d in range(len(x)):
        df += pow(x[d], 2)
    return df


def fmultiply(x):
    df = 1
    for d in range(len(x)):
        df *= x[d]
    return df


def integrator(f, t):
    res = list(map(lambda x: x(t), f))
    return res


def main():
    funcs = [f, f2, fmultiply]
    t = [1, 3, 4, 5, 10]

    result = integrator(funcs, t)

    for i in range(len(result)):
        print('%i.  %.2f' % (i + 1, result[i]))


if __name__ == "__main__":
    main()