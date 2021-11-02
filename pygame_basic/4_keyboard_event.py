import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Song Game")

background = pygame.image.load("D:/song/python/Workspace/Python_game_1/pygame_basic/background.png")

character = pygame.image.load("D:/song/python/Workspace/Python_game_1/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= 5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += 5
            elif event.key == pygame.K_UP: # 캐릭터를 위쪽으로
                to_y -= 5
            elif event.key == pygame.K_DOWN: # 캐릭터를 아랫쪽으로
                to_y += 5
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤 
            if event.type == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                to_x = 0
            if event.type == pygame.K_UP or event.type == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos -= to_y

    screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update()

pygame.quit