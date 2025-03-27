class mathmanager:

	def add(self, a, b):
			return a+b

	def subtract(self, a, b):
			return a-b

	def multiply(self, a, b):
			return a*b

	def calculate_monthly_interest(self, principal, years):
			rate = 0.038 if years == 1 else 0.036
			monthly_interest = (principal * rate) / 12
			return round(monthly_interest, 2)
	
	def calculate_tax(self, income):
			tax = 0
			if income <= 12570:
				return 0
			elif income <= 50270:
				tax += (income - 12570) * 0.20
			elif income <= 125140:
				tax += (50270 - 12570) * 0.20
				tax += (income - 50270) * 0.40
			else:
				tax += (50270 - 12570) * 0.20
				tax += (125140 - 50270) * 0.40
				tax += (income - 125140) * 0.45
			return round(tax, 2)