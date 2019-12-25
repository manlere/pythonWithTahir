def my_sum(list_of_numbers):
	result = 0
	for number in list_of_numbers:
		result+= number
	return result
def my_average(list_of_numbers):
	total = my_sum(list_of_numbers)
	count = len(list_of_numbers)
	return total/count

scores = [10,20,30,40,50,60,70,80,90,100]
print(my_sum(scores))
print(my_average(scores))			