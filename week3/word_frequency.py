def main():
	user_input = input("\nEnter Text String\n")
	word_frequency(user_input)
def word_frequency(user_input):
	i = 0
	a = user_input.split()
	a.sort(key=len)
	while i < len(a):	
		print(f"{a[i]} = {user_input.count(a[i])}")
		i+=1	
main()