
def func(x, y):
    if y == 0:
        raise ValueError("y can't be 0")
    result = x / y
    print(result)
    return result

def func2():
    raise RuntimeError
    print("Hi")

def main():
    try:
        a = func(10, 0)
        func2()
    except ValueError as e:
        print(e)
        a = func(10, 2)
    except RuntimeError:
        print("Runtime Error")
    finally:
        print("Done")
    print(a)
    
if __name__ == '__main__':
    main()