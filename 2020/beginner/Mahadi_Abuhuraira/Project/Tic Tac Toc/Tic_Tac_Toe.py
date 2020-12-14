import random as rnd
from time import sleep

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
	
	
	titles = ['Player 1', 'Player 2']
	
	def __init__(self):
		self.p1 = []
		self.p2 = []
		self.game = [x+1 for x in range(9)]
		self.vacant = [x+1 for x in range(9)]
		self.single = False
	
		
	def play(self,single = 0):
		self.single = single
		print(' Tic Tac Toc Game '.center(30,'='))
		if not self.initialise_players():
			x = 0
			while not self.check_win():
				self.move_character(x)
				x = 1 if x == 0 else 0
			
	def display(self):
		#this fxn displays the game in a tabular form
		print('-'*13)
		x = 0
		for i in range(3):
			for j in range(3):
				print('|{:^3}'.format(self.game[x]),end='')
				x += 1
			print('|')
			print('-'*13)
	#end of fxn display
	
	def get_input(self,player = 0, type = 0):
		'''This fxn accepts inputs from players
		player: indicate the player passing the input
		type: if 0 means we are getting position else its getting
		character'''
		
		pl = (self.p1,self.p2)[player]
		domain = (self.vacant,(('A1','A2','A3'),('B1','B2','B3'))[player])[type]
		prompt = (
		'Choose position to place: ',
		'Choose player to move: '
		)[type]
		fxn = (int,str)[type]
		while True:
			res = fxn(input(prompt))
			if type == 1:
				res = res.upper()
			if res in domain:
				return res
			else:
				print('wrong choice!')
	#end of fxn get_input		

	def initialise_players(self):
		'''this fxn initially allows players to place their players in
		respectively in their desired position'''
			
		if self.single:
			self.titles[0] = 'Computer'
		x = 1
		pls = (self.p1,self.p2)
		chars = 'AB'
		while len(self.p1) + len(self.p2) < 6:
			x = 1 if x == 0 else 0
			self.display()
			print(self.titles[x] + "'s turn...")
			n = len(pls[x]) + 1
			frm = 0
			if self.single and x == 0:
				self.auto_move('A' + str(n))
				continue
			else:
				frm = self.get_input(x)		
			self.game[frm-1] = chars[x] + str(n)
			self.vacant.remove(frm)
			pls[x].append(frm)
			
		return self.check_win()
	#end of fxn initialise
	
	
	def swap(self,frm,to,player = 0):
		'''This fxn changes position for a given character
		of a given player'''
		
		pl = (self.p1,self.p2)[player]
		ind = self.game.index(frm)
		self.game[to -1] = frm
		self.game[ind] = ind + 1
		pl.remove(ind + 1)
		self.vacant.remove(to)
		pl.append(to)
		self.vacant.append(ind + 1)
	#end of fxn swap
		
	def auto_move(self, initial = False):
		'''This fxn is used when playing against computer
		to automatically move characters on the board.
		initial: if True indicates that its at the begining
		of the game during initialisation'''
		
		to = rnd.choice(self.vacant)
		sleep(1)
		if initial:
			self.game[to - 1] = initial
			self.vacant.remove(to)
			self.p1.append(to)
			return
		frm = self.game[rnd.choice(self.p1) - 1]
		self.swap(frm,to)
	#end of fxn auto_move	
		
	def move_character(self, player = 0):
		'''This fxn allows players to move their characters
		accross the board.
		player: if 0 means player 1 else player 2
		'''
		self.display()
		print((self.titles[player] + "'s turn...").center(20))
		if self.single and player == 0:
			self.auto_move()
			return
		frm = self.get_input(player,1)
		to = self.get_input(player)
		self.swap(frm,to,player)	
	#end of fxn move character
	
	def check_win(self):
		#fxn to check if one player has won the game
		wins = ([1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7])
		x = -1
		if sorted(self.p1) in wins :
			x = 0
		elif sorted(self.p2) in wins:
			x = 1
		else:
			return False
		print('='*30)
		print(self.titles[x],' wins!')
		print('='*30)
		return True
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
	x = 0
	T = TicTacToe()
	while x != 3:
		x = choice(menus)
		if x == 1:
			y = choice(('Multiplayer','Vs Computer'))
			T.play(y-1)
		elif x == 2:
			print(T.__doc__)
		else:
			print('Thank you have a nice day!')
	#end of while loop
	
#end of main

main()