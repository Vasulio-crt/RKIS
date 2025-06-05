def point_in_circle(point: tuple[float, float], R: float) -> bool:
    if point[0] ** 2 + point[1] ** 2 <= R ** 2:
        return True
    else:
        return False

circle_r = 2
A = (1.5, 1.5)
print(point_in_circle(A, circle_r))