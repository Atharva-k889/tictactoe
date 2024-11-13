import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
running = True
count = 0

grid =  [
    ["","",""],
    ["","",""],
    ["","",""],
]

def check_winner():
    
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != "":  
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != "":  
            return grid[0][i]
    

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "":  
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != "": 
        return grid[0][2]
    
    return None  

def display_winner():{
    screen.fill ("white")
}

while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running= False
        screen.fill("white")

        pygame.draw.line(screen,("black"), (200,0),(200,600),width=1)
        pygame.draw.line(screen,("black"), (400,0),(400,600),width=1)
        pygame.draw.line(screen,("black"), (0,200),(600,200),width=1)
        pygame.draw.line(screen,("black"), (0,400),(600,400),width=1)

        for i in range(3):
            for j in range (3):
                
                if j == 0 :     dimx = 100
                elif j == 1 :   dimx = 300
                elif j == 2 :   dimx = 500 
                
                if i == 0 :     dimy = 100
                elif i == 1:    dimy = 300
                elif i == 2:    dimy = 500
                
                if grid[i][j] == 0 :
                    pygame.draw.circle(screen,"black", (dimx,dimy), 50, width=4)
                if grid[i][j] == 1 :
                    pygame.draw.line(screen, "black", (dimx-50,dimy-50), (dimx+50, dimy+50), width=4)
                    pygame.draw.line(screen, "black", (dimx-50,dimy+50), (dimx+50, dimy-50), width=4)


        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            
            if pos[0] < 200 and pos[1] < 200:  
                if grid[0][0] == "":  
                    grid[0][0] = 0 if count % 2 == 0 else 1
                    count += 1

            elif pos[0] < 400 and pos[0] >= 200 and pos[1] < 200:  
                if grid[0][1] == "":  
                    grid[0][1] = 0 if count % 2 == 0 else 1
                    count += 1

            elif pos[0] >= 400 and pos[1] < 200:  #(0, 2)
                if grid[0][2] == "":  
                    grid[0][2] = 0 if count % 2 == 0 else 1
                    count += 1

            elif pos[0] < 200 and pos[1] >= 200 and pos[1] < 400:  #(1, 0)
                if grid[1][0] == "":  
                    grid[1][0] = 0 if count % 2 == 0 else 1
                    count += 1

            elif pos[0] >= 200 and pos[0] < 400 and pos[1] >= 200 and pos[1] < 400:  #(1, 1)
                if grid[1][1] == "":  
                    grid[1][1] = 0 if count % 2 == 0 else 1
                    count += 1

            elif pos[0] >= 400 and pos[1] >= 200 and pos[1] < 400:  #(1, 2)
                if grid[1][2] == "":  
                    grid[1][2] = 0 if count % 2 == 0 else 1
                    count += 1

            elif pos[0] < 200 and pos[1] >= 400:  #(2, 0)
                if grid[2][0] == "":  
                    grid[2][0] = 0 if count % 2 == 0 else 1
                    count += 1

            elif pos[0] >= 200 and pos[0] < 400 and pos[1] >= 400:  #(2, 1)
                if grid[2][1] == "":  
                    grid[2][1] = 0 if count % 2 == 0 else 1
                    count += 1

            elif pos[0] >= 400 and pos[1] >= 400:  #(2, 2)
                if grid[2][2] == "":  
                    grid[2][2] = 0 if count % 2 == 0 else 1
                    count += 1
            
            

        if check_winner() != None :
            display_winner() 
        pygame.display.flip()
       
        clock.tick(60)

pygame.quit()
