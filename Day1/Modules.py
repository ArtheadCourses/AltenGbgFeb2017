
import import_module
from import_module import add
from import_module import add as add_it

def add(a, b):
    a += 1
    return a + b

def main():
    print(import_module.add(2,3)); # Uses import import_module
    #import_module.main()
    print(add(4,5)) # Uses from import_module import add
    print(add_it(2,9)) # Uses from import_module import add as add_it



if __name__ == '__main__':
    main()