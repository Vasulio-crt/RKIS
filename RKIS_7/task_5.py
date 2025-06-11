class FitnessCenter:
    def __init__(self, id: int, year: int, month_num: int, duration_classes: int):
        self.__ID = id
        self.year = year
        self.month_num = month_num
        self.duration = duration_classes
    
    @property
    def get_id(self):
        return self.__ID


classes = [FitnessCenter(1, 2024, 5, 120), FitnessCenter(2, 2025, 6, 90),
           FitnessCenter(3, 2024, 7, 90), FitnessCenter(4, 2025, 8, 180),
           FitnessCenter(5, 2024, 9, 60), FitnessCenter(6, 2025, 1, 60),
           FitnessCenter(7, 2024, 2, 120), FitnessCenter(8, 2025, 3, 180),
           FitnessCenter(9, 2024, 4, 90), FitnessCenter(10, 2025, 5, 60)]

years_classes_minutes = dict()
for i in classes:
    if i.year in years_classes_minutes.keys():
        years_classes_minutes[i.year] += i.duration
    else:
        years_classes_minutes[i.year] = i.duration

years_duration = min(years_classes_minutes.items())
print(f"{years_duration[0]} год: {years_duration[1]} минут")