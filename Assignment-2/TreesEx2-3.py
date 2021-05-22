from collections import deque

# class to hold overall organization of employees
class OrganizationStructure:

    # initializes class by adding root employee
    def __init__(self, employee):
        self.employee = employee

    def printLevelByLevel(self):
        queue = deque() # queue used to print BFS
        queue.append(self.employee) # append root
        visited = set() # set so we don't process nodes twice

        # queue to print BFS
        while queue:
            curr = queue.popleft() # pops node out for process
            print(curr.getName()) # print name of employee

            # gets all children of node and adds to queue if not visited
            for report in curr.getReports():
                if report not in visited:
                    queue.append(report)
                    visited.add(report)



class Employee:

    # initializes employee class
    def __init__(self):
        self.name = ""
        self.title = ""
        self.directReports = []

    # overloaded constructor, this is the constructor used in main
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.directReports = [] # contains employee's subjects

    # add subject to employee's reports
    def addToReport(self, e):
        self.directReports.append(e)

    # accessor methods
    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def getReports(self):
            return self.directReports


# main method
e1 = Employee("A", "CEO")
e2 = Employee("C", "VP")
e3 = Employee("B", "VP")
e4 = Employee("F", "Manager")
e5 = Employee("G", "Manager")
e6 = Employee("D", "Manager")
e7 = Employee("E", "Manager")
e1.addToReport(e3)
e1.addToReport(e2)
e2.addToReport(e4)
e2.addToReport(e5)
e3.addToReport(e6)
e3.addToReport(e7)

organization = OrganizationStructure(e1)
organization.printLevelByLevel()


