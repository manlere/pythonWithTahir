def allowed_dating_age(my_age):
	girls_age = my_age/2+7
	return girls_age

bucky_limit = allowed_dating_age(27)
creep_joe_limit = allowed_dating_age(49)
print("Bucky can date girls",bucky_limit,"or older")
print("creepy joe can date girls", creep_joe_limit,"or older")	