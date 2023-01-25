# RenderBoy

## RenderBoy is a fast(ish) unopiniated ray tracer engine.

![Rendering by RenderBoy that shows two spheres on a summer day.](https://i.imgur.com/FhiP1CU.png)

A nice summer day - RenderBoy. &copy; RenderBoy

RenderBoy is a fast(ish) ray tracer engine which gets it speed by leveraging the vectorization capabilities of BLAS through the Python library `NumPy`. No other necessary dependencies are needed, unless you want to use the default image writer which uses the library `Pillow`.

The internal engine of RenderBoy will do typical ray tracing, which includes:

- Light-geometry intersection
- Reflections (depth may be specified)

RenderBoy works with typical dependency injection; this is true for the scene you provide him, and the shader chosen. The decoupling from the shader and ray tracer engine allows RenderBoy to use a wide variety of shaders, and you may write your own shaders that RenderBoy then can use. To write your own shaders, you must make sure to inherit from `PixelShader` properly.

# Documentation
RenderBoy is backed up by a 3D Vector container `Vector3`:

```python
class Vector3:
    """A 3-dimensional vector container."""
    def __init__(self, x: float, y: float, z: float) -> None:
        """
        :param x: X-coordinate.
        :param y: Y-coordinate.
        :param z: Z-coordinate.
        """
    def dot(self, other: Vector3) -> float:
        """Computes the standard dot product of the two vectors."""
        
    def norm(self) -> float:
        """Returns the Euclidean norm of the vector."""

    def components(self) -> tuple[float, float, float]:
        return self.x, self.y, self.z

    def normalize(self) -> Vector3:
        """Normalizes the vector, effectively turning it into a unit vector."""

    def __add__(self, other: Vector3) -> Vector3:
        """Operator overloading for the class so two vectors can be added with the + operator."""

    def __sub__(self, other: Vector3) -> Vector3:
        """Operator overloading for the class so two vectors can be subtracted with the - operator."""

    def __mul__(self, other: float) -> Vector3:
        """Operator overloading for the class so scalar-vector multiplication can be done with the * operator."""

    def __rmul__(self, other: float):
        """Operator overloading such that scalar-vector multiplication is associative."""

    def __truediv__(self, other: float) -> Vector3:
        """Operator overloading for the class so scalar-vector division can be done with the / operator."""

    def __str__(self) -> str:
        """Returns a string representation of the vector."""

    def __repr__(self) -> str:
        """Returns a string of the object creation of the vector, such that it may be readily reproduced."""

    def __iter__(self) -> Generator[float, None, None]:
        """Returns a generator that yields the elements of the vector in standard order."""

    def __eq__(self, other: Vector3) -> bool:
        """Tests element-wise equality of two vectors."""

    def __ne__(self, other):
        """Tests element-wise inequality of two vectors."""

    def extract(self, mask):
        """Extracts elements from the container as specified in the provided mask."""

    def place(self, mask):
        """Inserts element into the container as specified in the provided mask."""
```

Several of RenderBoy's objects subclass from `Vector3`, such as `Color`, `Point`, `Camera`, `Light` and `Ray`:
```python
class Color(Vector3):
    """Container to represent color value of a pixel, as an RGB triplet."""

    def __init__(self, x: float, y: float, z: float) -> None:
        """
        :param x: X-coordinate.
        :param y: Y-coordinate.
        :param z: Z-coordinate.
        """

    def from_hex(cls, hex_color: str) -> Color:
        """Creates a Color object from a hex-value."""
```
```python
class Point(Vector3):
    """Representation of a 3D Cartesian coordinate point."""
    
    def __init__(self, x: float, y: float, z: float) -> None:
        """
        :param x: X-coordinate.
        :param y: Y-coordinate.
        :param z: Z-coordinate.
        """
```
```python
class Camera(Point):
    """The camera object."""
    
    def __init__(self, x: float, y: float, z: float) -> None:
        """
        :param x: X-coordinate.
        :param y: Y-coordinate.
        :param z: Z-coordinate.
        """
```
```python
class Light(Vector3):
    """A point light source."""

    def __init__(self, position: Point, color: Color = Color.from_hex("#FFFFFF")):
        """
        :param position: Position of light source.
        :param color: The Color of the light emitted, default white light.
        """
```
```python
class Ray:
    """Represents a light ray."""
    
    def __init__(self, origin: Point, direction: Vector3) -> None:
        """
        :param origin: The location that the light ray originated from.
        :param direction: The direction the light ray is headed, will be normalized.
        """
```

To render a scene, you need to provide RenderBoy with a `Scene` object:
```python
class Scene:
    """
    The scene object that contains everything the renderer and shader will take into account.
    """
    def __init__(self, camera: Camera, objects: list[SceneObject], lights: Light, width: int, height: int) -> None:
        """
        :param camera: A camera object where the camera is located.
        :param objects: The list of objects to be rendered.
        :param lights: The light source.
        :param width: The width of the rendered image.
        :param height: The height of the rendered image.
        """
```

Objects to be rendered by the scene must subclass from the abstract base class `SceneObject`:

```python
class SceneObject(abc.ABC):
    """A scene object to be rendered must implement functions to find intersection, unit normal surface vector and color at specified point,
     should have a material field.
    """

    def __init__(self, material: Material):
        """
        :param Material: The material of the SceneObject.

    def intersects(self, ray: Ray) -> Vector3:
    """Determines whether a ray intersected the sceneobject or not, if the ray does hit then returns distance to ray origin, otherwise Inf.
    :param ray: The incoming light ray.
    """
    
    def normal(self, point: Point) -> Vector3:
        """Returns the unit normal vector to the object's surface the provided point.
        :param point: The point at the surface.
        """
        
    def color_at(self, point: Point = None) -> Color:
        """Returns the color at the provided point. If no point provided should act as an object with the same color everywhere.
        :param point: The point at the surface.
        """
```
RenderBoy comes with two default geometry primitives, `Sphere` and `CheckerBoardSphere` which is properly subclassed from the `SceneObject` abstract base class.
```python
class Sphere(SceneObject):

    def __init__(self, center: Point, radius: float, material=Material(color=Color.from_hex("#FF0000"))) -> None:
        """
        Creates a sphere to be used as a SceneObject.
        :param center: The location of sphere's center.
        :param radius: The radius of the sphere.
        :param material: The material characteristics of the sphere, must be of type Material.
        """

    def intersects(self, ray: Ray) -> Vector3:
        """
        Checks if ray intersects this sphere,
        and returns the distance to the point hit if hit, otherwise infinity.
        """

    def color_at(self, point: Point) -> Color:
        """Returns the color at the provided point."""

    def normal(self, point: Point) -> Vector3:
        """Returns a unit normal vector to the sphere's surface at point provided."""
```
Every `SceneObject` needs a material in order for the shader to shade the object properly. Please note that there is no specific requirement as to what the `Material` class must include as this is decided by the shader. RenderBoy makes no guarantee the chosen shader can render the material properties you may define. The `Material` class below is merely an example `Material` which the included shader, `BlinnPhongShader`, may render properly.

```python
    def __init__(self, color=Color.from_hex("#0000FF"), ambient=0.05, diffuse=1.0, specular=1.0, reflection=0.3):
        """
        :param color: The color of the object, default red.
        :param ambient: The ambient parameter, default 0.05.
        :param diffuse: The diffuse shading parameter of the object, default 0.5.
        :param specular: The specular shading parameter of the object, default 0.5.
        :param reflection: The reflective parameter of the object, default 0.3.
        """
```

RenderBoy makes no explicit assumptions on which shader to be used by the engine, but does require the shader to adhere to a simple interface as described by
the abstract base class of `PixelShader`.

```python
class PixelShader
    """
    The abstract base-class that a PixelShader implementation must subclass from.
    """
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
        
        def shade(self) -> Color:
        """
        The method the RenderEngine internally calls to do apply the shading. This function call must do all the shading
        that is desired.
        """
```
The included `BlinnPhongShader` shows a proper subclass that adheres to the required shader interface:

```python
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

    def shadows(self):
        """Calculates a shadow mask."""

    def diffuse_shader(self):
        """Calculates the Lambert shading color."""
        
    def specular_shader(self):
        """Calculates the specular shading."""

    def shade(self):
        """Applies shading to pixel-data."""
```
The render engine of RenderBoy:
```python
class RenderEngine:
    """The main render engine, which does the ray-tracing."""

    def __init__(self, scene: Scene, shader: Type[PixelShader], max_depth=3) -> None:
        """
        :param scene: The scene to be rendered, must be of type Scene.
        :param shader: The pixel shader to be used for shading, must be of type PixelShader and adhere to PixelShader contract.
        :param max_depth: The number of reflections the engine will calculate at most.
        """
        
    def render(self):
        """Starts the render with the provided parameters."""

    @staticmethod
    def save_as(color: Color, width, height, filename: str):
        """
        Allows the color-data generated by RenderEngine to be saved a common file format.
        :param color: Pixel color-data from the completed render.
        :param width: Width used in the render.
        :param height: Height used in the render.
        :param filename: Filename to be saved as, must include file-format.

    def render_and_save_as(self, filename: str):
        """
        Starts the render, and immediately saves the result to file when completed.
        Warning: Should not be used in conjunction with render(), unless a re-render is desired.
        :param filename: Filename to be saved as, must include file-format.
```

## Example
The example code belows shows how to do a typical render with RenderBoy.
```python
from CheckerBoardSphere import CheckerBoardSphere
from RenderEngine import RenderEngine
from Scene import Scene
from Sphere import Sphere
from Point import Point
from Color import Color
from Material import Material
from Light import Light
from Camera import Camera
from BlinnPhongShader import BlinnPhongShader

WIDTH = 640
HEIGHT = 480

objects = [
    Sphere(Point(0.75, 0, 1), 0.6, Material(color=Color(0, 0, 1), reflection=0.3, diffuse=0.5, specular=0.5)),
    CheckerBoardSphere(Point(0, -99999.5, 0), 99999, Material(color=Color(0.75, 0.75, 0.75), reflection=0.7)),
    Sphere(Point(-0.75, 0, 1), 0.5, Material(color=Color(.5, .25, .5), reflection=0.7))
]

camera = Camera(0, 0.35, -1)
light = Light(Point(5, 5, -10), color=Color.from_hex("#FFFF00"))
my_scene = Scene(camera, objects, light, WIDTH, HEIGHT)

engine = RenderEngine(my_scene, BlinnPhongShader, max_depth=3)
color = engine.render_and_save_as("blood_moon.png")
```
![Render by RenderBoy that shows two sphere with a blood moon.](https://i.imgur.com/tImKJLt.png)

## Semantic Version
RenderBoy follows semantic versioning, and is currently 1.0.0.
