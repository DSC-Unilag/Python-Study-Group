class MossCode:
	dash = '_'
	dot = '.'
	def __init__(self):
		self.dictionary = {}
		self.dictionary['Digits'] = self.get_digits()
		self.dictionary['Alphabets'] = self.get_alphabets()
	
	def get_digits(self):
		dictionary = {}
		for i in range(1,6):
			dots = ''
			dashes = ''
			for j in range(i):
				dots += self.dot + ' '
			for j in range(5-i):
				dashes += self.dash + ' '
			dictionary[(dots.strip() + ' ' + dashes.strip()).strip()] = str(i)
			if i < 5: dictionary[dashes.strip() + ' ' + dots.strip()] = str(10 - i)
		dictionary[((self.dash + ' ')*5).strip()] = '0'
		return dictionary
	
	def get_alphabets(self):
		source = ''
		dictionary = {}
		trans = lambda x: self.dot if x == 'dt' else self.dash
		with open('alpha_morse_codes.txt', 'r') as f:
			source = f.read().split('\n')
		for line in source:
			temp = line.split(',')
			alph = temp[0]
			code = ' '.join(map(trans,temp[1:]))
			dictionary[code] = alph
		return dictionary
	
	def is_valid_code(self,code):
		for char in code:
			if not char in (self.dot,self.dash,' '):
				return False
		return True
	
	def get_charCode(self,char):
		char = char.upper()
		temp = 'Digits' if char.isdigit() else 'Alphabets'
		ans = ''
		for code,alph in self.dictionary[temp].items():
			if alph == char:
				ans = code
				break
		if not ans:
			return char
		return ans
		
	def translate_code(self,code):
		
		'''This fxn takes in text in morse code and returns
		its translated form.
		The standard rules followed are:
			The space bw parts of same letter is one
			The space bw letters is three
			The space bw words is seven
		'''
		#check if code contains only dots, dashes and spaces
		if not self.is_valid_code(code):
			print('Invalid characters in code!!!')
			return ''
			
		#split code to a list of code_words
		text = code.split(' '*7)

		#split words to list of char_codes
		for i in range(len(text)):
			text[i] = text[i].split(' '*3)
		
		result = ''
		for code_word in text:
			word = ''
			for char_code in code_word:
				try:
					word += self.dictionary['Alphabets'][char_code]
				except KeyError:
					#not yet decided
					return
			result += word + ' '
		
		return result
	
	def decode_file(self,filename, enc = 0):
		'''This function takes two parameters:
			filename : which is the fullname of the text file to be processed
			enc : with default value as 0. if its 0 then the content of file will be read and encoded into a new file, while if 1 the file will be decoded
		'''
		lines = []
		param = ((lambda x: self.translate_code(x),'_decoded.txt','plain text'),(lambda x: self.encode_text(x),'_encoded.txt','cypher text'))[enc]
		try:
			with open(filename, 'r') as f:
				lines = f.read().split('\n')
		except:
			print('file not found..')
			return
		result = ''
		for line in lines:
			result += param[0](line) + '\n'
		new_file = filename[:filename.rindex('.')] + param[1]
		with open(new_file, 'w') as f:
			f.write(result.strip('\n'))
		print('Task completed successfully!')
		print(param[2],'saved in',new_file)
		
	def encode_text(self,text):
		'This fxn returns the morse code for the parameter text'
		
		#split text to words
		words = text.split()
		
		#encode
		code = ''
		for word in words:
			code_word = ''
			for char in word:
				code_word += self.get_charCode(char) + ' '*3
			code += code_word.strip() + ' '*7
		return code.strip()
	
	def encode_file(self,filename):
		self.decode_file(filename,1)
	
#end of class MossCode()

def choice(options):
	for i in range(len(options)):
		print(i+1,options[i],sep='. ')
	x = 0
	while not x in range(1,len(options)+1):
		try: x = int(input('your choice? :'))
		except ValueError:
			print('Invalid choice')
			continue
	return x

def my_print(data):
	f = '|{:^12}|{:^20}|'
	print('-'*35)
	print(f.format('Character','Code'))
	print('-'*35)
	for cd,ch in data.items():
		print(f.format(ch,cd))
		print('-'*35)

def main():
	menus = ('Encode a text','Translate a code','Encode a file','Decode a file','View Alphabets Codes','View Digits Code','Exit')
	MC = MossCode()
	x = 0
	while x != len(menus):
		x = choice(menus)
		if x == 1:
			print('The Moss Code is:',MC.encode_text(input('\nEnter the text: ')))
		elif x == 2:
			print('The plain text is :',MC.translate_code(input('\nEnter the code: ')))
		elif x == 3:
			MC.encode_file(input('\nEnter the file name: '))
		elif x == 4:
			MC.decode_file(input('\nEnter the file name: '))
		elif x == 5:
			my_print(MC.dictionary['Alphabets'])
		elif x == 6:
			my_print(MC.dictionary['Digits'])
		else:
			print('\nThank you!')
		print()

#main()
