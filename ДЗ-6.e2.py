class  trapezium:
	def __init__(self, X1, Y1, X2, Y2, X3, Y3, X4, Y4):
		self.X1 = X1
		self.Y1 = Y1
		self.X2 = X2
		self.Y2 = Y2
		self.X3 = X3
		self.Y3 = Y3
		self.X4 = X4
		self.Y4 = Y4

	def chek(self):
		import math
		a = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
		b = math.sqrt((X3-X2)**2 + (Y3-Y2)**2)
		c = math.sqrt((X4-X3)**2 + (Y4-Y3)**2)
		d = math.sqrt((X1-X4)**2 + (Y1-Y4)**2)
		if a == c:
			print('Трапеция - равнобедренная')
		else:
			print('Трапеция - не равнобедренная')

	def perimetr(self):
		import math
		a = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
		b = math.sqrt((X3-X2)**2 + (Y3-Y2)**2)
		c = math.sqrt((X4-X3)**2 + (Y4-Y3)**2)
		d = math.sqrt((X1-X4)**2 + (Y1-Y4)**2)
		p = a + b + c + d
		print('Периметр равен - ', p)

	def square(self):
		import math
		a = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
		b = math.sqrt((X3-X2)**2 + (Y3-Y2)**2)
		c = math.sqrt((X4-X3)**2 + (Y4-Y3)**2)
		d = math.sqrt((X1-X4)**2 + (Y1-Y4)**2)
		h = math.sqrt(a**2 - ((d - b) / 2)**2)
		s = ((b + d) * h)/ 2
		print('Площадь равна - ', s)

	def side(self):
		import math
		import math
		a = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
		b = math.sqrt((X3-X2)**2 + (Y3-Y2)**2)
		c = math.sqrt((X4-X3)**2 + (Y4-Y3)**2)
		d = math.sqrt((X1-X4)**2 + (Y1-Y4)**2)
		print('Длины сторон - ', a, ',', b, ',', c, ',', d)

trap = trapezium(2, 2, 4, 4, 6, 4, 8, 2)

trap.chek()
trap.perimetr()
trap.square()
trap.side()


