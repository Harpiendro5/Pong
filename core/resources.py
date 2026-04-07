import pygame
import Pong.src.core.constants as constants


pygame.font.init()

try:
	font_path = ""
	pygame.font.Font(font_path, 30)
	scores_font = pygame.font.Font(font_path, 45)
	pygame.font.Font(font_path, 90)
except:
	print(f"{constants.TERMINAL_RED}Error loading font pack{constants.TERMINAL_RESET}")
	scores_font = pygame.font.Font(None, 45)
