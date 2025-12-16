# Method overriding (runtime polymorphism)
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()  # Dog barks

# Method overloading simulation using *args
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(5))
print(calc.add(5,10))
print(calc.add(5,10,15))
