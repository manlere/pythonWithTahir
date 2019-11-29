class Mario():
	def move(self):
		print('i am moving')
class Shroom():
	def eat_shroom(self):
		print('Now i am big')
class BigMario(Mario,Shroom):
	pass
bm = BigMario()				
bm.move()
bm.eat_shroom()