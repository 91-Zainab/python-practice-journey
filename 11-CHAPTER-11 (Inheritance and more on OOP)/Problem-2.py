# Create a class 'pets' from a class 'Animals' and further create a class 'dog' from 'pets'. Add a method 'Bark' to class 'dog'.

class animals:
        pass

class pets(animals):
    pass

class dog(pets):
    @staticmethod
    def bark():
         print("Bow Bow!")

d = dog()
d.bark()
