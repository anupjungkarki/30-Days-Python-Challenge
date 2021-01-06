# Use of multiple inheritance in python
# When a class can be derived from more than one base class this types of inheritance is called multiple inheritance.
class TeamMember(object):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid


class Worker(object):
    def __init__(self, salary, job_title):
        self.salary = salary
        self.job_title = job_title


class TeamLeader(TeamMember, Worker):
    def __init__(self, name, uid, salary, job_title, exp):
        self.exp = exp
        TeamMember.__init__(self, name, uid)
        Worker.__init__(self, salary, job_title)
        print("Name: {}, Pay: {}, Exp: {}".format(self.name, self.salary, self.exp))


obj = TeamLeader('Anup', 10001, 250000, 'Scrum Master', 5)


# One class extending more than one class is called multiple inheritance.Furthermore when a class is derived from more than one base class
# it is called multiple inheritance.The derived class inherit all the feature of the base class.

# Example of multiple inheritance
class Manager:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Employee:
    def __init__(self, salary, post):
        self.salary = salary
        self.post = post


class Person(Manager, Employee):
    def __init__(self, name, address, salary, post, points):
        self.points = points
        Manager.__init__(self, name, address)
        Employee.__init__(self, salary, post)
        print(self.name)


obj = Person('Anup Karki', 'Kathmandu', 300000, 'Data Analyst', 450)