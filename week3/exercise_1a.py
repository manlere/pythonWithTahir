def main():
	max2(5,10)
	min2(5,10)
	max2("a","b")
	min2("a","b")

def max2(a,b):
	if a > b:
		max_value = a
		print(f"{max_value}")
	elif b > a:
		max_value = b
		print(f"{max_value}")
def min2(a,b):
	if a<b:
		min_value = a
		print(f"{min_value}")
	elif b<a:
		min_value = b
		print(f"{min_value}")
main()		 	