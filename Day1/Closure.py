name = "Joakim"

def outer(pow):
    def inner(base):
        return base**pow
    return inner


def main():
    square = outer(2)
    print(square(2))
    print(square(3))

    cube = outer(3)
    print(cube(2))
    print(cube(3))

if __name__ == '__main__':
    main()