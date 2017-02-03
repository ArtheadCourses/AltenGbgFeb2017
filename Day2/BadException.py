
def gen():
    yield 1
    yield 2


def main():
    for i in gen():
        print(i)

    g = gen()
    print(next(g))
    print(next(g))
    print(next(g))

if __name__ == '__main__':
    main()