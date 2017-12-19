
class Branding:

	options = {'Sí':1, 'No':0}

	def __init__(self, brand, clean, new):
		self.brand = options[brand]
		self.clean = options[clean]
		self.new = options[new]

	def looks_good(self):
		return self.brand

	def is_clean(self):
		return self.clean

	def is_new(self):
		return self.new