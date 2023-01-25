from Color import Color
from Material import Material
from Point import Point
from Sphere import Sphere
import numpy as np


class CheckerBoardSphere(Sphere):
    """A Sphere with a checkerboard pattern."""

    def __init__(self, center: Point, radius: float, material=Material(color=Color.from_hex("#FF0000"))) -> None:
        super().__init__(center, radius, material)

    def color_at(self, point):
        pattern = (np.floor((point.x * 2)) % 2) == (np.floor((point.z * 2)) % 2)
        return self.material.color * pattern
