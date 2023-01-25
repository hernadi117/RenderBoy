from SceneObject import SceneObject
from Point import Point
from Vector3 import Vector3
from Color import Color
from Ray import Ray
from Material import Material
import numpy as np


class Sphere(SceneObject):

    def __init__(self, center: Point, radius: float, material=Material(color=Color.from_hex("#FF0000"))) -> None:
        """
        Creates a sphere to be used as a SceneObject.
        :param center: The location of sphere's center.
        :param radius: The radius of the sphere.
        :param material: The material characteristics of the sphere, must be of type Material.
        """
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray: Ray) -> Vector3:
        """
        Checks if ray intersects this sphere,
        and returns the distance to the point hit if hit, otherwise infinity.
        """
        oc: Vector3 = ray.origin - self.center
        b = 2 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius * self.radius
        discriminant = b ** 2 - 4 * c
        sqrt_discriminant = np.sqrt(np.maximum(0, discriminant))
        hit1, hit2 = (-b - sqrt_discriminant) / 2, (-b + sqrt_discriminant) / 2
        distance = np.where((hit1 > 0) & (hit1 < hit2), hit1, hit2)
        mask = (discriminant > 0) & (distance > 0)
        return np.where(mask, distance, np.inf)

    def color_at(self, point: Point) -> Color:
        """Returns the color at the provided point."""
        return self.material.color

    def normal(self, point: Point) -> Vector3:
        """Returns a unit normal vector to the sphere's surface at point provided."""
        return (point - self.center).normalize()
