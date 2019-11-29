class Enemy:
	def __init__(self,x):
		self.energy = x
	def get_energy(self):
		print(self.energy)
jeson = Enemy(5)
sandy = Enemy(18)	
dudu = Enemy(0)
jeson.get_energy()
sandy.get_energy()
dudu.get_energy()	