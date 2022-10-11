from drawSVG import DrawSVG

# TODO: documentation
# TODO: improve code
# TODO: improve drawing with different dimensions


class DrawCistercian:
    def __init__(self, width, height, background, color, stroke):
        self.x = width / 2
        self.y1 = height / 8
        self.y2 = height - self.y1
        self.xw = width / 3
        self.yw = 0.75 * height

        self.color = color
        self.stroke = stroke

        self.draw = DrawSVG(width, height)
        self.draw.add_background(background)
        self.draw.add_line(self.x, self.y1, self.x, self.y2, self.color,
                           self.stroke)

        self.draw_methods = {
            1: self.draw_1,
            2: self.draw_2,
            3: self.draw_3,
            4: self.draw_4,
            5: self.draw_5,
            6: self.draw_6,
            7: self.draw_7,
            8: self.draw_8,
            9: self.draw_9
        }

    def draw_number(self, n):
        for i in range(4):
            m = n % 10
            if m != 0:
                self.draw_methods[m](i)
            n = n // 10

    def save(self, path):
        self.draw.write(path)

    def draw_1(self, power=0):
        y = self.y1 + (0 if power <= 1 else 1) * self.yw
        x2 = self.x + (1 if power % 2 == 0 else -1) * self.xw
        self.draw.add_line(self.x, y, x2, y, self.color, self.stroke)

    def draw_2(self, power=0):
        y = self.y1+self.xw if power <= 1 else self.y2-self.xw
        x2 = self.x + (1 if power % 2 == 0 else -1) * self.xw
        self.draw.add_line(self.x, y, x2, y, self.color, self.stroke)

    def draw_3(self, power=0):
        y1 = self.y1 + (0 if power <= 1 else 1) * self.yw
        x2 = self.x + (1 if power % 2 == 0 else -1) * self.xw
        y2 = self.y1+self.xw if power <= 1 else self.y2-self.xw
        self.draw.add_line(self.x, y1, x2, y2, self.color, self.stroke)

    def draw_4(self, power=0):
        y1 = self.y1+self.xw if power <= 1 else self.y2-self.xw
        x2 = self.x + (1 if power % 2 == 0 else -1) * self.xw
        y2 = self.y1 + (0 if power <= 1 else 1) * self.yw
        self.draw.add_line(self.x, y1, x2, y2, self.color, self.stroke)

    def draw_5(self, power=0):
        self.draw_4(power)
        self.draw_1(power)

    def draw_6(self, power=0):
        x = self.x + (1 if power % 2 == 0 else -1) * self.xw
        y1 = self.y1 + (0 if power <= 1 else 1) * self.yw
        y2 = self.y1+self.xw if power <= 1 else self.y2-self.xw
        self.draw.add_line(x, y1, x, y2, self.color, self.stroke)

    def draw_7(self, power=0):
        self.draw_1(power)
        self.draw_6(power)

    def draw_8(self, power=0):
        self.draw_2(power)
        self.draw_6(power)

    def draw_9(self, power=0):
        self.draw_7(power)
        self.draw_2(power)
