from abc import ABC, abstractmethod

# Interface (Abstract Class with only abstract methods)
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Class implementing the interface
class Car(Vehicle):

    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")


# Main Program
c1 = Car()

c1.start()
c1.stop()
