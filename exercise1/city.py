class City :

    def __init__(self, name, department):
        """this method initializes the arguments """
        self.name = str(name) 
        self.department = int(department)

    def show_location(self):
        """this method display the name and department of the city """
        txt="The city of {} is in department {}".format(self.name, self.department)
        return txt

    def change_location(self, name, department):
        """this method overwrites the old values ​​and displays the news """
        City.__init__(self, name,department) # call the method to avoid repeating the same arguments
        txt="you move to {} in department {}".format(self.name,self.department)
        return txt
