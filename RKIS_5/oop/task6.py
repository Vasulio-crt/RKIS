class Nikola:
    __slots__ = ('name', 'age')
    
    def __init__(self, name: str, age: int):
        if name.lower() != "николай":
            print(f"Я не {name}, а Николай")
        self.name = "Николай"
        self.age = age


nikolay = Nikola('Максим', 30)
print(nikolay.name)

nikolay2 = Nikola('Николай', 26)
print(nikolay2.name)