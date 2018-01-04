import chess
import chess.polyglot
import random
import chess.svg

from IPython.display import SVG

board = chess.Board("8/8/8/8/4N3/8/8/8 w - - 0 1")
squares = board.attacks(chess.E4)
SVG(chess.svg.board(board=board, squares=squares)) 
board = chess.Board()
move_list = []
gameOver = False

def read_move_list():
	global move_list
	move_list = []
	with chess.polyglot.open_reader("performance.bin") as reader:
		for move in reader.find_all(board):
			move_list.append(move)	

def choose_move_open():
	global move_list
	sum_ = 0
	probability_list = []
	move_list = []

	with chess.polyglot.open_reader("performance.bin") as reader:
		for move in reader.find_all(board):
			sum_ += move.weight
			move_list.append(move)
	#with chess.polyglot.open_reader("performance.bin") as reader:
		total = 0.0
		for move in reader.find_all(board):
			probability = move.weight/sum_
			total = total + probability
			probability_list.append(total)
		for value in probability_list:
			print(value)
		choice = random.random()
		for i in range(0, len(move_list)):
			if choice < probability_list[i]:
				board.push(move_list[i].move())
				print(move_list[i].move())
				break;
##### Piece-square tables #####
Pieces = {'P': 100, 'N': 300, 'B': 300, 'R': 500, 'Q':900, 'K': 10000, 'p': 100, 'n': 300, 'b': 300, 'r': 500, 'q':900, 'k': 10000}

values = {}
#pawn

values['P']=[0,  0,  0,  0,  0,  0,  0,  0,
	5, 10, 10, -20, -20, 10, 10, 5,
	5, -5, -10, 0, 0, -10, -5, 5,
 	0,  0, 0, 20, 20, 0,  0,  0,
 	5,  5, 10, 25, 25, 10,  5,  5,
 	10, 10, 20, 30, 30, 20, 10, 10,
	50, 50, 50, 70, 70, 50, 50, 50,
	0,  0,  0,  0,  0,  0,  0,  0]

 #knight
values['N']= [-50,-40,-30,-30,-30,-30,-40,-50,
	-40,-20,  0,  5,  5,  0,-20,-40,
	-30,  5, 10, 15, 15, 10,  5,-30,
	-30,  0, 15, 20, 20, 15,  0,-30,
	-30,  5, 15, 20, 20, 15,  5,-30,
	-30,  0, 10, 15, 15, 10,  0,-30,
	-40,-20,  0,  0,  0,  0,-20,-40,
	-50,-40,-30,-30,-30,-30,-40,-50]

#bishop
values['B']=[-20,-10,-10,-10,-10,-10,-10,-20,
	-10,  5,  0,  0,  0,  0,  5,-10,
	-10,  10, 10, 10, 10, 10, 10,-10,
	-10,  0,  10, 10, 10, 10, 0,-10,
	-10,  5,  5,  10, 10, 5,  5,-10,
	-10,  0,  5,  10, 10, 5,  0,-10,
	-10,  0,  0,  0,  0,  0,  0,-10,
	-20,-10,-10, -10,-10,-10,-10,-20]

#rook
values['R']=[0,  0,  0,  0,  0,  0,  0,  0,
	-5,  0,  0,  0,  0,  0,  0,  -5,
	-5,  0,  0,  0,  0,  0,  0, -5,
	-5,  0,  0,  0,  0,  0,  0, -5,
	-5,  0,  0,  0,  0,  0,  0, -5,
	-5,  0,  0,  0,  0,  0,  0, -5,
	5,  10, 10, 10, 10, 10, 10, -5,
	0,  0,  0,  5,  5,  0,  0,  0]

#queen
values['Q']=[-20,-10,-10, -5, -5,-10,-10,-20,
	-10,  0,  0,  0,  0,  0,  0,-10,
	-10,  0,  5,  5,  5,  5,  0,-10,
	0,  0,  5,  5,  5,  5,  0, -5,
	-5,  0,  5,  5,  5,  5,  0, -5,
	-10,  5,  5,  5,  5,  5,  0,-10,
	-10,  0,  5,  0,  0,  0,  0,-10,
	-20,-10,-10, -5, -5,-10,-10,-20]

#king middle game
values['K']=[20, 30, 10,  0,  0, 10, 30, 20,
	20, 20,  0,  0,  0,  0, 20, 20,
	-10,-20,-20,-20,-20,-20,-20,-10,
	-20,-30,-30,-40,-40,-30,-30,-20,
	-30,-40,-40,-50,-50,-40,-40,-30,
	-30,-40,-40,-50,-50,-40,-40,-30,
	-30,-40,-40,-50,-50,-40,-40,-30,
	-30,-40,-40,-50,-50,-40,-40,-30]

#King endgame
"""	-50,-40,-30,-20,-20,-30,-40,-50,
	-30,-20,-10,  0,  0,-10,-20,-30,
	-30,-10, 20, 30, 30, 20,-10,-30,
	-30,-10, 30, 40, 40, 30,-10,-30,
	-30,-10, 30, 40, 40, 30,-10,-30,
	-30,-10, 20, 30, 30, 20,-10,-30,
	-30,-30,  0,  0,  0,  0,-30,-30,
	-50,-30,-30,-30,-30,-30,-30,-50
"""
values['p']=[0,  0,  0,  0,  0,  0,  0,  0,
	50, 50, 50, 70, 70, 50, 50, 50,
	10, 10, 20, 30, 30, 20, 10, 10,
 	5,  5, 10, 25, 25, 10,  5,  5,
 	0,  0,  0, 20, 20,  0,  0,  0,
 	5, -5,-10,  0,  0,-10, -5,  5,
	5, 10, 10,-20,-20, 10, 10,  5,
	0,  0,  0,  0,  0,  0,  0,  0]

 #knight
values['n']= [-50,-40,-30,-30,-30,-30,-40,-50,
	-40,-20,  0,  0,  0,  0,-20,-40,
	-30,  0, 10, 15, 15, 10,  0,-30,
	-30,  5, 15, 20, 20, 15,  5,-30,
	-30,  0, 15, 20, 20, 15,  0,-30,
	-30,  5, 10, 15, 15, 10,  5,-30,
	-40,-20,  0,  5,  5,  0,-20,-40,
	-50,-40,-30,-30,-30,-30,-40,-50]

#bishop
values['b']=[-20,-10,-10,-10,-10,-10,-10,-20,
	-10,  0,  0,  0,  0,  0,  0,-10,
	-10,  0,  5, 10, 10,  5,  0,-10,
	-10,  5,  5, 10, 10,  5,  5,-10,
	-10,  0, 10, 10, 10, 10,  0,-10,
	-10, 10, 10, 10, 10, 10, 10,-10,
	-10,  5,  0,  0,  0,  0,  5,-10,
	-20,-10,-10,-10,-10,-10,-10,-20]
#rook
values['r']=[0,  0,  0,  0,  0,  0,  0,  0,
	5, 10, 10, 10, 10, 10, 10,  5,
	-5,  0,  0,  0,  0,  0,  0, -5,
	-5,  0,  0,  0,  0,  0,  0, -5,
	-5,  0,  0,  0,  0,  0,  0, -5,
	-5,  0,  0,  0,  0,  0,  0, -5,
	-5,  0,  0,  0,  0,  0,  0, -5,
	0,  0,  0,  5,  5,  0,  0,  0]

#queen
values['q']=[-20,-10,-10, -5, -5,-10,-10,-20,
	-10,  0,  0,  0,  0,  0,  0,-10,
	-10,  0,  5,  5,  5,  5,  0,-10,
	-5,  0,  5,  5,  5,  5,  0, -5,
	0,  0,  5,  5,  5,  5,  0, -5,
	-10,  5,  5,  5,  5,  5,  0,-10,
	-10,  0,  5,  0,  0,  0,  0,-10,
	-20,-10,-10, -5, -5,-10,-10,-20]

#king
values['k']=[-30,-40,-40,-50,-50,-40,-40,-30,
	-30,-40,-40,-50,-50,-40,-40,-30,
	-30,-40,-40,-50,-50,-40,-40,-30,
	-30,-40,-40,-50,-50,-40,-40,-30,
	-20,-30,-30,-40,-40,-30,-30,-20,
	-10,-20,-20,-20,-20,-20,-20,-10,
	20, 20,  0,  0,  0,  0, 20, 20,
	20, 30, 10,  0,  0, 10, 30, 20]


cmap = board.piece_map()
score = 0
piece_scores = {'P': 0, 'N': 0, 'B': 0, 'R': 0, 'Q':0, 'K': 0, 'p': 0, 'n': 0, 'b': 0, 'r': 0, 'q':0, 'k': 0}
turn = 0

#- .3 * (wD * wI - bD * bI)
#+ .1 * (wM - bM)

'''print(material_score)
board.push_san('e4')
print (board)
print (piece_scores['P'])
'''

### Minimax search algorithm ###
#pop moves after pushed
def minimax(position, depth):
	global turn
	global material_score
	if depth == 0 or board.is_checkmate():
		return (material_score, None)
	else:
		if (depth % 2 == 0): #White's turn
			best_score = 999999
			best_move = None
			for move in board.legal_moves:
				new_pos = board.push(move)
				material_score, move = minimax(new_pos, depth - 1)
				board.pop()
				if material_score < best_score:  #white minimizes score
					best_score = score
					best_move = move
			return(best_score, best_move)
		else:
			best_score = -999999
			best_move = None
			for move in board.legal_moves:
				new_pos = board.push(move)
				#print(board)
				material_score, move = minimax(new_pos, depth - 1)
				#print("%s is the material score" %material_score)
				#print("%s move" %move)
				board.pop()
				if material_score > best_score:  #black maximizes score
					best_score = material_score
					best_move = move
					#print (best_move)
			return(best_score, best_move)
			print(best_move)
			print ("here")

# main loop
			
read_move_list()
while not gameOver:
	for piece in Pieces:
		for square in chess.SQUARES:
			if square in cmap:
				#print (cmap[square].symbol())
				if cmap[square].symbol() == piece:
					score += values[piece][square]
					score += Pieces[piece]
					piece_scores[piece] += Pieces[piece] + values[piece][square]
				else:
					pass

	material_score = (piece_scores['K'] - piece_scores['k']
	+ piece_scores['Q'] - piece_scores['q']
	+ piece_scores['R'] - piece_scores['r']
	+ piece_scores['B'] + piece_scores['N'] - piece_scores['b'] - piece_scores['n']
	+ piece_scores['P'] - piece_scores['p']) 
	print (board)
	if turn % 2 == 0 and len(move_list) > 0:
		print (material_score)
		valid = False	
		while valid == False: 
			try:
				user_move = input()
				board.push_san(user_move)
				valid = True
			except ValueError:
				print("Illegal move!")
	elif not turn % 2 ==0 and len(move_list) > 0:
		read_move_list()
		choose_move_open()
	else:
		print("out of opening")
		score, move = minimax(board, 3)	
		board.push(best_move)
	turn +=1
	material_score = 0
