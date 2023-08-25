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

# Variable to keep the main loop running
running = True

# Main loop
while running:
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop
            if event.key == pygame.K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop
        elif event.type == pygame.QUIT:
            running = False 
    #draw a rectangle
    #pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1280, 400))


        #display the position of the mouse on the screen with a small circle
        mousepos= pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255, 0, 0), (mousepos[0],mousepos[1]), 10)


        #display text at 90 degrees clockwise, filling the full height of the display saying "THIS WAY UP"
        font = pygame.font.SysFont("Arial", 12)
        mousepos= pygame.mouse.get_rel()
        text = font.render(f"{mousepos[0],mousepos[1]}", True, (255, 255, 255))
        #text = pygame.transform.rotate(text, 90)
        #draw a black rectangle to clear the screen
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1280, 400))

        screen.blit(text, (0, 0))


        # rotate the screen 90 degrees clockwise

        #screen.blit(pygame.transform.rotate(screen, 90), (0, 650))

        #update the display
        pygame.display.update()

    # wait for 5 seconds
    #pygame.time.wait(5000)

# end the programme
pygame.quit()

# end of programme

