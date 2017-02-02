
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __repr__(self):
        return f'Employee("{self.first}", "{self.last}", {self.pay})'

    def __str__(self):
        return "The name of this employee is {}".format(self.first)

    def __add__(self, other):
        return Employee(self.first, other.last, self.pay + other.pay)

def main():
    emp1 = Employee("John", "Smith", 50000)
    emp2 = Employee("Anna", "Jones", 55000)

    print(repr(emp1))
    print(str(emp2))

    emp3 = emp1 + emp2
    print(repr(emp3))

    emp4 = emp1 + emp2 + emp3
    print(repr(emp4))

if __name__ == '__main__':
    main()