class Person:
    def __init__(self, name, age):
        self.name = name           # Public attribute
        self.__age = age           # Private attribute (name mangling with __)

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Ede wow!")

    # Method to display info
    def display(self):
        print(f"Name: {self.name}, Age: {self.get_age()}")

# Create an instance of Person
person = Person("JV Sugal", 24)

# Accessing public attribute directly
print(person.name)  # Output: JV Sugal

# Accessing private attribute directly will cause an error:
# print(person.__age)  # AttributeError: 'Person' object has no attribute '__age'

# Using getter and setter for private attribute
print(person.get_age())  # Output: 24

person.set_age(24)  # Sets the age to 24
person.display()    # Output: Name: JV Sugal, Age: 24

# Trying to set a negative age will trigger validation
person.set_age(-5)  # Output: Ede wow!
