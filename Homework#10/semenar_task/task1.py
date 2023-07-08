import math


class Circkule:
    def __init__(self, radius):
        self.radius = radius

    def len_cirkul(self):
        return math.pi * 2 * self.radius

    def area_cirkul(self):
        return math.pi * self.radius ** 2
