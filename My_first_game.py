import random
import time
import pygame
pygame.init()
width = 1200
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino Jumping Game")
player=pygame.image.load("dino.png") 
rect=player.get_rect()
bg_img = pygame.image.load("background.jpg")
obstacles= [340,650,980,1300]
obst_img1 = pygame.image.load("cactus.png")
obst_img2 = pygame.image.load("cactus2.png")
obstacles_speed = 300
game_over_img = pygame.image.load("game_over.png")
player_height = 120
player_width = 85
x = 50
y = (height-player_height)
move_x = 0
move_y = 0
v = 10
m = 1.5
v1 = v
m1 = m
score = 0
highest_score = 0
isjump = False
active = False
font = pygame.font.Font('freesansbold.ttf', 30)
font2 = pygame.font.Font('freesansbold.ttf', 25)
enter = False
game_over = False
running=True
prev_time = time.time()
speed_increment = 50
next_triger = speed_increment
game_over_stop = False

while running:
    
    now = time.time()
    dt = now - prev_time
    prev_time = now
    
    screen.fill((255,255,255))
    screen.blit(bg_img,(0,0))
    screen.blit(player, (x,y))
    score_text = font.render(f'Score: {score}', True, (0,0,0))
    screen.blit(score_text, (535,50))
    highest_score_text = font.render(f'Highest Score: {highest_score}', True, (0,0,0))
    screen.blit(highest_score_text, (485,10))
    start_text = font.render("Prees Space To Start", True, (0,0,0))
    jump_text = font.render("Prees Space To Jump", True, (0,0,0))
    pause_text = font2.render("Press Enter To Pause", True, (0,0,0))
    play_text = font.render("Press Enter To Play", True, (0,0,0))
    restart_text = font.render("Press Space To Restart", True, (0,0,0))
    
    obstacle1 = screen.blit(obst_img1, (obstacles[0],600))
    obstacle2 = screen.blit(obst_img2, (obstacles[1],585))
    obstacle3 = screen.blit(obst_img1, (obstacles[2],600))
    obstacle4 = screen.blit(obst_img2, (obstacles[3],585))
    
    for event in pygame.event.get():
      
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE :
                isjump = True
        
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                active = True
                enter = False
                game_over = False
                game_over_stop = True
                obstacles= [340,650,980,1300]
                x = 50
                y = height-player_height
                score = 0
                # obstacles_speed = 300
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER and active:
                active = False
                enter =True
            elif event.key == pygame.K_KP_ENTER and not active and not game_over:  
                active = True
                enter =False
            if event.key == pygame.K_RETURN and active:
                active = False
                enter =True
            elif event.key == pygame.K_RETURN and not active and not game_over:  
                active = True
                enter =False
        
        elif event.type == pygame.QUIT:
            running = False

    if active:
        screen.blit(pause_text,(10,10))
    elif not active and not enter and  not game_over:
        screen.blit(start_text,(455,300))
        screen.blit(jump_text,(451,350))
    if enter:
        screen.blit(play_text,(450,300))
        screen.blit(restart_text,(420,350))
        
    if isjump:
        F = (1/2)*m*(v**2)
        y-= F
        v -=1
        if v<0:
            m = -m1
        if v == -(v1 + 1):
            isjump = False
            v = v1
            m = m1
        
    for i in range(len(obstacles)):
        if active:
            obstacles[i] -= obstacles_speed * dt
        if obstacles[i] < -10:
            obstacles[i] = random.randint(1310,1320)
            score += 1
    if rect.colliderect(obstacle1) or rect.colliderect(obstacle2) or rect.colliderect(obstacle3) or rect.colliderect(obstacle4):
        move_x = 0
        move_y = 0
        active = False
        game_over = True
    
    if game_over_stop:
        game_over = False
        game_over_stop = False
    
    if game_over :
        screen.blit(game_over_img,(350,230))
    
    rect.x = x
    rect.y = y
    x += move_x
    y += move_y
    if  x<= 0:
        x = 0
    elif x >= (width - player_width):
        x= (width - player_width)
    if  y<= 0:
        y = 0
    elif y >= (height - player_height):
        y= (height - player_height)
    
    if highest_score < score :
        highest_score += 1
    
    if speed_increment == score:
        obstacles_speed += 50
        speed_increment += next_triger
    pygame.time.delay(30)
    pygame.display.update()
pygame.quit()
