
Bank_database = [
    {"account_name":"Dahir Muhammad", "account_number":"001","account_type":"current", "account_balance":30000, "Pin":1010},
    {"account_name":"Fauziya Musa", "account_number":"002","account_type":"seving", "account_balance":70000, "Pin":1020},
    {"account_name":"Aisha Ahmad", "account_number":"003","account_type":"current", "account_balance":35000, "Pin":1030},
    {"account_name":"Maimuna Ahmad", "account_number":"004","account_type":"seving", "account_balance":20000, "Pin":1040},
    {"account_name":"Muhammad Abdulhameed Sani", "account_number":"005","account_type":"current", "account_balance":30000, "Pin":1130}
]
def main():
	while True:
		action = input("welcome, what will you like to do:\n [1] - Deposit Money\n [2] - withdraw\n [3] - Transfer Money\n [4] - Check Balance\n [5] - Airtime\n [6] - Exit Bank\n")
		if action == "1":
			deposit_funds()
		elif action == "2":
			withraw_funds()
		elif action == "3":
			transfer_funds()
		elif action == "4":
			check_balance()
		elif action == "5":
			airtime_funds()
		elif action == "6":
			exit()		
		else:
			print("\n {!!!!!Check your input!!!}\n")					
def deposit_funds():
	target_account_name = input("\nEnter account name: \n")
	target_account_number = input("\nEnter account number\n")
	target_pin = input("\nEnter your pin:\n")
	target_pin = int(target_pin)
	target_amount = (input("\nEnter amount to deposit:\n"))
	amount = int(target_amount)
	try_to_deposit = credit_account(target_account_name,target_account_number,amount)
	check_target_account_name = check_account_name(target_account_name)
	target_check_account_number= check_account_number(target_account_number)
	target_check_pin = check_pin(target_pin)
	if target_check_account_number == True:
		pass
		if check_target_account_name == True:
			pass
			if target_check_pin == True:
				pass	
				if try_to_deposit == True:
					print("\n {!!!!!Your Bank Deposit was Successful!!!!!}\n")		
def withraw_funds():
	target_account_name = input("\nEnter account name: \n")
	target_account_number = input("\nEnter account number\n")
	target_account_type = input("\nEnter account type:\n[1] - saving\n[2] - current\n")
	if target_account_type == "1":
		target_account_type = "saving"
	elif target_account_type == "2":
		target_account_type = "current"		
	target_pin = input("\nEnter your pin:\n")
	target_pin = int(target_pin)
	target_amount = (input("\nEnter amount to withraw:\n"))
	amount = int(target_amount)
	try_to_withraw = debit_account(target_account_name,target_account_number,amount)
	check_target_account_number= check_account_number(target_account_number)
	check_target_account_name = check_account_name(target_account_name)
	target_check_pin = check_pin(target_pin)
	check_target_account_type = check_account_type(target_account_type)
	if check_target_account_number == True:
		pass
		if check_target_account_name == True:
			pass	
			if target_check_pin == True:
				pass
				if check_target_account_type == True:
					pass 	
					if try_to_withraw == True:
						print("\n {!!!!!Your Bank Withraw was Successful!!!!!}\n")		
def transfer_funds():
	user_account_name = input("\n Enter Your Account Name\n")
	user_account_number = input("\n Enter Your Account Number\n")
	target_account_name = input("\n Enter Account Name To Transfer\n")
	target_account_number = input("\n Enter Account number To Transfer\n")
	target_amount = input("\n Enter Amount To Transfer\n")
	amount = int(target_amount)
	target_pin = input("\nEnter your pin:\n")
	target_pin = int(target_pin)
	target_check_transfer_user_account_name = check_transfer_user_account_name(user_account_name)
	target_check_transfer_user_account_number = check_transfer_user_account_number(user_account_number)
	target_check_transfer_recepient_account_name = check_transfer_recepient_account_name(target_account_name)
	target_check_transfer_recepient_account_number = check_transfer_recepient_account_number(target_account_number)
	target_check_transfer_user_account_name_and_pin = check_transfer_user_account_name_and_pin(user_account_name,user_account_number,target_pin)
	target_check_pin = check_pin(target_pin)
	if target_check_transfer_user_account_name == True:
		pass
		if target_check_transfer_user_account_number == True:
			pass
			if target_check_transfer_recepient_account_name == True:
				pass
				if target_check_transfer_recepient_account_number == True:
					pass
					if 	target_check_transfer_user_account_name_and_pin == True:
						pass
						if target_check_pin == True:
							pass					
							if [user_account_name,user_account_number] == [target_account_name,target_account_number]:
								print("\n {!!!!!You can't Transfer Money To Thesame Account!!!!!}\n")
								return			
						try_to_debit =  debit_account(user_account_name,user_account_number,amount)
						if try_to_debit == True:
							try_to_transfer = credit_account(target_account_name,target_account_number,amount)
							if try_to_transfer == True:
								print("\n {!!!!!Your Transfer was Successful!!!!!}\n")																							
def airtime_funds():
	action = input("\n[1] - Self\n[2] - Other\n")
	if 	action == "1":
		target_account_name = input("\nEnter account name: \n")
		target_account_number = input("\nEnter account number\n")
		target_amount = input("\n Enter Amount to Recharge\n")
		amount = int(target_amount)
		target_pin = input("\nEnter your pin:\n")
		target_pin = int(target_pin)
		check_target_account_number= check_account_number(target_account_number)
		check_target_account_name = check_account_name(target_account_name)
		try_to_debit = debit_airtime(target_amount,target_account_number,target_account_name,amount,target_pin)
		target_check_pin = check_pin(target_pin)
		if check_target_account_number == True:
			pass
			if check_target_account_name == True:
				pass
				if target_check_pin == True:
					pass
					if try_to_debit == True:
						print("\n {!!!!! Your Recharge was Successful !!!!!}\n")
	elif action == "2":
		target_phone_number = input("\n Enter phone Number\n")
		target_account_name = input("\nEnter account name: \n")
		target_account_number = input("\nEnter account number\n")
		target_amount = input("\n Enter Amount to Recharge\n")
		amount = int(target_amount)
		target_pin = input("\nEnter your pin:\n")
		target_pin = int(target_pin)
		check_target_account_name = check_account_name(target_account_name)
		check_target_account_number= check_account_number(target_account_number)
		try_to_debit = debit_airtime(target_amount,target_account_number,target_account_name,amount,target_pin)
		target_check_pin = check_pin(target_pin)
		if check_target_account_name == True:
			pass
			if check_target_account_number == True:
				pass
				if target_check_pin == True:
					pass
					if try_to_debit == True:
						print("\n {!!!!! Your Recharge was Successful !!!!!}\n")
def check_balance():
	target_account_number = input("\nEnter account number\n")
	target_pin = input("\nEnter your pin:\n")
	target_pin = int(target_pin)
	target_check_account_number= check_account_number(target_account_number)
	target_check_pin = check_pin(target_pin)
	for account in Bank_database:
		if [account["account_number"],account["Pin"]]==[target_account_number,target_pin]:
			if target_check_account_number == True:
				pass
				if target_check_pin == True:
					pass
					current_account_balance = account["account_balance"]		
					print("\n{!!!!!Your Account Balance is NGN" + str(current_account_balance)+"!!!!!}\n")
					return
	return False
	print("\n {!!!!! Invalid pin !!!!!}\n")						
def debit_airtime(target_amount,target_account_number,target_account_name,amount,target_pin):
	for account in Bank_database:
		if [account["account_number"],account["account_name"],account["Pin"]] == [target_account_number,target_account_name,target_pin]:
			account["account_balance"] -= amount
			return True
	return
def credit_account(target_account_name,target_account_number,amount):
	for account in Bank_database:
		if [account["account_name"],account["account_number"]] == [target_account_name, target_account_number]:
			account["account_balance"]+= amount
			return True
	return 		
def debit_account(target_account_name,target_account_number,amount):
	for account in Bank_database:
		if [account["account_name"],account["account_number"]] == [target_account_name, target_account_number]:
			account["account_balance"]-= amount
			return True
	return
def check_pin(target_pin):	
	for pin in Bank_database:
		if pin["Pin"]==target_pin:
			return True		
	print("\n {!!!!! Invalid pin !!!!!}\n")			
def check_account_type(target_account_type):
	for account_type in Bank_database:
		if account_type["account_type"]== target_account_type:
			return True
	print("\n {!!!!! Invalid Account Type !!!!!}\n")
def check_account_name(target_account_name):
	for account_name in Bank_database:
		if account_name["account_name"] == target_account_name:
			return True
	print("\n {!!!!! Account Name not Found !!!!!}\n")
def check_account_number(target_account_number):
	for account_number in Bank_database:
		if account_number["account_number"] == target_account_number:
			return True
	print("\n {!!!!! Account Number not Found !!!!!}\n")
def check_transfer_user_account_name(user_account_name):
	for account_name in Bank_database:
		if account_name["account_name"] ==  user_account_name:
			return True
	print("\n {!!!!! Your Account Name not Found !!!!!}\n")
def check_transfer_user_account_number(user_account_number):
	for account_number in Bank_database:
		if account_number["account_number"] ==  user_account_number:
			return True
	print("\n {!!!!! Your Account Number not Found !!!!!}\n")
def check_transfer_recepient_account_name(target_account_name):
	for account_name in Bank_database:
		if account_name["account_name"] ==  target_account_name:
			return True
	print("\n {!!!!! Recepient Account Name not Found !!!!!}\n")
def check_transfer_recepient_account_number(target_account_number):
	for account_number in Bank_database:
		if account_number["account_number"] ==  target_account_number:
			return True
	print("\n {!!!!! Recepient Account Number not Found !!!!!}\n")
def check_transfer_user_account_name_and_pin(user_account_name,user_account_number,target_pin):	
	for account in Bank_database:
		if [account["account_name"],account["account_number"],account["Pin"]] == [user_account_name,user_account_number,target_pin]:
			return True
	print("\n {!!!!! Your Transfer Failed !!!!!}\n")			
main()								