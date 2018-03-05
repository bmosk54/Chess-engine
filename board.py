import pygame
import itertools
import os
import chess

def drawBoard(board):

	pygame.init() 
	clock = pygame.time.Clock()
	pygame.display.set_caption("Chess Engine")
	board = chess.Board()

	square_size = 60
	width, height = 8*square_size, 8*square_size
	colors = itertools.cycle([(245,245,220), (128,0,0)])

	for x in range(0, width, square_size):
		for y in range(0, height, square_size):
			rect = (x, y, square_size, square_size)
			pygame.draw.rect(background, next(colors), rect)
			tiles.append(rect)
		next(colors)

	for square in chess.SQUARES:
		piece = board.piece_at(square)
		myx = (square % 8) * square_size
		myy = (7 - square//8) * square_size
		if piece != None and piece.symbol() == 'P':
			point = (myx, myy, square_size, square_size)
			white_pawns = pygame.image.load(os.path.join('White_pawn.png'))
			background.blit(white_pawns, (point))
		if piece != None and piece.symbol() == 'R':
			point = (myx, myy, square_size, square_size)
			white_rooks = pygame.image.load(os.path.join('White_rook.png'))
			background.blit(white_rooks, (point))
		if piece != None and piece.symbol() == 'N':
			point = (myx, myy, square_size, square_size)
			white_knights = pygame.image.load(os.path.join('White_knight.png'))
			background.blit(white_knights, (point))
		if piece != None and piece.symbol() == 'B':
			point = (myx, myy, square_size, square_size)
			white_bishops = pygame.image.load(os.path.join('White_bishop.png'))
			background.blit(white_bishops, (point))
		if piece != None and piece.symbol() == 'Q':
			point = (myx, myy, square_size, square_size)
			white_queen = pygame.image.load(os.path.join('White_queen.png'))
			background.blit(white_queen, (point))
		if piece != None and piece.symbol() == 'K':
			point = (myx, myy, square_size, square_size)
			white_king = pygame.image.load(os.path.join('White_king.png'))
			background.blit(white_king, (point))
		if piece != None and piece.symbol() == 'p':
			point = (myx, myy, square_size, square_size)
			black_pawns = pygame.image.load(os.path.join('Black_pawn.png'))
			background.blit(black_pawns, (point))
		if piece != None and piece.symbol() == 'r':
			point = (myx, myy, square_size, square_size)
			black_rooks = pygame.image.load(os.path.join('Black_rook.png'))
			background.blit(black_rooks, (point))
		if piece != None and piece.symbol() == 'n':
			point = (myx, myy, square_size, square_size)
			black_knights = pygame.image.load(os.path.join('Black_knight.png'))
			background.blit(black_knights, (point))
		if piece != None and piece.symbol() == 'b':
			point = (myx, myy, square_size, square_size)
			black_bishops = pygame.image.load(os.path.join('Black_bishop.png'))
			background.blit(black_bishops, (point))
		if piece != None and piece.symbol() == 'q':
			point = (myx, myy, square_size, square_size)
			black_queen = pygame.image.load(os.path.join('Black_queen.png'))
			background.blit(black_queen, (point))
		if piece != None and piece.symbol() == 'k':
			point = (myx, myy, square_size, square_size)
			black_king = pygame.image.load(os.path.join('Black_king.png'))
			background.blit(black_king, (point))
	pygame.display.update()


main_surface = pygame.display.set_mode((1000, 700))
square_size = 60
width, height = 8*square_size, 8*square_size
background = pygame.Surface((width, height))
tiles = []

a8, a7, a6, a5, a4, a3, a2, a1, b8, b7, b6, b5, b4, b3, b2, b1, c8, c7, c6, c5, c4, c3, c2, c1, \
d8, d7, d6, d5, d4, d3, d2, d1, e8, e7, e6, e5, e4, e3, e2, e1, f8, f7, f6, f5, f4, f3, f2, f1, \
g8, g7, g6, g5, g4, g3, g2, g1, h8, h7, h6, h5, h4, h3, h2, h1 = (0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0), \
(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0), \
(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0), \
(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0), \
(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0), \
(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0), \
(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0)

squares = [a8, a7, a6, a5, a4, a3, a2, a1, b8, b7, b6, b5, b4, b3, b2, b1, c8, c7, c6, c5, c4, c3, c2, c1, \
d8, d7, d6, d5, d4, d3, d2, d1, e8, e7, e6, e5, e4, e3, e2, e1, f8, f7, f6, f5, f4, f3, f2, f1, \
g8, g7, g6, g5, g4, g3, g2, g1, h8, h7, h6, h5, h4, h3, h2, h1]

def new_game():    

	colors = itertools.cycle([(245,245,220), (128,0,0)])

	for x in range(0, width, square_size):
		for y in range(0, height, square_size):
			rect = (x, y, square_size, square_size)
			pygame.draw.rect(background, next(colors), rect)
			tiles.append(rect)
		next(colors)

	exit = False
	
	global a8, a7, a6, a5, a4, a3, a2, a1, b8, b7, b6, b5, b4, b3, b2, b1, c8, c7, c6, c5, c4, c3, c2, c1, \
	d8, d7, d6, d5, d4, d3, d2, d1, e8, e7, e6, e5, e4, e3, e2, e1, f8, f7, f6, f5, f4, f3, f2, f1, \
	g8, g7, g6, g5, g4, g3, g2, g1, h8, h7, h6, h5, h4, h3, h2, h1
	
	a8, a7, a6, a5, a4, a3, a2, a1, b8, b7, b6, b5, b4, b3, b2, b1, c8, c7, c6, c5, c4, c3, c2, c1, \
	d8, d7, d6, d5, d4, d3, d2, d1, e8, e7, e6, e5, e4, e3, e2, e1, f8, f7, f6, f5, f4, f3, f2, f1, \
	g8, g7, g6, g5, g4, g3, g2, g1, h8, h7, h6, h5, h4, h3, h2, h1 = tiles[0], tiles[1], tiles[2], \
	tiles[3], tiles[4], tiles[5], tiles[6], tiles[7], tiles[8], tiles[9], tiles[10],\
	tiles[11], tiles[12], tiles[13], tiles[14], tiles[15], tiles[16], tiles[17], tiles[18], \
	tiles[19], tiles[20], tiles[21], tiles[22], tiles[23], tiles[24], tiles[25], tiles[26], \
	tiles[27], tiles[28], tiles[29], tiles[30], tiles[31], tiles[32], tiles[33], tiles[34], \
	tiles[35], tiles[36], tiles[37], tiles[38], tiles[39], tiles[40], tiles[41], tiles[42], \
	tiles[43], tiles[44], tiles[45], tiles[46], tiles[47], tiles[48], tiles[49], tiles[50], \
	tiles[51], tiles[52], tiles[53], tiles[54], tiles[55], tiles[56], tiles[57], tiles[58], \
	tiles[59], tiles[60], tiles[61], tiles[62], tiles[63]

	while not exit:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT: 
			exit = True  
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x,y = ev.pos
			print (x,y)
			'''for square in squares:
				if square.rect.collidepoint(x,y):
					print(squares)     '''  
		
		main_surface.fill((54,69,79))
		main_surface.blit(background, (100, 100))

		drawBoard(board)
		clock.tick(30)
new_game()
