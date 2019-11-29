def gender(sex = ''):
	if sex is 'm':
		sex = "male"
	elif sex is 'f':
		sex = "female"
	print(sex)
gender('m')
gender('f')
gender()