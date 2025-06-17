sec = int(input("Введите секунды: "))
minutes = sec // 60
hours = minutes // 60

if hours > 0:
    minutes -= hours * 60
    sec -= hours * 3600 + minutes * 60
else:
    sec -= minutes * 60

sec = sec if sec > 9 else f"0{sec}"
minutes = minutes if minutes > 9 else f"0{minutes}"

print(f"{hours}:{minutes}:{sec}")