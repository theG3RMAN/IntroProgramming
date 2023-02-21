#virtual garage program
#main default class
class Vehicle:
    
    def __init__(self, make, model): 
        self.model = model
        self.make = make
        
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model
        
#child class for car    
class Car(Vehicle): 
    def __init__(self, make, model,numDoors):
        super().__init__(make,model)
        self.numDoors = numDoors

    def getNumDoors(self):
        return self.numDoors
    
    def display_info(self):
        super().display_info()
        print(f'Number of doors: {self.getNumDoors()}')
#child class for truck   
class Truck(Vehicle):
    def __init__(self, make, model, bedLength):
        super().__init__(make, model)
       
        self.bedLength = bedLength

    def getBedLength(self):
        return self.bedLength

    def display_info(self):
        super().display_info()
        print(f'Bed length: {self.getBedLength()}')

# main function 
def main():
    while True: 
        print('Welcome to the Bellevue Virtual Garage')
        print('Enter 1 to add a car, 2 to add a truck, 3 to Exit')
        choice = input('Enter choice: ')
        if choice == '1' or choice == '2':
            
            make = input('Enter make: ')
            model = input('Enter model: ')
                        
            if choice == '1': 
                numDoors = input("Enter number of doors: ")
                newCar = Car(make,model,numDoors)
                print('Added new car to the garage!\n')
            elif choice == '2':
                bedLength = input("Enter bed length: ")
                newTruck = Truck(make,model,bedLength) 
                
                print('Added new truck to the garage!\n')
        elif choice == '3': 
            break 
        
    
main()