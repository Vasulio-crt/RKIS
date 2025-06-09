from datetime import datetime as dt

class Task:
    def __init__(self, DS, DF, Des):
        self.DateStart = DS
        self.DateFinish = DF
        self.Description = Des

task = [Task(dt(2025, 6, 7, 10), dt(2025, 6, 7, 12), "Практическое занятие 1"),
        Task(dt(2025, 6, 7, 13), dt(2025, 6, 7, 15), "Контрольная работа 1"),
        Task(dt(2025, 6, 6, 9), dt(2025, 6, 6, 11), "Теоретическое занятие 1"),
        Task(dt(2025, 6, 10, 9), dt(2025, 6, 10, 11), "Практическое занятие 2"),
        Task(dt(2025, 6, 11, 9), dt(2025, 6, 11, 11), "Практическое занятие 3")]

min_date = task[0]
for t in task:
    if min_date.DateFinish > t.DateFinish:
        min_date = t

print(f"{min_date.Description}: {min_date.DateStart} - {min_date.DateFinish}")