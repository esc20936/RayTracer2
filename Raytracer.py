import random
from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 512
height = 512


# generate ground blocks randomly and add them to the scene as ground 
def generateGround(rtx, groundTexture):
    for i in range(0, 10):
        x = random.randint(-2, 2)
        z = random.randint(-10, 0)
        ground = AABB(position= (x, -1.8, z), size = (0.5,0.5,0.5), material=groundTexture)
        rtx.scene.append(ground)




# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)
grass = Material(diffuse = (0.3, 1.0, 0.3), spec = 64)


dirt = Material(spec = 64, texture = Texture("textures/dirt.bmp"), matType= OPAQUE)
water = Material(spec = 64, diffuse=(0.1,0.3,0.9), matType= REFLECTIVE)

rtx = Raytracer(width, height)

rtx.envMap = Texture("sky.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
#rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.5 ))
rtx.lights.append( PointLight(point = (-1,-1,0) ))


rtx.scene.append( AABB(position = (0,-2,-10), size = (20,0.1,20), material = water) )
generateGround(rtx, dirt)


rtx.glRender()

rtx.glFinish("output.bmp")