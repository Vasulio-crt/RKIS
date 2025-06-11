class FitnessCenter:
    def __init__(self, id: int, year: int, month_num: int, duration_classes: int):
        self.__ID = id
        self.year = year
        self.month_num = month_num
        self.duration = duration_classes
    
    @property
    def get_id(self):
        return self.__ID


classes = [FitnessCenter(1, 2025, 5, 120), FitnessCenter(2, 2025, 6, 90),
           FitnessCenter(3, 2025, 7, 90), FitnessCenter(4, 2025, 8, 180),
           FitnessCenter(5, 2025, 9, 60)]

max_duration = classes[0]
min_duration = classes[0]

for i in classes:
    if max_duration.duration < i.duration:
        max_duration = i
    if min_duration.duration > i.duration:
        min_duration = i

print(f"id: {max_duration.get_id} year: {max_duration.year} month_num: {max_duration.month_num} duration_classes: {max_duration.duration}")
print(f"id: {min_duration.get_id} year: {min_duration.year} month_num: {min_duration.month_num} duration_classes: {min_duration.duration}")