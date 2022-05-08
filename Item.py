import pygame
import os

##################################
pygame.init()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("KKLHY GAME")

# FPS
clock = pygame.time.Clock()
##################################

# 사용자 게임 초기화
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background1.png"))

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character1.png"))
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]         # 캐릭터의 가로 크기
character_height = character_size[1]        # 캐릭터의 세로 크기
character_x_pos = 0        # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로위치)
# 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로위치)
character_y_pos = -80 + screen_height / 2

# 캐릭터 이동 방향 & 속도
character_to_x_LEFT = 0
character_to_x_RIGHT = 0
character_to_y_UP = 0
character_to_y_DOWN = 0
character_speed = 1

# 적 enemy 캐릭터
item = pygame.image.load(os.path.join(image_path, "item.png"))
item_size = item.get_rect().size  # 이미지의 크기를 구해옴
item_width = item_size[0]         # 캐릭터의 가로 크기
item_height = item_size[1]        # 캐릭터의 세로 크기
item_x_pos = 1200 - item_width / 2         # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로위치)
item_y_pos = (screen_height / 2) - (item_height / 2)

item_to_x = 0
item_to_y = 0

# 시작 시간
start_ticks = pygame.time.get_ticks()     # 현재 tick 을 받아옴

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:          # 캐릭터 왼쪽으로
                character_to_x_LEFT -= character_speed
            elif event.key == pygame.K_RIGHT:           # 캐릭터 오른쪽으로
                character_to_x_RIGHT += character_speed
            elif event.key == pygame.K_UP:        # 캐릭터 위쪽으로
                character_to_y_UP -= character_speed
            elif event.key == pygame.K_DOWN:        # 캐릭터 아래로
                character_to_y_DOWN += character_speed

        if pygame.time.get_ticks() > 2000:
            item_to_x -= 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character_to_x_LEFT = 0
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT = 0
            elif event.key == pygame.K_UP:
                character_to_y_UP = 0
            elif event.key == pygame.K_DOWN:
                character_to_y_DOWN = 0

    # 게임 캐릭터 위치 정의
    character_x_pos += character_to_x_LEFT + character_to_x_RIGHT
    character_y_pos += character_to_y_UP + character_to_y_DOWN

    item_x_pos += item_to_x

    # 가로 경계값 처리
    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos <= 0:
        character_y_pos = 0
    elif character_y_pos >= screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))    # 캐릭터 그리기
    screen.blit(item, (item_x_pos, item_y_pos))      # 적 그리기

    pygame.display.update()

pygame.quit()
