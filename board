import pygame
import itertools
import os

main_surface = pygame.display.set_mode((1000, 700))
square_size = 60
width, height = 8*square_size, 8*square_size
background = pygame.Surface((width, height))


def draw_board():
	clock = pygame.time.Clock()
	pygame.init()     

	colors = itertools.cycle([(245,245,220), (128,0,0)])
	squares = []

	for x in range(0, width, square_size):
		for y in range(0, height, square_size):
			rect = (x, y, square_size, square_size)
			pygame.draw.rect(background, next(colors), rect)
			squares.append(rect)
		next(colors)

	exit = False
	
	a8, a7, a6, a5, a4, a3, a2, a1, b8, b7, b6, b5, b4, b3, b2, b1, c8, c7, c6, c5, c4, c3, c2, c1, \
	d8, d7, d6, d5, d4, d3, d2, d1, e8, e7, e6, e5, e4, e3, e2, e1, f8, f7, f6, f5, f4, f3, f2, f1, \
	g8, g7, g6, g5, g4, g3, g2, g1, h8, h7, h6, h5, h4, h3, h2, h1 = squares[0], squares[1], squares[2], \
	squares[3], squares[4], squares[5], squares[6], squares[7], squares[8], squares[9], squares[10],\
	squares[11], squares[12], squares[13], squares[14], squares[15], squares[16], squares[17], squares[18], \
	squares[19], squares[20], squares[21], squares[22], squares[23], squares[24], squares[25], squares[26], \
	squares[27], squares[28], squares[29], squares[30], squares[31], squares[32], squares[33], squares[34], \
	squares[35], squares[36], squares[37], squares[38], squares[39], squares[40], squares[41], squares[42], \
	squares[43], squares[44], squares[45], squares[46], squares[47], squares[48], squares[49], squares[50], \
	squares[51], squares[52], squares[53], squares[54], squares[55], squares[56], squares[57], squares[58], \
	squares[59], squares[60], squares[61], squares[62], squares[63]

	while not exit:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT: 
			exit = True                  
		
		main_surface.fill((54,69,79))
		main_surface.blit(background, (100, 100))
		
		white_king = pygame.image.load(os.path.join('White_king.png'))
		background.blit(white_king, (e1))
		white_queen = pygame.image.load(os.path.join('White_queen.png'))
		background.blit(white_queen, (d1))
		white_rook_a = pygame.image.load(os.path.join('White_rook.png'))
		background.blit(white_rook_a, (a1))
		white_rook_h = pygame.image.load(os.path.join('White_rook.png'))
		background.blit(white_rook_a, (h1))
		white_knight_b = pygame.image.load(os.path.join('White_knight.png'))
		background.blit(white_knight_b, (b1))
		white_knight_g = pygame.image.load(os.path.join('White_knight.png'))
		background.blit(white_knight_g, (g1))
		white_bishop_c = pygame.image.load(os.path.join('White_bishop.png'))
		background.blit(white_bishop_c, (c1))
		white_bishop_f = pygame.image.load(os.path.join('White_bishop.png'))
		background.blit(white_bishop_f, (f1))
		white_pawn_a = pygame.image.load(os.path.join('White_pawn.png'))
		background.blit(white_pawn_a, (a2))
		white_pawn_b = pygame.image.load(os.path.join('White_pawn.png'))
		background.blit(white_pawn_b, (b2))
		white_pawn_c = pygame.image.load(os.path.join('White_pawn.png'))
		background.blit(white_pawn_c, (c2))
		white_pawn_d = pygame.image.load(os.path.join('White_pawn.png'))
		background.blit(white_pawn_d, (d2))
		white_pawn_e = pygame.image.load(os.path.join('White_pawn.png'))
		background.blit(white_pawn_e, (e2))
		white_pawn_f = pygame.image.load(os.path.join('White_pawn.png'))
		background.blit(white_pawn_f, (f2))
		white_pawn_g = pygame.image.load(os.path.join('White_pawn.png'))
		background.blit(white_pawn_g, (g2))
		white_pawn_h = pygame.image.load(os.path.join('White_pawn.png'))
		background.blit(white_pawn_h, (h2))
		black_king = pygame.image.load(os.path.join('Black_king.png'))
		background.blit(black_king, (e8))
		black_queen = pygame.image.load(os.path.join('Black_queen.png'))
		background.blit(black_queen, (d8))
		black_rook_a = pygame.image.load(os.path.join('Black_rook.png'))
		background.blit(black_rook_a, (a8))
		black_rook_h = pygame.image.load(os.path.join('Black_rook.png'))
		background.blit(black_rook_a, (h8))
		black_knight_b = pygame.image.load(os.path.join('Black_knight.png'))
		background.blit(black_knight_b, (b8))
		black_knight_g = pygame.image.load(os.path.join('Black_knight.png'))
		background.blit(black_knight_g, (g8))
		black_bishop_c = pygame.image.load(os.path.join('Black_bishop.png'))
		background.blit(black_bishop_c, (c8))
		black_bishop_f = pygame.image.load(os.path.join('Black_bishop.png'))
		background.blit(black_bishop_f, (f8))
		black_pawn_a = pygame.image.load(os.path.join('Black_pawn.png'))
		background.blit(black_pawn_a, (a7))
		black_pawn_b = pygame.image.load(os.path.join('Black_pawn.png'))
		background.blit(black_pawn_b, (b7))
		black_pawn_c = pygame.image.load(os.path.join('Black_pawn.png'))
		background.blit(black_pawn_c, (c7))
		black_pawn_d = pygame.image.load(os.path.join('Black_pawn.png'))
		background.blit(black_pawn_d, (d7))
		black_pawn_e = pygame.image.load(os.path.join('Black_pawn.png'))
		background.blit(black_pawn_e, (e7))
		black_pawn_f = pygame.image.load(os.path.join('Black_pawn.png'))
		background.blit(black_pawn_f, (f7))
		black_pawn_g = pygame.image.load(os.path.join('Black_pawn.png'))
		background.blit(black_pawn_g, (g7))
		black_pawn_h = pygame.image.load(os.path.join('Black_pawn.png'))
		background.blit(black_pawn_h, (h7))

		pygame.display.flip()
		clock.tick(30)
		pygame.display.set_caption("Chess Engine")

	pygame.quit()

draw_board()
