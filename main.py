import pygame
import sys
import Pong.src.core.constants as constants
import Pong.src.core.resources as resources
"""
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((constants.width, constants.height))
pygame.display.set_caption("Pong")

player1 = (25, 335, 40, 115)
player2 = (885, 335, 40, 115)

player1_score = 0
player1_score_text = resources.scores_font.render(str(player1_score), True, (constants.WHITE))

player2_score = 0
player2_score_text = resources.scores_font.render(str(player2_score), True, (constants.WHITE))

def drawMiddle():
  for y_value in range(10, 801, 40):
    pygame.draw.rect(screen, constants.WHITE, (465, y_value, 10, 30))

while True:
  screen.fill(constants.BLACK)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      pygame.display.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        pygame.display.quit()
        sys.exit()

  pygame.draw.rect(screen, constants.WHITE, player1, border_radius=1)
  pygame.draw.rect(screen, constants.WHITE, player2, border_radius=1)

  drawMiddle()

  screen.blit(player1_score_text, (415, 20))
  screen.blit(player2_score_text, (485, 20))
  
  pygame.draw.circle(screen, constants.WHITE, (336, 440), 12)

  pygame.display.flip()"""

def main():
	pygame.init()
	screen = pygame.display.set_mode((constants.width, constants.height))
	clock = pygame.time.Clock()
	scene = GameScene()

	while True:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			scene.handle_event(event)
		
		scene.update()
		scene.draw(screen)
		pygame.display.flip()

if __name__ == "__main__": # Makes sure that only the main file can start the game
	main()