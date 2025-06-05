class KgToPounds:
    def __init__(self, kg=0):
        self.__kg = kg

    @property
    def pound(self):
        return self.__kg * 2.205
    
    @property
    def kg(self):
        return self.__kg
    
    @kg.setter
    def kg(self, num):
        self.__kg = num


cls = KgToPounds(20)
print(cls.kg)
cls.kg = 100
print("pound:", cls.pound, "kg:", cls.kg)