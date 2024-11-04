#functions
from datetime import date


#area of a triangle

def calc_area_triangle(b, h):
    area=0.5 * b * h
    print(area)

def calc_area_circle(r):
    area=22/7*r*r
    area=round(area,2)
    print("The area of the circle is:",area,"cm^2")

def todays_date():
    today=date.today()
    print(today)

def add(*args):
    total=0
    for i in args:
        total=total+i
        total=round(total,2)
    print("Total is ",total)

def sayHi(name,age):
    print("Hi ",name,"I am",age,"years old.")

#use a func call
calc_area_triangle(8,13)
calc_area_triangle(4,1)


triangles=[[8,9],[6,13],[5,4],[34,2]]

for t in triangles:
    calc_area_triangle(t[0],t[1])

calc_area_circle(4)
todays_date()

add(1,3,4)
add(3,45,56,67)
add(45.278,34.567)

sayHi("Loyce",21)

#data  name,gender,amount
#account
#deposit/withdrawal/check balance
#oop

#matatu --->number,driver,conductor,route

