class KgToPounds:
    def __init__(self, kg=0):
        self.kg = kg

    def to_pounds(self):
        self.pound = self.kg * 2.205
        print("Pound:", self.pound)
    
    def set_kg(self, kg):
        self.kg = kg
    
    def get_kg(self):
        print("KG:", self.kg)

# Я так и не понял что надо реализовать

cls = KgToPounds(20)
cls.to_pounds()
cls.set_kg(10)
cls.get_kg()