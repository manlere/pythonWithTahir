# Exercise 2-5: Loops and Numbers (for and while Loops)
# Using while Loop

number = 0
while number <=10:
	print(number)
	number+=1
# Using for Loop

for i in range(0,11):
	print(i)
# Exercise 2-7: Loops and String
# Using while Loop

text = input("input string text: ")
counter = 0
while counter < len(text):
	print(text[counter])
	counter+=1
# Using for Loop

text = input("input string text: ")
for c in text:
	print(c)

# Exercise 2-8: Loops and operators
# Using fixed list (wile loop)

counter = 0
numbers = [0,1,2,3,4]
while counter <= len(numbers):
	print(sum(int(x) for x in numbers))
	break
# Using fixed list(for loop)

numbers = [0,1,2,3,4]
print(sum(int(i) for i in numbers))

# Using user input (while loop)
while True:
	number = input("input Number: ") 
	print(sum(int(x)for x in number))
	break
# Using user input(for loop)
number = input("input Number: ")
print(sum(int(x)for x in number))

# Exercise 2-9: More loops and operatin (Average)
number = [1,2,3,4,5]
average = (sum(int(x) for x in number))/len(number)
print(average)

#Exercise 2-8: p(320)

f = int(input("start value: "))
t = int(input("end value: "))
i = int(input("increment value: "))
for x in range(f,t+1,i):
	print(x)