#while True: print(sum(int(x)for x in input()))
from math import sqrt
def quadratic_equation():
	x = int(input("enter the coeficient of x square:\n"))
	y = int(input("enter the linear term:\n"))
	z  = int(input("enter the constant term\n"))
	result = (-y+math.sqrt(y*y-4*x*z)/2*x)
	result2 = (-y-math.sqrt(y*y-4*x*z)/2*x)
	print(f"x = {result} or x = {result2}")
quadratic_equation()	