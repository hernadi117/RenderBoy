from Color import Color


class Material:
    """The material properties of an object, which dictates how the object's surface is shaded."""

    def __init__(self, color=Color.from_hex("#0000FF"), ambient=0.05, diffuse=0.5, specular=0.5, reflection=0.5):
        """
        :param color: The color of the object.
        :param ambient: The ambient parameter.
        :param diffuse: The diffuse shading parameter of the object.
        :param specular: The specular shading parameter of the object.
        :param reflection: The reflective parameter of the object.
        """
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection
