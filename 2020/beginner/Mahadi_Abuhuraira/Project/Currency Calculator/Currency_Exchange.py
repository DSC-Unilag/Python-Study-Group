from Moss_Code import choice

class CurrencyExchange:
	'''This class is a basic currecy calculator Where conversions are made
	It uses a csv file (currencies.csv) where all currencies are stored.
	The first line of the file contain the primary currency with which values in the rest are compared.
	The rest of the lines are currencies in the form:
		symbol,value
		symbol = symbol of the currency
		value = unit equivalent of the currency in primary currency
	'''
	currencies = {}
	primary = ''
	
	def __init__(self):
		lines = ''
		with open('currencies.csv', 'r') as f:
			lines = f.read().split('\n')
		self.primary = lines.pop(0)
		for line in lines:
			symbl = line[:line.index(',')]
			rate = float(line[line.index(',') + 1:])
			self.currencies[symbl] = rate
	
	#This fxn exchange between currencies, returns the amount of f_rm in to if successful, '' if one of the currency doesnt exist
	def exchange(self, f_rm, to, amnt):
		if not (f_rm in self.currencies or to in self.currencies):
			print('One of the currecy is not added')
			return ''
		rate = self.currencies[f_rm]/self.currencies[to]
		return rate * amnt
	
	#this fxn change the primary currency, returns true if successful false if the given currency doesnt exist
	def set_primary(self, newP):
		if not newP in self.currencies:
			return False	
		for currency in self.currencies:
			if currency == newP:
				continue
			self.currencies[currency] = self.exchange(currency,newP,1)
		self.primary = newP
		self.currencies[newP] = 1.00
		return True
	
	#This fxn add new currency, returns True if successful, False if currency already exist
	def add_currency(self,c_name,unitVal):
		if c_name in self.currencies:
			return False
		else:
			self.currencies[c_name] = unitVal
		return True
	
	#This fxn returns all the currencies with their unit values in the primary currency in a tabular form
	def get_All(self):
		line = '-'*33 + '\n'
		f = '|{:^4}|{:<10}|{:>15,.3f}|\n'
		result = line + '|{:<4}|{:<10}|{:>15}|\n'.format('S/N','Currency','Value in ' + self.primary) + line
		n = 0
		for c,v in self.currencies.items():
			result += f.format(n+1,c,v) + line
			n += 1
		return result
	
	#this fxns saves all changes made during running the programme in the underlying csv file
	def save(self):
		result = self.primary + '\n'
		for c,v in self.currencies.items():
			result += c + ',' + str(v) + '\n'
		with open('currencies.csv', 'w') as f:
			f.write(result.strip())
	
	#this fxn update the value of a currency, returns True if successful, False if currency doesnt exist
	def change_rate(self,cur,newVal):
		if not cur in self.currencies:
			return False
		self.currencies[cur] = newVal
		return True

#end of class currency exchange

def main():
	menus = ('Display Current Rates','Exchange Currencies','Add Currency','Update Currency value','Change Primary Currency','Exit')
	CE = CurrencyExchange()
	x = 0
	while x != len(menus):
		x = choice(menus)
		if x == 1:
			print(CE.get_All())
		elif x == 2:
			frm = input('\nEnter the currency to exchange from: ').upper()
			to = input('Enter the currency to exchange to: ').upper()
			amnt = float(input('Enter amount to exchange: '))
			ex = CE.exchange(frm,to,amnt)
			if ex == '':
				continue
			else:
				print('{} {} = {} {:,.2f}'.format(frm,amnt,to,ex))
		elif x == 3 or x == 4:
			cur = input('\nEnter Currency name: ').upper()
			val = float(input('Enter unit Value of {} in {}: '.format(cur,CE.primary)))
			temp = ((CE.add_currency,'existed already !'),(CE.change_rate,'doesnt exist !'))[x - 3]
			if temp[0](cur,val):
				print('Currencies updated successfully!')
			else:
				print('Currency ' + temp[1])
		elif x == 5:
			cur = input('\nEnter Currency name to make primary: ').upper()
			if CE.set_primary(cur):
				print('primary currency set successfully!')
			else:
				print('currency doesnt exist')
		elif x == 6:
			CE.save()
			print('Thank you')
		print()

#end of main fxn

main()