class employee:
    empCount = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        employee.empCount += 1

    def displayCount(self):
        print("The Total Number of employee are:", employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name, ",Age:", self.age, ", Salary:", self.salary)


obj = employee('Anup Karki', 30, 2000000)
obj.displayCount()
obj.displayEmployee()
