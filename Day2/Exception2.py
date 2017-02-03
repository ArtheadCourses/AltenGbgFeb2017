
class MyException(Exception):
    def __init__(self, value="", location="", msg=""):
        self.value = value
        self.location = location
        self.msg = msg

    def __str__(self):
        return "There is an error in {0} with code: {1}. Message: {2}".\
            format(self.location, self.value, self.msg)

def test_func():
    raise MyException("34b", "main()", "You can't do that here")


def main():
    try:
        test_func()
    except MyException as e:
        print(e)
        raise


if __name__ == '__main__':
    main()