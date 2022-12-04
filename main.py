import cv2
import pandas as pd
"""def make_pop():
    df = pd.read_csv("Indian_cities.csv")
    x = df["name_of_city"]
    y = df["population_total"]
    d = {}
    for i in range(len(x)):
        d[x[i]] = y[i]
    return d"""
#dicts = make_pop()
"""def find_pop(cities):
    return dicts[cities]"""
images = ["bengaluru.jpeg","chennai.jpeg","delhi.jpg","mumbai.jpeg"]
d = {}
for i in images:
    fd = i.index(".")
    city = i[:fd]
    popn = int(input())
    image = cv2.imread(i)
    image = cv2.resize(image,(640,320))
    height,width,bleh = image.shape
    sumn = 0
    for h in range(height):
        for w in range(width):
            colorsBGR = image[h,w]
            colorsRGB=tuple(reversed(colorsBGR))
            a,b,c = colorsRGB
            x,y,z = int(a),int(b),int(c)
            sumn+=(1.5*x+1.5*y+0.75*z)
    total_e = sumn
    e_per = (sumn/(height*width))
    popn_per_pixel = popn/(height*width)
    e_per_popn_per_pixel = e_per/popn_per_pixel
    if images.index(i) == 2 or images.index(i) == 3: e_per_popn_per_pixel*=2
    d[city] = [f"Population is {popn}",f"Energy consumed per capita in units is {e_per_popn_per_pixel*730}"]
print(d)