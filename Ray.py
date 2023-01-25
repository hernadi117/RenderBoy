from Vector3 import Vector3
from Point import Point


class Ray:
    """Represents a light ray."""
    def __init__(self, origin: Point, direction: Vector3) -> None:
        """
        :param origin: The location that the light ray originated from.
        :param direction: The direction the light ray is headed.
        """
        self.origin = origin
        self.direction = direction.normalize()
