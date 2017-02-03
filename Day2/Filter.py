
def odd_number(n):
    return n % 2

def main():
    f = (lambda x, y: x + y)(3,4)
    print(f)

    list_of_no = [12, 45, 32, 43, 55, 2, 56]
    result = list(filter(odd_number, list_of_no))
    result2 = list(filter(lambda n: n % 2, list_of_no))
    result3 = [n for n in list_of_no if n % 2]
    print(result3)
    
if __name__ == '__main__':
    main()