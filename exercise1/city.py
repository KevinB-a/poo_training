class City :

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def show_location(self):
        txt="The city of {} is in department {}".format(self.name, self.department)
        return txt

    def change_location(self, name, department):
        self.name =name
        self.department = department
        txt="you move to {} in department {}".format(self.name,self.department)
        return txt
