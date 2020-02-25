string = input("\n Enter text: \n")
a = string.split()
a.sort()
count =0
while count <len(a):
	print(str(a[count])+"=" +str(a.count(a[count])))
	count+=a.count(a[count])	