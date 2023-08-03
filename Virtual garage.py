class Vehicle:
    def __init__(self):
        self.VehicleMake = ""
        self.VehicleModel = ""

    def SetVehicleMake(self, make):
        self.VehicleMake = make

    def SetVehicleModel(self, model):
        self.VehicleModel = model

    def GetVehicleMake(self):
        return self.VehicleMake

    def GetVehicleModel(self):
        return self.VehicleModel


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.CarDoor = ""

    def SetCarDoor(self, doors):
        self.CarDoor = doors

    def GetCarDoor(self):
        return self.CarDoor


class Pickup(Vehicle):
    def __init__(self):
        super().__init__()
        self.BedLength = ""

    def SetBedLength(self, length):
        self.BedLength = length

    def GetBedLength(self):
        return self.BedLength


def main():
    car = Car()
    pickup = Pickup()

    while True:
        print("1. Add a car")
        print("2. Add a pickup truck")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            make = input("Enter the make of the car: ")
            model = input("Enter the model of the car: ")
            doors = input("Enter the number of doors of the car: ")

            car.SetVehicleMake(make)
            car.SetVehicleModel(model)
            car.SetCarDoor(doors)

            print("Car added successfully!")

        elif choice == "2":
            make = input("Enter the make of the pickup truck: ")
            model = input("Enter the model of the pickup truck: ")
            length = input("Enter the length of the truck bed: ")

            pickup.SetVehicleMake(make)
            pickup.SetVehicleModel(model)
            pickup.SetBedLength(length)

            print("Pickup truck added successfully!")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()