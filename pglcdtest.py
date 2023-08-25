# Implement a test programme on the waveshare 7.9" dsi lcd display
# using pygame and the pygame library

import pygame

# Initialise pygame
pygame.init()

# print information about the display
print(pygame.display.Info())

# print informaion  about the display modes
print(pygame.display.list_modes())


# set the screen size
screen = pygame.display.set_mode((400, 1280))

#draw a rectangle
pygame.draw.rect(screen, (255, 255, 255), (0, 0, 400, 1280))


#display text at 90 degrees clockwise, filling the full height of the display saying "THIS WAY UP"
font = pygame.font.SysFont("Arial", 250)
text = font.render("THIS WAY UP", True, (0, 0, 0))
text = pygame.transform.rotate(text, 90)
screen.blit(text, (0, 0))

# rota the screen 90 degrees clockwise
screen = pygame.transform.rotate(screen, 90)

#update the display
pygame.display.update()

# wait for 5 seconds
pygame.time.wait(2000)

# draw a rectangle filling the screen with blue
screen.fill((0, 0, 255))

#display text at 90 degrees clockwise, filling the full height of the display saying "THIS WAY UP"
font = pygame.font.SysFont("Arial", 250)
text = font.render("THIS WAY UP", True, (0, 0, 0))
text = pygame.transform.rotate(text, 90)
screen.blit(text, (0, 0))

# update the display
pygame.display.update()

# wait for 5 seconds
pygame.time.wait(2000)  

# draw a rectangle filling the screen with red
screen.fill((255, 0, 0))

#display text at 90 degrees clockwise, filling the full height of the display saying "THIS WAY UP"
font = pygame.font.SysFont("Arial", 250)
text = font.render("THIS WAY UP", True, (0, 0, 0))
text = pygame.transform.rotate(text, 90)
screen.blit(text, (0, 0))

# update the display
pygame.display.update()

# wait for 5 seconds
pygame.time.wait(2000)

# draw a rectangle filling the screen with green

screen.fill((0, 255, 0))
#display text at 90 degrees clockwise, filling the full height of the display saying "THIS WAY UP"
font = pygame.font.SysFont("Arial", 250)
text = font.render("THIS WAY UP", True, (0, 0, 0))
text = pygame.transform.rotate(text, 90)
screen.blit(text, (0, 0))

# update the display
pygame.display.update()

# wait for 5 seconds
pygame.time.wait(2000)

# end the programme
pygame.quit()

# end of programme

