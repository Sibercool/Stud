class  triangle:
	def __init__(self, X1, Y1, X2, Y2, X3, Y3):
		self.X1 = X1
		self.Y1 = Y1
		self.X2 = X2
		self.Y2 = Y2
		self.X3 = X3
		self.Y3 = Y3

	def perimetr(self):
		import math
		a = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
		b = math.sqrt((X3-X2)**2 + (Y3-Y2)**2)
		c = math.sqrt((X1-X3)**2 + (Y1-Y3)**2)
		p = a + b + c
		print('Периметр треугольника равен - ', p)

	def square(self):
		import math
		a = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
		b = math.sqrt((X3-X2)**2 + (Y3-Y2)**2)
		c = math.sqrt((X1-X3)**2 + (Y1-Y3)**2)
		p = a + b + c
		s = math.sqrt(((p / 2) - a) * ((p / 2) - b) * ((p / 2) - c))
		print('Площадь треугольника равна - ', s)

	def height(self):
		import math
		a = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
		b = math.sqrt((X3-X2)**2 + (Y3-Y2)**2)
		c = math.sqrt((X1-X3)**2 + (Y1-Y3)**2)
		h1 = math.sqrt((a**2 + b**2 - c**2) / 2)
		h2 = math.sqrt((b**2 + c**2 - a**2) / 2)
		h3 = math.sqrt((c**2 + a**2 - b**2) / 2)
		print('Высоты треугольника - ', h1, ",", h2,",", h3)

tri = triangle(1, 2, 4, 8, 3, 6)

tri.perimetr()
tri.square()
tri.height()


