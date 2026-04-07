import pygame
import Pong.src.core.constants as constants


pygame.font.init()

try:
	font_path = "C://Users//wilso//Desktop//All.py//Arcade Central//press_start_2p//PressStart2P-Regular.ttf"
	pygame.font.Font(font_path, 30)
	scores_font = pygame.font.Font(font_path, 45)
	pygame.font.Font(font_path, 90)
except:
	print(f"{constants.TERMINAL_RED}Error loading font pack{constants.TERMINAL_RESET}")
	scores_font = pygame.font.Font(None, 45)
