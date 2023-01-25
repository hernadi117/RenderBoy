import abc
from Ray import Ray
from Scene import Scene
from SceneObject import SceneObject
from typing import Callable
from Color import Color


class PixelShader(abc.ABC):
    """
    The abstract base-class that a PixelShader implementation must subclass from.
    """

    @abc.abstractmethod
    def __init__(self, inc_ray: Ray, obj: SceneObject, dist, scene: Scene, raytrace: Callable, depth: int, max_depth):
        """
        :param inc_ray: The incoming ray to the current pixel.
        :param obj: The object being shaded.
        :param dist: The distance to the ray's origin.
        :param scene: The current scene being rendered
        :param raytrace: The ray-tracer from the RenderEngine.
        :param depth: The current depth of raytracing recursion.
        :param max_depth: The maximum depth allowed by the raytracer.
        """
        self.inc_ray = inc_ray
        self.obj = obj
        self.dist = dist
        self.scene = scene
        self.raytrace = raytrace
        self.depth = depth
        self.MAX_DEPTH = max_depth

    @abc.abstractmethod
    def shade(self) -> Color:
        """
        The method the RenderEngine internally calls to do apply the shading. This function call must do all the shading
        that is desired.
        """
        pass

    def __call__(self, *args, **kwargs):
        self.__init__(*args, **kwargs)
