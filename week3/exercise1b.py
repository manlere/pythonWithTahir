def main():
	my_max(100,10,50,2,3,4,5,6)
	my_max("musa","hassan")
	my_max("t","sssssssssssssssssssss")
	my_max(40,30,0,9,1)
	my_min(40,30,0,9,1)
	my_min(100,10,50,2,3,4,5,6)
	my_min("musa","hassan")
def my_max(*args):
	i = 0
	while i < len(args):
		args = list(args)
		args.sort()
		print(args[-1])
		break		
def my_min(*args):
	i = 0
	while i < len(args):
		a = list(args)
		a.sort()
		print(a[0])
		break	
main()