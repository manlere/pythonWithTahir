def main():
	while True:
		user_input = input("welcome to manlere naira currency converter, what will you like to convert:\n [1]  - brirtsh_pound\n [2]  - euro\n [3]  - american_dollar\n [4]  - indian_rupee\n [5]  - saudi_riyal\n [6]  - canadian_dollar\n [7]  - japanese_yen\n [8]  - swiss_franc\n [9]  - korean_won\n [10] - brazilian_real\n [11] - malaysian_ringgit\n [12] - qatari_rial\n [13] - pakistan_rupee\n [14] - egyptian_pound\n [15] - turkish_lira\n [0]  - Exit\n")
		if user_input == "1":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			brirtsh_pound(naira)
		elif user_input == "2":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			euro(naira)
		elif user_input == "3":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			american_dollar(naira)
		elif user_input == "4":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			indian_rupee(naira)
		elif user_input == "5":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			saudi_riyal(naira)
		elif user_input == "6":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			canadian_dollar(naira)
		elif user_input == "7":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			japanese_yen(naira)
		elif user_input == "8":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			swiss_franc(naira)
		elif user_input == "9":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			korean_won(naira)
		elif user_input == "10":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			brazilian_real(naira)
		elif user_input == "11":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			malaysian_ringgit(naira)
		elif user_input == "12":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			qatari_rial(naira)
		elif user_input == "13":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			pakistan_rupee(naira)
		elif user_input == "14":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			egyptian_pound(naira)
		elif user_input == "15":
			naira = input("\nEnter Amount In Naira\n")
			naira = int(naira)
			turkish_lira(naira)	
		elif user_input == "0":
			exit()
		else:
			print("***** Input not recognise *****") 

def brirtsh_pound(naira):
	brirtsh_pound = 0
	for x in range(naira):
		brirtsh_pound+=0.0021
	print(f"***** {naira} NGN is equal to {brirtsh_pound} Brirtsh Pound *****" )

def euro(naira):
	euro = 0
	for x in range(naira):
		euro+=0.0025
	print(f"***** {naira} NGN is equal to {euro} Euro *****" )

def american_dollar(naira):
	american_dollar = 0
	for x in range(naira):
		american_dollar+=0.0028
	print(f"***** {naira} NGN is equal to {american_dollar} American Dollar *****" )

def indian_rupee(naira):
	indian_rupee = 0
	for x in range(naira):
		indian_rupee+=0.196
	print(f"***** {naira} NGN is equal to {indian_rupee} Indian Rupee *****" )

def saudi_riyal(naira):
	saudi_riyal = 0
	for x in range(naira):
		saudi_riyal+=0.0103
	print(f"***** {naira} NGN is equal to {saudi_riyal} Saudi Riyal *****" )

def canadian_dollar(naira):
	canadian_dollar = 0
	for x in range(naira):
		canadian_dollar+=0.0036
	print(f"***** {naira} NGN is equal to {canadian_dollar} Canadian Dollar *****" )

def japanese_yen(naira):
	japanese_yen = 0
	for x in range(naira):
		japanese_yen+=0.302
	print(f"***** {naira} NGN is equal to {japanese_yen} Japanese Yen *****" )

def swiss_franc(naira):
	swiss_franc = 0
	for x in range(naira):
		swiss_franc+=0.0027
	print(f"***** {naira} NGN is equal to {swiss_franc} Swiss Franc *****" )

def korean_won(naira):
	korean_won = 0
	for x in range(naira):
		korean_won+=3.2
	print(f"***** {naira} NGN is equal to {korean_won} Korean Won *****" )

def brazilian_real(naira):
	brazilian_real = 0
	for x in range(naira):
		brazilian_real+=0.0113
	print(f"***** {naira} NGN is equal to {brazilian_real} Brazilian Real *****" )

def malaysian_ringgit(naira):
	malaysian_ringgit = 0
	for x in range(naira):
		malaysian_ringgit+=0.0114
	print(f"***** {naira} NGN is equal to {malaysian_ringgit} Malaysian Ringgit *****" )

def qatari_rial(naira):
	qatari_rial = 0
	for x in range(naira):
		qatari_rial+=0.01
	print(f"***** {naira} NGN is equal to {qatari_rial} Qatari Rial *****" )

def pakistan_rupee(naira):
	pakistan_rupee = 0
	for x in range(naira):
		pakistan_rupee+=0.427
	print(f"***** {naira} NGN is equal to {pakistan_rupee} Pakistan Rupee *****" )

def egyptian_pound(naira):
	egyptian_pound = 0
	for x in range(naira):
		egyptian_pound+=0.0443
	print(f"***** {naira} NGN is equal to {egyptian_pound} Egyptian Pound *****" )

def turkish_lira(naira):
	turkish_lira = 0
	for x in range(naira):
		turkish_lira+=0.0164
	print(f"***** {naira} NGN is equal to {turkish_lira} Turkish Lira *****" )
	
main()															