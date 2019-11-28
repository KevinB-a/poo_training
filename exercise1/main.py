from city import *

lille = City("Lille", 59) # call class City with two arguments name and departement
marseille = City("Marseille", 13)
paris = City("Paris", 75)
lyon = City("Lyon", 69)
dijon = City("Dijon", 21)
print(lille.show_location()) # display name and department
print(marseille.show_location())
print(paris.show_location())
print(lyon.show_location())
print(dijon.show_location())
print(lyon.change_location("Montceau-les-mines", 71 )) # change value of object lyon
