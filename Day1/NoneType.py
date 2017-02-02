'''
This is a
multi-line comment
'''

def test(name, name_list=None):
    if not name_list:
        name_list = [] #Create an empty list
    name_list.append(name)
    print(name_list)


def main():
    test_list = ['Eric']
    test('Anna', test_list)
    test('John')
    
if __name__ == '__main__':
    main()
