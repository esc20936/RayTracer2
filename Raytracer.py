from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 512
height = 512

# Materiales


r1 = Material(diffuse = (0.8, 0.3, 0.3), spec = 64, matType= REFLECTIVE)
r2 = Material(diffuse = (0.9, 0.9, 0.2), spec = 64, matType = REFLECTIVE)

t1 = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = TRANSPARENT, ior = 1.5)
t2 = Material(diffuse = (0.9, 0.2, 0.9), spec = 64, matType = TRANSPARENT, ior = 2.3)

o1 = Material(diffuse = (0.2, 0.2, 0.9), spec = 32)
o2 = Material(diffuse = (0.9, 0.9, 0.2), spec = 32)

rtx = Raytracer(width, height)

rtx.envMap = Texture("fondo3.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))
#rtx.lights.append( PointLight(point = (0,0,0)))

rtx.scene.append( Sphere(V3(0,0,-10), 1, t1)  )
rtx.scene.append( Sphere(V3(3,0,-10), 1, t2)  )

rtx.scene.append( Sphere(V3(0,3,-10), 1, r1)  )
rtx.scene.append( Sphere(V3(3,3,-10), 1, r2)  )

rtx.scene.append( Sphere(V3(0,-3,-10),1, o1)  )
rtx.scene.append( Sphere(V3(3,-3,-10), 1, o2)  )


rtx.glRender()

rtx.glFinish("output.bmp")