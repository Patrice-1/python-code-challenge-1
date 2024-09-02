#class named Car with the following attributes: make, model, year. Implement a method named display_info that prints out the car's information.

class Car:
    def __init__(self, make, model, year):

        #initialize a Car instance with given parameters above
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):

        #method to display the car's information
        print(f"Make: {self.make} |", f"Model: {self.model} |", f"Year: {self.year}")


#create an instance of Car and test the display_info method
my_car = Car("Tesla", "Model3", 2024)
my_car.display_info()


my_car1=Car("BMW", "3 Series", 2020)
my_car1.display_info()

