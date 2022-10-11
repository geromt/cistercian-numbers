import xml.etree.ElementTree as Et

# TODO: Documentation


class DrawSVG:
    def __init__(self, width, height):
        self.doc = Et.Element("svg", width=str(width), height=str(height),
                              version='1.1', xmlns='http://www.w3.org/2000/svg')
        self._width = width
        self._height = height

    def add_background(self, background_color):
        Et.SubElement(self.doc, "rect", x=str(0), y=str(0),
                      width=str(self._width), height=str(self._height),
                      style=f"fill:{background_color}")

    def add_line(self, x1, y1, x2, y2, color, stroke_width=10):
        Et.SubElement(self.doc, "line", x1=str(x1), y1=str(y1), x2=str(x2),
                      y2=str(y2),
                      style=f"stroke:{color};stroke-width:{stroke_width}")

    def write(self, path):
        with open(path, "w") as f:
            f.write("\n")
            f.write("\n")
            f.write(Et.tostring(self.doc, encoding="unicode"))

