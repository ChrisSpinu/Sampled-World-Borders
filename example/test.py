#Imports and Inits
import pygame, json
pygame.init()

#Variables
offsetX = 0
complete = []

#Opening the file
f = open('sampled.json')
data = json.load(f)

#Loading all the points into a list
for i in range(0,len(data)):
    for y in range(0,len(data[i][1])):
        complete.append(data[i][1][y])


#Display init
screen = pygame.display.set_mode([1280, 720])

#Game loop
running = True
while running:
    #Screen clear
    screen.fill((255, 255, 255))

    #Events listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Keys for setting the offset of the map
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                offsetX -= 10
            if event.key == pygame.K_RIGHT:
                offsetX += 10
    
    #Running through all the points and drawing them
    for i in range(0,len(complete)):
        x=complete[i][0] + offsetX
        y=complete[i][1]   
        pygame.draw.circle(screen, (0, 255, 0), (x,y), 2)
        
    pygame.display.flip()

pygame.quit()