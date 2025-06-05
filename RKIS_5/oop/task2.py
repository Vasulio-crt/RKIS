class Animal:
    def speak(self):
        print("Животное говорит")

class Dog(Animal):
    def speak(self):
        print("Гав гав")

class Cat(Animal):
    def speak(self):
        print("Мяу мяу")

cat = Cat()
dog = Dog()

cat.speak()
dog.speak()