#cylinder
from lesson11 import calc_area_circle


class Cylinder:
    def __init__(self,radius,height,color):
        self.r=radius
        self.h=height
        self.c=color

    def cal_area(self,is_closed=True):
        if is_closed==True:
            area=2 * 22/7 * self.r ** 2 + 22/7 * self.h * self.r
            print(f"Area of a closed cylinder is {area} cm^2")

        else:
            area=22/7* self.r ** 2 + 2 * 22/7 * self.h * self.r
            print(f"Area of an open cylinder is {area} cm^2")

    def cal_volume(self):
        v=22/7 * self.r ** 2 * self.h
        print(f"Volume of a cylinder is: {v} cm^3")

c1=Cylinder(14,10,"Red")
c2=Cylinder(21,2,"Green")
c1.cal_area(is_closed=False)
c1.cal_area(is_closed=True)
c2.cal_volume()