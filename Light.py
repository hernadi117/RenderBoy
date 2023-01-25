from Color import Color
from Point import Point
from Vector3 import Vector3


class Light(Vector3):
    """A point light source."""

    def __init__(self, position: Point, color: Color = Color.from_hex("#FFFFFF")):
        """
        :param position: Position of light source.
        :param color: The Color of the light emitted.
        """
        super().__init__(*position)
        self.origin = position
        self.color = color
