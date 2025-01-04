import random
import math
import matplotlib.pyplot as plt

w = 150                                  ## Cell thickness as 150 um
n = 3.5                                  ## Refractive index of Silicon


def Trig(I, phi, theta):
    
    opposite = math.tan(theta)*w
    dx = math.cos(math.radians(phi))*opposite
    dy = math.sin(math.radians(phi))*opposite
    hypotenuse = w/math.cos(theta)
    pathlength = hypotenuse

    return dx,dy,pathlength


def Tracing():
   
    x,y,z = 0,0,w
    I = random.random()
    theta = math.asin(math.sqrt(I))
    phi = random.randint(0,360)
    count = 1
    total_pathlength = 0
    print (x,y,z,total_pathlength)

    while(math.cos(theta) < math.sqrt(1-(1/math.pow(n, 2))) or count%2 == 1):   #conditions: escape cone and hitting the top surface
        dx,dy,pathlength = Trig(I, phi, theta)
        x += dx
        y += dy
        if count%2 == 1:
            z = 0
        else:
            z = w
        total_pathlength += pathlength
        print (x,y,z,total_pathlength)

        I = random.random()
        theta = math.asin(math.sqrt(I))
        phi = random.randint(0,360)
        count += 1
    
    dx,dy,pathlength = Trig(I, phi, theta)
    x += dx
    y += dy
    z = w
    total_pathlength += pathlength
    
    print (x,y,z,total_pathlength)
    
    xy_travel = math.sqrt(x**2 + y**2)
    print("theta: "+str(round(math.degrees(theta),1))+" degrees")
    print("xy_travel: "+str(round(xy_travel,1))+" um"+"/"+"pathlength: "+str(round(total_pathlength,1))+" um")
    print("reflection counts:"+str(count))
    return xy_travel, count, total_pathlength


## Excel Part

iterations = 10000000

for j in range(iterations):
    xy_travel, count, total_pathlength = Tracing()
    values  += f"{round(xy_travel,0)},{count},{round(total_pathlength,0)}\n"

f = open("C:\\Users\\14505\\Downloads\\outputJY_4.csv", "a")
f.write(values)
f.close()
