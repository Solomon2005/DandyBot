steps = (
    ["right"] * 9 + ["up"] * 7 + ["left"] * 8 + ["right"] * 12 +
    ["up"] * 5 + ["right"] * 1 + ["down"] * 6 + ["right"] * 5 +
    ["down"] * 7 + ["right"] * 8 + ["up"] * 8 + ["left"] * 7 +
    ["up"] * 8 + ["right"] * 7 + ["up"] * 8 + ["left"] * 8 +
    ["down"] * 8 + ["left"] * 11 + ["up"] * 8 + ["left"] * 8 +
    ["down"] * 8
)
step = 0


points = [
    # правый верхний угол
    (9, 7), (9, 5), (10, 5), (10, 3), (9, 3), (9, 1), (15, 1), (15, 5),
    (12, 5), (12, 2), (12, 3), (14, 3), (8, 3),
    # левый верхний угол
    (7, 3), (7, 1), (1, 1), (1, 5), (4, 5), (4, 2), (4, 3), (2, 3), (6, 3),
    (6, 5), (7, 5), (7, 7),
    # центр и левый нижний угол
    (6, 7), (6, 9), (7, 9), (7, 11), (6, 11), (6, 13), (2, 13), (4, 13),
    (4, 14), (4, 9), (4, 11), (1, 11), (1, 15), (7, 15), (7, 13),
    # правый нижний угол
    (14, 13), (12, 13), (12, 14), (12, 13), (12, 11), (15, 11), (15, 15),
    (9, 15), (9, 13), (10, 13), (10, 11), (9, 11), (9, 9),
    # проход справа и золото в столбце x = 12
    (10, 9), (10, 8), (12, 8), (12, 10), (12, 6),
]
i = 0


def script(check, x, y):
    global step, i

    if check("gold", x, y):
        return "take"

    # Уровень 1
    if check("level") == 1:
        if x < 23:
            return "right"
        return "down"

    # Уровень 2
    if check("level") == 2:
        c = x % 8
        if c == 1:
            return "up" if y > 1 else "right"
        if c == 5:
            return "down" if y < 9 else "right"
        return "right"

    # Уровень 3
    if check("level") == 3:
        if step < len(steps):
            step += 1
            return steps[step - 1]

    # Уровень 4
    if check("level") == 4:


        if x < 19 and y <= 4:
            if y == 1 and x < 4:
                return "right"
            return "down" if y < 4 else "right"


        if x >= 19 and y <= 8:
            if x == 19 and 1 < y <= 4:
                return "up"
            if y == 1:
                return "right" if x < 26 else "down"
            if y == 8:
                if check("gold", 19, 8):
                    return "left"
                return "right" if x < 22 else "down"
            return "down"


        if x >= 19 and y >= 16:
            if x == 19:
                if check("gold", 19, 16):
                    return "up"
                return "down" if y < 20 else "left"
            if x == 26 and y < 23:
                return "down"
            if y == 16:
                return "right"
            return "left"


        if y == 20 and x > 8:
            return "left"


        if x <= 8 and y >= 16:
            if x == 8 and y == 23:
                return "pass"
            if y == 23:
                return "right"
            if x == 8 and y > 16:
                return "up"
            if y == 16 and x > 1:
                return "left"
            return "down"


        if 10 <= x <= 17 and 7 <= y <= 17:
            if y == 7:
                return "left" if x > 10 else "down"
            if x == 17:
                return "right" if y == 13 else "up"
            if x == 10:
                return "down" if y < 17 else "right"
            return "right"


        if x >= 18 and y == 12:
            return "left"
        if x >= 18 and y == 13:
            return "right" if x < 22 else "down"


        if x == 22 and y < 16:
            return "down"

    # Уровень 5
    if check("level") == 5:
        if i < len(points) and (x, y) == points[i]:
            i += 1
        if i < len(points):
            tx, ty = points[i]
            if x < tx:
                return "right"
            if x > tx:
                return "left"
            if y < ty:
                return "down"
            if y > ty:
                return "up"

    return "pass"