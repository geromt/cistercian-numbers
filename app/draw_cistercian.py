from math import floor, log10

from drawSVG import DrawSVG

# TODO: documentation
# TODO: correct cut borders
# TODO: Decorator for add_line to add the color and stroke in each call
# TODO: INV. way to share already calculated values


class DrawCistercian:
    def __init__(self, width, height, background, color, stroke):
        self._mid_x = width / 2  # Middle point of the x coordinate
        self._high_y = height / 8  # Higher point of y coordinate
        self._low_y = height - self._high_y  # Lower point of y coordinate
        # length of lines
        self._length = width / 3 if width < height else height / 3
        # length of the bigger middle line
        self._big_length = self._low_y - self._high_y

        self.color = color
        self.stroke = stroke

        self.canvas = DrawSVG(width, height)
        self.canvas.add_background(background)
        self.canvas.add_line(self._mid_x, self._high_y,
                             self._mid_x, self._low_y,
                             self.color, self.stroke)

        # Dictionary to call each method from the integer
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
        if n == 0:
            return None

        for i in range(floor(log10(n)) + 1):
            r = n % 10
            if r != 0:
                self.draw_methods[r](i)
            n = n // 10

    def save(self, path):
        self.canvas.write(path)

    def draw_1(self, power=0):
        y = self._calc_outside_y(power)
        x2 = self._calc_outside_x(power)
        self.canvas.add_line(self._mid_x, y, x2, y, self.color, self.stroke)

    def draw_2(self, power=0):
        y = self._calc_inside_y(power)
        x2 = self._calc_outside_x(power)
        self.canvas.add_line(self._mid_x, y, x2, y, self.color, self.stroke)

    def draw_3(self, power=0):
        y1 = self._calc_outside_y(power)
        x2 = self._calc_outside_x(power)
        y2 = self._calc_inside_y(power)
        self.canvas.add_line(self._mid_x, y1, x2, y2, self.color, self.stroke)

    def draw_4(self, power=0):
        y1 = self._calc_inside_y(power)
        x2 = self._calc_outside_x(power)
        y2 = self._calc_outside_y(power)
        self.canvas.add_line(self._mid_x, y1, x2, y2, self.color, self.stroke)

    def draw_5(self, power=0):
        self.draw_4(power)
        self.draw_1(power)

    def draw_6(self, power=0):
        x = self._calc_outside_x(power)
        y1 = self._calc_outside_y(power)
        y2 = self._calc_inside_y(power)
        self.canvas.add_line(x, y1, x, y2, self.color, self.stroke)

    def draw_7(self, power=0):
        self.draw_1(power)
        self.draw_6(power)

    def draw_8(self, power=0):
        self.draw_2(power)
        self.draw_6(power)

    def draw_9(self, power=0):
        self.draw_7(power)
        self.draw_2(power)

    def _calc_outside_y(self, power):
        return self._high_y + ((0 if power <= 1 else 1) * self._big_length)

    def _calc_outside_x(self, power):
        return self._mid_x + ((1 if power % 2 == 0 else -1) * self._length)

    def _calc_inside_y(self, power):
        # I don't use ternary operator for readability
        if power <= 1:
            return self._high_y + self._length
        else:
            return self._low_y - self._length
