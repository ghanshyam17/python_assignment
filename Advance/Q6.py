# Single Inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Parent:", self.name)

class Child1(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print("Child:", self.name, "Age:", self.age)

# Multiple Inheritance
class Father:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Father:", self.name)

class Mother:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Mother:", self.name)

class Child2(Father, Mother):
    def __init__(self, name, age):
        Father.__init__(self, name)
        Mother.__init__(self, name)
        self.age = age

    def display(self):
        print("Child:", self.name, "Age:", self.age)

# Multilevel Inheritance
class Grandparent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Grandparent:", self.name)

class Parent(Grandparent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print("Parent:", self.name, "Age:", self.age)

class Child3(Parent):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby

    def display(self):
        print("Child:", self.name, "Age:", self.age, "Hobby:", self.hobby)



if __name__ == "__main__":
    # Single Inheritance
    print("Single Inheritance:")
    parent_obj = Parent("Alice",50)
    parent_obj.display()

    child1_obj = Child1("Bob", 5)
    child1_obj.display()

    # Multiple Inheritance
    print("\nMultiple Inheritance:")
    father_obj = Father("John")
    father_obj.display()

    mother_obj = Mother("Jane")
    mother_obj.display()

    child2_obj = Child2("Lucy", 7)
    child2_obj.display()

    # Multilevel Inheritance
    print("\nMultilevel Inheritance:")
    grandparent_obj = Grandparent("Tom")
    grandparent_obj.display()

    parent_obj = Parent("Michael", 40)
    parent_obj.display()

    child3_obj = Child3("Sophia", 12, "Gardening")
    child3_obj.display()
