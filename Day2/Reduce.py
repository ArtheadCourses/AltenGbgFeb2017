from functools import reduce

def get_max(a, b):
    if a > b:
        return a
    else:
        return b

def get_min(a, b):
    if a < b:
        return a
    else:
        return b

def sum(a, b):
    return a + b

def main():
    list_of_no = [12, 45, 320, 43, 55, 2, 56]
    maximum = reduce(sum, list_of_no)

    print(maximum)

if __name__ == '__main__':
    main()