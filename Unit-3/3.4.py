#4 Write a program to make use of inner class


class Computer:
    def __init__(self, brand, model, processor_name):
        self.brand = brand
        self.model = model
        # Create an instance of the inner class during initialization
        self.cpu = self.CPU(processor_name)

    def display_specs(self):
        print(f"Computer: {self.brand} {self.model}")
        # Accessing method from the inner class instance
        self.cpu.display_details()

    class CPU:
        """This is the Inner Class"""
        def __init__(self, name):
            self.name = name
            self.cores = 8
            self.clock_speed = "3.5 GHz"

        def display_details(self):
            print(f"Processor: {self.name} | Cores: {self.cores} | Speed: {self.clock_speed}")

# --- Using the classes ---

# Method 1: Create the outer class, which automatically creates the inner class
my_laptop = Computer("Fruit", "Air Pro", "M3 Max")
my_laptop.display_specs()

# Method 2: Access the inner class directly via the outer class name
custom_cpu = Computer.CPU("Intel i9")
custom_cpu.display_details()
