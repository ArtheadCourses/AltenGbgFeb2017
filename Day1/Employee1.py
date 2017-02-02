
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __repr__(self):
        return f'Employee("{self.first}", "{self.last}", {self.pay})'

    def __str__(self):
        return "The name of this employee is {}".format(self.first)

def main():
    emp1 = Employee("John", "Smith", 50000)
    emp2 = Employee("Anna", "Jones", 55000)

    print(repr(emp1))
    print(str(emp2))
    
if __name__ == '__main__':
    main()