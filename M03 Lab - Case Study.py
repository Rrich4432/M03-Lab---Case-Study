# Ryan Richardson
# M03 Lab - Case Study


#super class
class Vehicle:
    def __init__(self, vechicle_type):
        self.vechicle_type = vechicle_type
        
# child class
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        Vehicle.__init__(self, vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
            
    def __str__(self):
        return "Vehicle type: " + self.vechicle_type + "\nYear: " + self.year + "\nMake: " + self.make + "\nModel: " + self.model + "\nNumber of doors: " + self.doors + "\nType of roof: " + self.roof
        
if __name__ == "__main__":
    # get year, make, model, doors and roof from user
    year = input("Enter year: ")
    make = input("Enter make: ")
    model = input("Enter model: ")
    doors = input("Enter number of doors: ")
    roof = input("Enter type of roof: ")
    # create an object of Vehicle type as car
    carObj = Automobile("car", year, make, model, doors, roof)
    # print details
    print("Entered details are =>")
    print(carObj)