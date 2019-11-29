while True:
	try: 
		number = int(input("what's your fav number hoss?\n"))
		print(18/number)
		break
	except ValueError:
		print("Make sure and enter number")
	except ZeroDivisionError:
		print("Don't pick zero")
	except: 
		break
	finally:
		print("loop complete")				