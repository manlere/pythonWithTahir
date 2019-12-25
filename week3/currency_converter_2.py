def main():
	while True:
		naira = int(input("welcome to manlere naira currency converter,\n Enter Amount In Naira\n"))
		brirtsh_pound(naira)
		euro(naira)
		american_dollar(naira)
		indian_rupee(naira)
		saudi_riyal(naira)
		canadian_dollar(naira)
		japanese_yen(naira)
		swiss_franc(naira)
		korean_won(naira)
		brazilian_real(naira)
		malaysian_ringgit(naira)
		qatari_rial(naira)
		pakistan_rupee(naira)
		egyptian_pound(naira)
		turkish_lira(naira)
		action = input("\n [1] - Continue\n [0] - Exit\n")
		quit(action)			
def brirtsh_pound(naira):
	brirtsh_pound = 0
	for x in range(naira):
		brirtsh_pound+=0.0021
		round(brirtsh_pound)

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
def quit(action):
	if action == "1":
		pass
	elif action == "0":
		exit()
	else:
		print("***** Input not recognise *****") 
main()		