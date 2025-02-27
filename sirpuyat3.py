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
            print("Ako ay isang kupal!")

    # Method to display info
    def display(self):
        print(f"Name: {self.name}, Age: {self.get_age()}")

# Create an instance of Person
person = Person("Patrick Kupal", 23)

# Accessing public attribute directly
print(person.name)  # Output: Patrick Kupal

# Accessing private attribute directly will cause an error:
# print(person.__age)  # AttributeError: 'Person' object has no attribute '__age'

# Using getter and setter for private attribute
print(person.get_age())  # Output: 23

person.set_age(23)  # Sets the age to 23
person.display()    # Output: Name: Patrick Kupal, Age: 23

# Trying to set a negative age will trigger validation
person.set_age(-5)  # Output: Ako ay isang kupal!
