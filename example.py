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

WIDTH = 1920
HEIGHT = 1080

objects = [
    Sphere(Point(0.75, 0, 1), 0.6, Material(color=Color(0, 0, 1), reflection=0.3, diffuse=0.5, specular=0.5)),
    CheckerBoardSphere(Point(0, -99999.5, 0), 99999, Material(color=Color(0.75, 0.75, 0.75), reflection=0.7)),
    Sphere(Point(-0.75, 0, 1), 0.5, Material(color=Color(.5, .25, .5), reflection=0.7))
]

camera = Camera(0, 0.35, -1)
light = Light(Point(5, 5, -10), color=Color.from_hex("#FFFF00"))
my_scene = Scene(camera, objects, light, WIDTH, HEIGHT)

engine = RenderEngine(my_scene, BlinnPhongShader, max_depth=2)
color = engine.render_and_save_as("blood_moon.png")
