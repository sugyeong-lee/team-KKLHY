import pygame
import os
import random
###############################################
# 기본 초기화
pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 1200  # 가로크기
screen_height = 800  # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Open Source")  # 게임 이름

# FPS
clock = pygame.time.Clock()
##############################################


# 1. 사용자 게임 초기화 ( 배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "image")  # images 폴더 위치 반환

# 배경
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = character_width
character_y_pos = (screen_height / 2) - (character_height / 2)

teacher = pygame.image.load(os.path.join(image_path, "teacher.png"))
teacher_size = teacher.get_rect().size
teacher_width = teacher_size[0]
teacher_height = teacher_size[1]
teacher_x_pos = screen_width - teacher_width
teacher_y_pos = (screen_height / 2) - (teacher_height / 2)


# 캐릭터 이동 방향
character_to_x = 0
character_to_y = 0

# 캐릭터 이동 속도
character_speed = 10

# teacher 움직이기
to_y_teacher = 0
random_teacher = random.randrange(0, screen_height - teacher_height)

running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_UP:
                character_to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                character_to_y += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                character_to_y = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    character_y_pos += character_to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_y_pos < 0:
        character_y_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

# 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    if random_teacher > teacher_y_pos:
        teacher_y_pos += 10
    elif random_teacher < teacher_y_pos:
        teacher_y_pos -= 10
    else:
        random_teacher = random.randrange(0, screen_height - teacher_height)

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(teacher, (teacher_x_pos, teacher_y_pos))

    pygame.display.update()

# pygame 종료
pygame.quit()
