import random
from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 256
height = 256


# generate ground blocks randomly and add them to the scene as ground
def generateGround(rtx, groundTexture, sandTexture):
    for i in range(-6, 2):
        rtx.scene.append(
            AABB(position= (i/2, -1.8, -5), size = (0.5,0.5,0.5), material=groundTexture)
        )
    for i in range(2,7):
        rtx.scene.append(
            AABB(position= (i/2, -1.8, -5), size = (0.5,0.5,0.5), material=sandTexture)
        )

def generateGrass(rtx, grassTexture):
    rtx.scene.append(
            AABB(position= (-2.2, -1.55, -7.2), size = (6,0.1,5), material=grassTexture)
        )

def generateSand(rtx, sandTexture):
    rtx.scene.append(
            AABB(position= (3.5, -1.8, -10), size = (8,0.5,10), material=sandTexture)
        )

def generateDirt(rtx, dirtTexture):
    rtx.scene.append(
            AABB(position= (-2, -2, -10), size = (10,0.5,10), material=dirtTexture)
        )

        
def generateMirror(rtx, mirrorTexture):
    rtx.scene.append(
            AABB(position= (-5, 0, -15), size = (5,5,1), material=mirrorTexture)
        )


def generateSun(rtx, sunTexture):
    rtx.scene.append(
            Sphere(center= (6, 6, -15), radius = 1, material=sunTexture)
        )

def generateDiamond(rtx, diamondTexture):
    rtx.scene.append(
            Triangle(
                V3(-0.5, 0, -1),
                V3(0, 0.5, -1),
                V3(0.5, 0, -1),
               material= diamondTexture
            )
        )
    rtx.scene.append(
            Triangle(
                V3(-0.5, 0, -1),
                V3(0, -0.5, -1),
                V3(0.5, 0, -1),
                material=diamondTexture
            )
        )
   



# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)
grass = Material(diffuse = (0.3, 1.0, 0.3), spec = 64)
dirt = Material(spec = 64, texture = Texture("textures/dirt.bmp"), matType= OPAQUE)
water = Material(spec = 64, diffuse=(0.1,0.3,0.9), matType= REFLECTIVE)
grass = Material(spec = 64, texture= Texture("textures/grass2.bmp"), matType= OPAQUE)
mirror = Material(spec = 64, diffuse=(0.9,0.9,0.9), matType= REFLECTIVE)
sun = Material(spec = 64, diffuse=(1,1,0), texture=Texture('textures/sun.bmp') , matType= OPAQUE)
sand = Material(spec = 64, texture=Texture('textures/sand.bmp') , matType= OPAQUE)
diamond = Material(spec = 64 , matType= TRANSPARENT, ior=1.5, diffuse=(0.9,0.9,0.9))


rtx = Raytracer(width, height)

# Environment map
rtx.envMap = Texture("sky.bmp")

# Luces
rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( PointLight(point = (-1,1,-5) ))
rtx.lights.append( PointLight(point = (-1,1,0) ))

# Figures
rtx.scene.append( AABB(position = (0,-2,-10), size = (20,0.1,20), material = water) ) # 1 figura reflectiva
generateGround(rtx, dirt,sand) # 11 figuras
generateGrass(rtx, grass) # 1 figura
generateSand(rtx, sand) # 1 figura
generateDirt(rtx, dirt) # 1 figura
generateSun(rtx, sun) # 1 figura
generateDiamond(rtx, diamond) # 1 figura refractiva




rtx.glRender()

rtx.glFinish("output.bmp")