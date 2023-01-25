from PixelShader import PixelShader
from SceneObject import SceneObject
from Ray import Ray
from Scene import Scene
from Vector3 import Vector3
from Color import Color
from functools import reduce
import numpy as np


class BlinnPhongShader(PixelShader):
    """
    A shader that implements shadows, Blinn-Phong specular shading and Lambert diffuse shading.
    """

    def __init__(self, inc_ray: Ray, obj: SceneObject, dist, scene: Scene, raytrace, depth, max_depth) -> None:
        """
        Creates the shader object for provided color-pixel-data.
        :param inc_ray: The incoming ray.
        :param obj: The object being shaded.
        :param dist: The distance to ray origin.
        :param scene: The scene being rendered.
        :param raytrace: The raytracer function by the main RenderEngine.
        :param depth: The depth of current ray tracing.
        :param max_depth: The maximum allowable depth for the ray-tracing recursion.
        """
        self.obj = obj
        self.inc_ray = inc_ray
        self.raytrace = raytrace
        self.depth = depth
        self.max_depth = max_depth
        self.scene = scene
        self.intersection_point = inc_ray.origin + inc_ray.direction * dist
        self.normal = obj.normal(self.intersection_point)
        self.to_light = (scene.lights - self.intersection_point).normalize()
        self.to_camera = (scene.camera - self.intersection_point).normalize()
        self.color = self.obj.material.ambient * Color(1, 1, 1)
        self.new_ray_origin = self.intersection_point + self.normal * 0.0001

    def shadows(self):
        """Calculates a shadow mask."""
        dist_to_light = [obj.intersects(Ray(self.new_ray_origin, self.to_light)) for obj in self.scene.objects]
        closest = reduce(np.minimum, dist_to_light)
        shadow_mask = dist_to_light[self.scene.objects.index(self.obj)] == closest
        return shadow_mask

    def diffuse_shader(self):
        """Calculates the Lambert shading color."""
        lambert = np.maximum(self.normal.dot(self.to_light), 0)
        self.color += self.obj.color_at(self.intersection_point) * self.obj.material.diffuse * lambert

    def specular_shader(self):
        """Calculates the specular shading."""
        phong_term = self.normal.dot((self.to_light + self.to_camera).normalize())
        self.color += self.scene.lights.color * self.obj.material.specular * np.power(np.clip(phong_term, 0, 1), 50)

    def shade(self) -> Color:
        """Applies shading to pixel-data."""
        shadow_mask = self.shadows()
        self.diffuse_shader()
        self.specular_shader()
        if self.depth < self.max_depth:
            new_dir = (self.inc_ray.direction - self.normal * 2 * self.inc_ray.direction.dot(self.normal)).normalize()
            new_ray = Ray(self.new_ray_origin, new_dir)
            self.color += self.raytrace(new_ray, self.depth + 1) * self.obj.material.reflection
        return self.color * shadow_mask

