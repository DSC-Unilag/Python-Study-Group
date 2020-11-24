class TicTacToe:
	'''
This is a game that simulate a common game played by teenagers called Tic Tac Toe.
	
Tic Tac Toe is a common game played by children and teenagers. It is a game that requires two

players to fill in the available spots in a 3x3 grid such that a player wins once he is able to have

3 of his character all lined horizontally, vertically or diagonally while the opponent plays to

prevent the first from achieving that.

Each player has three characters:
	player1: A1, A2 and A3
	player2: B1, B2 and B3
At first each player will be given chance to choose his initial position in turn, untill all 6 characters are placed on the board.
if no player wins, then continously untill one player wins each player will be given chance turn-wise to choose a character and move it to his choosen position.
There are a total of 9 positions labelled (1 - 9), with atleast 3 vacant positions at each instance.
	'''
	
	#this var is the visual display of the game
	game = [[0 for x in range(3)] for x in range(3)]
	
	#this variable keep track of vacant positions
	vacant = [x+1 for x in range(9)]
	
	#p1 and p2 stores the current positions of player1 and player2 respectively
	p1 = []
	p2 = []
	
	def __init__(self):
		x = 1
		for i in range(3):
			for j in range(3):
				self.game[i][j] = x
				x += 1
	
	#this fxn displays the game in a tabular form
	def display(self):
		print('-'*13)
		for i in range(3):
			for j in range(3):
				print('|{:^3}'.format(self.game[i][j]),end='')
			print('|')
			print('-'*13)
	
	#this fxn initially allows players to place their players in respective positions
	def initialise_players(self):
		
		x = 0
		pls = ('Player 1', 'Player 2')
		pvals = (self.p1,self.p2)
		chars = 'AB'
		
		while len(self.p1) + len(self.p2) < 6:
			self.display()
			n = str(len(pvals[x]) + 1)
			a = 0
			
			while True:
				a = int(input(pls[x] + "'s turn..\nChoose position to place your character" + n + ': '))
				if a in self.vacant:
					break
				else:
					print('Invalid position!')
					
			for i in range(3):
				for j in range(3):
					if self.game[i][j] == a:
						self.game[i][j] = chars[x] + n
						pvals[x].append(a)
						self.vacant.remove(a)
						break
			x = 1 if x == 0 else 0
		return self.check_win()
	#end of fxn initialise
	
	#fxn to move characters in the game	
	def move_character(self, player = 0):
		
		self.display()
		print((('Player1','Player2')[player] + "'s turn...").center(20))
		frm_options = (('A1','A2','A3'),('B1','B2','B3'))[player]
		pl = self.p1 if player == 0 else self.p2
		
		frm = ''
		while True:
			frm = input('which character do you want to move?: ').upper()
			if frm in frm_options:
				break
			else:
				print('Invalid choice')
		
		to = 0
		while True:
			to = int(input('To what position?: '))
			if to in self.vacant:
				break
			else:
				print('position not available!')
		
		x = 1
		for i in range(3):
			for j in range(3):
				if self.game[i][j] == frm:
					self.game[i][j] = x
					pl.remove(x)
					self.vacant.append(x)
				if self.game[i][j] == to:
					self.game[i][j] = frm
					pl.append(x)
					self.vacant.remove(x)
				x += 1
	#end of fxn move character
	
	#fxn to check if one player has won the game
	def check_win(self):
		wins = ([1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7])
		if sorted(self.p1) in wins:
			print('='*30)
			print('Player1 wins!'.center(30))
			print('='*30)
			return True
		elif sorted(self.p2) in wins:
			print('='*30)
			print('Player2 wins!')
			print('='*30)
			return True
		else:
			return False
	#end of fxn check win
	
#end of clas TicTacToe	
						
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

def main():
	menus = ('Start Game','Help','Exit')
	T = TicTacToe()
	x = 0
	while x != 3:
		x = choice(menus)
		if x == 1:
			break
		elif x == 2:
			print(T.__doc__)
		else:
			print('Thank you have a nice day!')
			return
			
	print(' Tic Tac Toc Game '.center(30,'='))
	if not T.initialise_players():
		x = 0
		while not T.check_win():
			T.move_character(x)
			x = 1 if x == 0 else 0
	if input('Do you wish to restart? :').lower()[0] == 'y':
		print()
		main()
	else:
		print('Thank you have a nice day!')
main()