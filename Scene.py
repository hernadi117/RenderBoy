from Camera import Camera
from SceneObject import SceneObject
from Light import Light


class Scene:
    """
    The scene object that contains everything the renderer and shader will take into account.
    """
    def __init__(self, camera: Camera, objects: list[SceneObject], lights: Light, width: int, height: int) -> None:
        """
        :param camera: A camera object where the camera is located.
        :param objects: The objects to be rendered.
        :param lights: The light source.
        :param width: The width of the rendered image.
        :param height: The height of the rendered image.
        """
        self.camera = camera
        self.objects = objects
        self.width = width
        self.lights = lights
        self.height = height
