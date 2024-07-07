



class EmployeeRecord:

    def __init__(self, employee):
        self.employees = employee

    def add_employee(self, employee):
        if type(employee) == set:
            self.employees = self.employees.union(employee)
        else:
            try:
                self.employees.add(employee)
            except:
                print('You have inputted the wrong value')

    def print_employee(self):
        print(f" {'Staff ID': >10s} {'StaffName': >10s}")
        for indx, staff in enumerate(self.employees):
            print(f" {indx: >10d} {staff.Name: >10s}")

