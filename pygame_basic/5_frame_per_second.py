import pygame

pygame.init() # 초기화 반드시 필요

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Song Game")

# FPS
clock = pygame.time.Clock()

background = pygame.image.load("D:/song/python/Workspace/Python_game_1/pygame_basic/background.png")

character = pygame.image.load("D:/song/python/Workspace/Python_game_1/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

#캐릭터 속도
character_speed = 0.6

running = True
while running:
    dt = clock.tick(60) #프레임 수 조절


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아랫쪽으로
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt #프레임으로 보정
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update()

pygame.quit