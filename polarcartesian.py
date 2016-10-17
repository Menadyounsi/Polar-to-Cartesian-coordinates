#Program to transform between Polar and Cartesian coordinates
import math
print "Script to calculate Cartesian coordinates from Polar"
print "\n\nplease enter the corresponding values:"
r = float(raw_input("r > "))
angle = float(raw_input("Theta > "))

x = r * math.cos(angle)
y = r * math.sin(angle)

print x, y
