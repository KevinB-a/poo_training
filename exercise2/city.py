from cities import *

class City :

    def __init__(self, cities):
        """this method initializes the arguments """
        self.name = None
        self.department = None
        self.country = None
        self.population = None
        self.mayor = None
        self.capital = None
        for key_name, value_name in cities.items():
            if hasattr(self, key_name):
                setattr(self, key_name, value_name)


    def show_location(self):
        """this method display the name and department of the city """
        text="The city of {} is in department {}".format(self.name, self.department)
        return text

    def change_location(self, name, department):
        """this method overwrites the old values ​​and displays the news """
        self.name =name
        self.department = department
        txt="you move to {} in department {}".format(self.name,self.department)
        return text

    def show_information(self):
        text="City's information \n\
        name : {} \n\
        department : {} \n\
        country : {} \n\
        population : {} \n\
        mayor : {} \n\
        capital : {} \n "
        print(text.format(self.name, self.department, self.country, self.population, self.mayor, self.capital))
