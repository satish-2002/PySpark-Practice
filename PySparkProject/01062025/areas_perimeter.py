import math
#Areas & Perimeters
base = int(input("Enter base value:"))
height = int(input("Enter height value:"))

#Area of triangle 0.5*b*h
print("Area of triangle is:", 0.5*base*height)

#Perimeter of triangle s1+s2+s3
s3 = math.sqrt((base*base)+(height*height))
print("Perimeter of triangle is:", base+height+s3)

#Area of square s^2
print("Area of Square:", base*base)

#Perimeter of Square 4(a)
print("Perimeter of Square:", 4*base)

#Area of Rectangle b*h
print("Area of Rectangle:", base*height)

#Perimeter of Rectangle 2*(l+b)
print("Perimeter of Square:", 2*(base+height))

#Area of circle pi*r^2
print("Area of circle (radius = ",base,"):", 3.14*base**2)

#Perimeter of circle 2*pi*r
print("Perimeter of circle (radius = ",base,"):", 2*3.14*base)
