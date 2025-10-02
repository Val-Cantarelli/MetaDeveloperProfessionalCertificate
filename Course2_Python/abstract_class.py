'''
Vehicle is an abstract class because the idea of vehicle is abstract. You don't create a vehicle, 
but rather a car, a boat, or a train.
They are implemented in two ways:
1. methods must be implemented in child classes (because abstract ones don't have their own implementation)
2. super() function to call parent class method.
'''

from abc import ABC, abstractmethod

# Abstract Vehicle class
class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine_on = False
    
    @abstractmethod
    def start_engine(self):
        """Abstract method that must be implemented by child classes"""
        pass
    
    @abstractmethod
    def accelerate(self):
        """Abstract method to accelerate the vehicle"""
        pass
    
    @abstractmethod
    def brake(self):
        """Abstract method to brake the vehicle"""
        pass
    
    # Concrete method that can be used by all child classes
    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            print(f"{self.brand} {self.model} engine stopped.")
        else:
            print(f"{self.brand} {self.model} engine is already off.")
    
    def info(self):
        status = "on" if self.engine_on else "off"
        print(f"Vehicle: {self.brand} {self.model} - Engine: {status}")

# Car child class
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # calling parent constructor
        self.doors = doors
    
    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"Car {self.brand} {self.model} started! Vroom vroom!")
        else:
            print(f"Car {self.brand} {self.model} engine is already running.")
    
    def accelerate(self):
        if self.engine_on:
            print(f"Car {self.brand} {self.model} accelerating on the road!")
        else:
            print("Need to start the engine first!")
    
    def brake(self):
        if self.engine_on:
            print(f"Car {self.brand} {self.model} braking... Screech!")
        else:
            print("Car is already stopped.")
    
    def open_door(self):
        print(f"Opening one of the {self.doors} doors of the car.")

# Boat child class
class Boat(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
    
    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"Boat {self.brand} {self.model} started! Marine engine running!")
        else:
            print(f"Boat {self.brand} {self.model} engine is already running.")
    
    def accelerate(self):
        if self.engine_on:
            print(f"Boat {self.brand} {self.model} sailing at full speed!")
        else:
            print("Need to start the engine first!")
    
    def brake(self):
        if self.engine_on:
            print(f"Boat {self.brand} {self.model} reducing speed on the water...")
        else:
            print("Boat is already stopped.")
    
    def anchor(self):
        print(f"Boat {self.brand} {self.model} anchored!")

# Train child
class Train(Vehicle):
    def __init__(self, brand, model, num_cars):
        super().__init__(brand, model)
        self.num_cars = num_cars
    
    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"Train {self.brand} {self.model} started! Choo choo!")
        else:
            print(f"Train {self.brand} {self.model} engine is already running.")
    
    def accelerate(self):
        if self.engine_on:
            print(f"Train {self.brand} {self.model} accelerating on tracks with {self.num_cars} cars!")
        else:
            print("Need to start the engine first!")
    
    def brake(self):
        if self.engine_on:
            print(f"Train {self.brand} {self.model} braking gradually...")
        else:
            print("Train is already stopped.")
    
    def horn(self):
        print(f"Train {self.brand} {self.model} honking: Too0000t")

# Exemple
if __name__ == "__main__":
    print("=== Abstract Classes Demonstration ===\n")
    # Attempting to instantiate abstract class (this would cause an error)
    # vehicle = Vehicle("Generic", "Abstract")  # TypeError!
    
    
    
    # Creating instances of child classes
    car = Car("Toyota", "Corolla", 4)
    boat = Boat("Yamaha", "VX Cruiser", "Gasoline")
    train = Train("CPTM", "Series 7000", 8)
    
    vehicles = [car, boat, train]
    
    print("1. Vehicle information:")
    for vehicle in vehicles:
        vehicle.info()
    
    print("\n2. Starting engines:")
    for vehicle in vehicles:
        vehicle.start_engine()
    
    print("\n3. Accelerating:")
    for vehicle in vehicles:
        vehicle.accelerate()
    
    print("\n4. Braking:")
    for vehicle in vehicles:
        vehicle.brake()
    
    print("\n5. Specific methods:")
    car.open_door()
    boat.anchor()
    train.horn()
    
    print("\n6. Stopping engines:")
    for vehicle in vehicles:
        vehicle.stop_engine()
    
    print("\n=== Demonstrated concepts ===")
    print("Abstract class with ABC")
    print("Abstract methods with @abstractmethod")
    print("Shared concrete methods")
    print("Using super() in child classes")
    print("Polymorphism - same method, different behaviors")


