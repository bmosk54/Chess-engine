import pygame
import itertools
import os
import chess

pygame.init() 
clock = pygame.time.Clock()
pygame.display.set_caption("Chess Engine")
board = chess.Board()
main_surface = pygame.display.set_mode((1000, 700))
moves_made = pygame.Surface((250,450))
square_size = 60
img_x, img_y = 48,58
width, height = 8*square_size, 8*square_size
chessboard = pygame.Surface((width, height))
tiles = []
main_surface.fill((54,69,79))
hover_color = (9,227,0)
click_color = (11,105,35)


white_pawns = pygame.image.load(os.path.join('White_pawn.png'))
white_pawns = pygame.transform.scale(white_pawns, (img_x,img_y))
white_rooks = pygame.image.load(os.path.join('White_rook.png'))
white_rooks = pygame.transform.scale(white_rooks, (img_x,img_y))
white_knights = pygame.image.load(os.path.join('White_knight.png'))
white_knights = pygame.transform.scale(white_knights, (img_x+8,img_y+2))
white_bishops = pygame.image.load(os.path.join('White_bishop.png'))
white_bishops = pygame.transform.scale(white_bishops, (img_x+10,img_y))
white_queen = pygame.image.load(os.path.join('White_queen.png'))
white_queen = pygame.transform.scale(white_queen, (img_x+8,img_y-2))
white_king = pygame.image.load(os.path.join('White_king.png'))
white_king = pygame.transform.scale(white_king, (img_x+8,img_y+3))
black_pawns = pygame.image.load(os.path.join('Black_pawn.png'))
black_pawns = pygame.transform.scale(black_pawns, (img_x+4,img_y+4))
black_rooks = pygame.image.load(os.path.join('Black_rook.png'))
black_rooks = pygame.transform.scale(black_rooks, (img_x+2,img_y))
black_knights = pygame.image.load(os.path.join('Black_knight.png'))
black_knights = pygame.transform.scale(black_knights, (img_x+8,img_y+2))
black_bishops = pygame.image.load(os.path.join('Black_bishop.png'))
black_bishops = pygame.transform.scale(black_bishops, (img_x+10,img_y))
black_queen = pygame.image.load(os.path.join('Black_queen.png'))
black_queen = pygame.transform.scale(black_queen, (img_x+8,img_y-2))
black_king = pygame.image.load(os.path.join('Black_king.png'))
black_king = pygame.transform.scale(black_king, (img_x+8,img_y+3))

pieceMap = {'P': white_pawns, 'B': white_bishops, 'N': white_knights, 'R': white_rooks, 'Q': white_queen, 'K': white_king,\
'p': black_pawns, 'b': black_bishops, 'n': black_knights, 'r': black_rooks, 'q': black_queen, 'k': black_king}

pieces = [white_pawns,white_rooks,white_knights,white_bishops,white_queen,white_king,\
black_pawns,black_knights,black_bishops,black_queen,black_king,black_rooks]

a8, a7, a6, a5, a4, a3, a2, a1, b8, b7, b6, b5, b4, b3, b2, b1, c8, c7, c6, c5, c4, c3, c2, c1, \
d8, d7, d6, d5, d4, d3, d2, d1, e8, e7, e6, e5, e4, e3, e2, e1, f8, f7, f6, f5, f4, f3, f2, f1, \
g8, g7, g6, g5, g4, g3, g2, g1, h8, h7, h6, h5, h4, h3, h2, h1 = (0,0,square_size,square_size),(0,60,square_size,square_size),(0,120,square_size,square_size),(0,180,square_size,square_size), \
(0,240,square_size,square_size),(0,300,square_size,square_size),(0,360,square_size,square_size),(0,420,square_size,square_size),(60,0,square_size,square_size),(60,60,square_size,square_size),(60,120,square_size,square_size),(60,180,square_size,square_size),(60,240,square_size,square_size),(60,300,square_size,square_size), \
(60,360,square_size,square_size),(60,420,square_size,square_size),(120,0,square_size,square_size),(120,60,square_size,square_size),(120,120,square_size,square_size),(120,180,square_size,square_size),(120,240,square_size,square_size),(120,300,square_size,square_size),(120,360,square_size,square_size), \
(120,420,square_size,square_size),(180,0,square_size,square_size),(180,60,square_size,square_size),(180,120,square_size,square_size),(180,180,square_size,square_size),(180,240,square_size,square_size),(180,300,square_size,square_size),(180,360,square_size,square_size),(180,420,square_size,square_size),(240,0,square_size,square_size), \
(240,60,square_size,square_size),(240,120,square_size,square_size),(240,180,square_size,square_size),(240,240,square_size,square_size),(240,300,square_size,square_size),(240,360,square_size,square_size),(240,420,square_size,square_size),(300,0,square_size,square_size),(300,60,square_size,square_size),(300,120,square_size,square_size), \
(300,180,square_size,square_size),(300,240,square_size,square_size),(300,300,square_size,square_size),(300,360,square_size,square_size),(300,420,square_size,square_size),(360,0,square_size,square_size),(360,60,square_size,square_size),(360,120,square_size,square_size),(360,180,square_size,square_size),(360,240,square_size,square_size), \
(360,300,square_size,square_size),(360,360,square_size,square_size),(360,420,square_size,square_size),(420,0,square_size,square_size),(420,60,square_size,square_size),(420,120,square_size,square_size),(420,180,square_size,square_size),(420,240,square_size,square_size),(420,300,square_size,square_size),(420,360,square_size,square_size), \
(420,420,square_size,square_size)

squareMap = {'a8':(0,0,square_size,square_size),'a7':(0,60,square_size,square_size),'a6':(0,120,square_size,square_size),'a5':(0,180,square_size,square_size), \
'a4':(0,240,square_size,square_size),'a3':(0,300,square_size,square_size),'a2':(0,360,square_size,square_size),'a1':(0,420,square_size,square_size),'b8':(60,0,square_size,square_size),'b7':(60,60,square_size,square_size),'b6':(60,120,square_size,square_size),'b5':(60,180,square_size,square_size),'b4':(60,240,square_size,square_size),'b3':(60,300,square_size,square_size), \
'b2':(60,360,square_size,square_size),'b1':(60,420,square_size,square_size),'c8':(120,0,square_size,square_size),'c7':(120,60,square_size,square_size),'c6':(120,120,square_size,square_size),'c5':(120,180,square_size,square_size),'c4':(120,240,square_size,square_size),'c3':(120,300,square_size,square_size),'c2':(120,360,square_size,square_size), \
'c1':(120,420,square_size,square_size),'d8':(180,0,square_size,square_size),'d7':(180,60,square_size,square_size),'d6':(180,120,square_size,square_size),'d5':(180,180,square_size,square_size),'d4':(180,240,square_size,square_size),'d3':(180,300,square_size,square_size),'d2':(180,360,square_size,square_size),'d1':(180,420,square_size,square_size),'e8':(240,0,square_size,square_size), \
'e7':(240,60,square_size,square_size),'e6':(240,120,square_size,square_size),'e5':(240,180,square_size,square_size),'e4':(240,240,square_size,square_size),'e3':(240,300,square_size,square_size),'e2':(240,360,square_size,square_size),'e1':(240,420,square_size,square_size),'f8':(300,0,square_size,square_size),'f7':(300,60,square_size,square_size),'f6':(300,120,square_size,square_size), \
'f5':(300,180,square_size,square_size),'f4':(300,240,square_size,square_size),'f3':(300,300,square_size,square_size),'f2':(300,360,square_size,square_size),'f1':(300,420,square_size,square_size),'g8':(360,0,square_size,square_size),'g7':(360,60,square_size,square_size),'g6':(360,120,square_size,square_size),'g5':(360,180,square_size,square_size),'g4':(360,240,square_size,square_size), \
'g3':(360,300,square_size,square_size),'g2':(360,360,square_size,square_size),'g1':(360,420,square_size,square_size),'h8':(420,0,square_size,square_size),'h7':(420,60,square_size,square_size),'h6':(420,120,square_size,square_size),'h5':(420,180,square_size,square_size),'h4':(420,240,square_size,square_size),'h3':(420,300,square_size,square_size),'h2':(420,360,square_size,square_size), \
'h1':(420,420,square_size,square_size)}

squares = [a8, a7, a6, a5, a4, a3, a2, a1, b8, b7, b6, b5, b4, b3, b2, b1, c8, c7, c6, c5, c4, c3, c2, c1, \
d8, d7, d6, d5, d4, d3, d2, d1, e8, e7, e6, e5, e4, e3, e2, e1, f8, f7, f6, f5, f4, f3, f2, f1, \
g8, g7, g6, g5, g4, g3, g2, g1, h8, h7, h6, h5, h4, h3, h2, h1]

c = 0
other_dictionary = {}
dictionary = {}
for x in ['1','2','3','4','5','6','7','8']:
	for y in ['a','b','c','d','e','f','g','h']:
		dictionary[y+x] = c
		other_dictionary[c] = y+x
		c = c+1

def drawBoard(board):

	global pieces

	square_size = 60
	width, height = 8*square_size, 8*square_size
	colors = itertools.cycle([(245,245,220), (128,0,0)])

	for x in range(0, width, square_size):
		for y in range(0, height, square_size):
			rect = (x, y, square_size, square_size)
			pygame.draw.rect(chessboard, next(colors), rect)
			tiles.append(rect)
		next(colors)

	for square in chess.SQUARES:
		piece = board.piece_at(square)
		myx = (square % 8) * square_size
		myy = (7 - square//8) * square_size
		if piece != None and piece.symbol() == 'P':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(white_pawns, (point))
		if piece != None and piece.symbol() == 'R':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(white_rooks, (point))
		if piece != None and piece.symbol() == 'N':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(white_knights, (point))
		if piece != None and piece.symbol() == 'B':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(white_bishops, (point))
		if piece != None and piece.symbol() == 'Q':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(white_queen, (point))
		if piece != None and piece.symbol() == 'K':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(white_king, (point))
		if piece != None and piece.symbol() == 'p':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(black_pawns, (point))
		if piece != None and piece.symbol() == 'r':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(black_rooks, (point))
		if piece != None and piece.symbol() == 'n':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(black_knights, (point))
		if piece != None and piece.symbol() == 'b':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(black_bishops, (point))
		if piece != None and piece.symbol() == 'q':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(black_queen, (point))
		if piece != None and piece.symbol() == 'k':
			point = (myx, myy, square_size, square_size)
			chessboard.blit(black_king, (point))

	pygame.display.update()

def hover():
	x,y = pygame.mouse.get_pos()
	for square in squares:
		clear = (0,0,0)
		square = pygame.draw.rect(chessboard,clear,square)
		square_x, square_y = square[0], square[1]
		for k,v in squareMap.items():
			if square == v:
				for move in board.legal_moves:
					if move.from_square == dictionary[k]:
						if square_x < x-100 < (square_x+square_size) and square_y < y-100 < (square_y+square_size):
							pygame.draw.rect(chessboard,hover_color,v)

def moves():    
	global pieces
	global squares
	colors = itertools.cycle([(245,245,220), (128,0,0)])

	for x in range(0, width, square_size):
		for y in range(0, height, square_size):
			rect = (x, y, square_size, square_size)
			pygame.draw.rect(chessboard, next(colors), rect)
			tiles.append(rect)
		next(colors)

	exit = False
	val = None
	colorMe = False
	clicked = False
	key = 0
	while not exit:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT: 
			exit = True  
		if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and not clicked:
			for square in squares:
				clear = (0,0,0)
				square = pygame.draw.rect(chessboard,clear,square)
				x,y = pygame.mouse.get_pos()
				square_x, square_y = square[0], square[1]
				if square_x < x-100 < (square_x+square_size) and square_y < y-100 < (square_y+square_size):
					for k,v in squareMap.items():
						if square == v:
							if board.piece_at(dictionary[k]) != None:
								colorMe = True
								key = k
								val = v	
								piece_from = k
								clicked = True
		elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and clicked:
			for square in squares:
				x,y = pygame.mouse.get_pos()
				square_x, square_y = square[0], square[1]
				if square_x < x-100 < (square_x+square_size) and square_y < y-100 < (square_y+square_size):
					for k,v in squareMap.items():
						if square == v:
							piece_to = k
							clicked = False
							board_move = chess.Move.from_uci(piece_from + piece_to)
							if board_move in board.legal_moves:
								board.push(board_move)
								drawBoard(board)
								colorMe = False


		main_surface.blit(chessboard, (100, 100))
		main_surface.blit(moves_made, (625, 100))
		drawBoard(board)
		if colorMe:
			pygame.draw.rect(chessboard,click_color,val)
			for p, pic in pieceMap.items():
				symbol = board.piece_at(dictionary[key])
				myx = (dictionary[key] % 8) * 60
				myy = (7 - dictionary[key]//8) * 60
				point = (myx, myy, 60, 60)
				if symbol.symbol() == p:
					chessboard.blit(pic, (point))
					hover()
			#colorMe = False
		clock.tick(30)
moves()
