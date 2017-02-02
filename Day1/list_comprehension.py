
def main():
    num_list = [1, 2, 3, 4, 5, 6]

    result = []
    for value in num_list:
        if value != 4:
            if value != 3:
                result.append(value**2)
            else:
                result.append(value**3)

    print(result)

    result = [value**2 if value != 3 else value**3 for value in num_list if value != 4]

    print(result)

    new_result = []
    for x in range(2):
        for y in range(3):
            new_result.append(x+y)

    print(new_result)

    new_result = [x+y for x in range(2) for y in range(3)]
    print(new_result)

if __name__ == '__main__':
    main()