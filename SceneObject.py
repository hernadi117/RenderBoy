from Ray import Ray
from Color import Color
from Point import Point
from Material import Material
from Vector3 import Vector3
import abc


class SceneObject(abc.ABC):
    """A scene object must implement functions to find intersection, unit normal surface vector and color at specified point,
     should have a material field.
    """

    @abc.abstractmethod
    def __init__(self, material: Material):
        self.material = material

    @abc.abstractmethod
    def intersects(self, ray: Ray) -> Color:
        """Determines whether a ray intersected the sceneobject or not, if the ray does hit then returns distance to ray origin, otherwise Inf.
        :param ray: The incoming light ray.
        """
        pass

    @abc.abstractmethod
    def normal(self, point: Point) -> Vector3:
        """Returns the unit normal vector to the object's surface the provided point.
        :param point: The point at the surface.
        """
        pass

    @abc.abstractmethod
    def color_at(self, point: Point = None) -> Color:
        pass
