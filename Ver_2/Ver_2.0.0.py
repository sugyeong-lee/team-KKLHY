import pygame
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

class obj:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.to_x = 0  # 이동할 좌표
        self.to_y = 0
        self.speed = 0  # 이동 속도
    #수정
    def img(self, address):  # 이미지 함수
        return pygame.image.load(address)  # 이미지 불러오기

    def img_size(self, k):  # 이미지 크기
        k_size = k.get_rect().size  # 캐릭터 가로, 세로 크기 불러오기
        k_width = k_size[0]  # 가로 크기
        k_height = k_size[1]  # 세로 크기
        return k_width, k_height

    def rect(self, a, b):
        rect = a.get_rect()
        rect.left = b.x_pos  # 캐릭터의 x축 정보
        rect.top = b.y_pos   # 캐릭터의 y축 정보
        return rect

    def item_list(self, p):
        item = []
        item.append(p)

    def show(self, k, a, b):
        screen.blit(k, (a, b))  # 배경 그리기


ch = obj()

background = ch.img(
    "배경/background.png")  # 배경 이미지 불러오기

# 캐릭터 설정
character = ch.img(
    "0_image/Yang/character.png")  # 캐릭터 이미지 불러오기
character_width, character_height = ch.img_size(character)  # 캐릭터의 가로, 세로 크기 설정
ch.x_pos, ch.y_pos = 0, -80 + screen_height / 2  # 캐릭터 위치 설정
ch.speed = 1  # 이동 속도

wp = obj()
weapon = wp.img("0_image/Yang/weapon.png")
weapon_width, weapon_height = wp.img_size(weapon)  # 아이템의 가로, 세로 크기 설정
wp.speed = 5

teach = obj()
teacher = ch.img("0_image/Yang/teacher.png")
teacher_width, teacher_height = ch.img_size(teacher)
teach.x_pos, teach.y_pos = screen_width - \
    teacher_width, (screen_height / 2) - (teacher_height / 2)

it = obj()
ball = it.img("0_image/Yang/ball.png")
ball_width, ball_height = it.img_size(ball)
it.speed = 3

items = []
item_time = 0
random_time = random.randint(10, 100)

weapons = []

random_y_teacher = random.randrange(0, screen_height - teacher_height, 5)
random_x_teacher = random.randrange(screen_width/2, screen_width - teacher_width, 5)


font_hp = pygame.font.SysFont(None, 30)
font_gameover = pygame.font.SysFont(None, 100)

gameover = False
character_current_hp = 400
teacher_current_hp = 400
hp_bar = 400


running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                ch.to_x -= ch.speed
            elif event.key == pygame.K_RIGHT:
                ch.to_x += ch.speed
            elif event.key == pygame.K_UP:
                ch.to_y -= ch.speed
            elif event.key == pygame.K_DOWN:
                ch.to_y += ch.speed
            elif event.key == pygame.K_SPACE:
                wp.x_pos = ch.x_pos + weapon_width / 2
                wp.y_pos = ch.y_pos
                weapons.append([wp.x_pos, wp.y_pos])

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ch.to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ch.to_y = 0

    # 3. 게임 캐릭터 위치 정의
    ch.x_pos += ch.to_x * dt
    ch.y_pos += ch.to_y * dt
    it.x_pos += it.to_x

    w = screen_width - character_width
    h = screen_height - character_height
    # 가로 경계값 처리
    if ch.x_pos <= 0:  # = 추가
        ch.x_pos = 0
    elif ch.x_pos >= w:
        ch.x_pos = w
    # 세로 경계값처리
    if ch.y_pos <= 0:
        ch.y_pos = 0
    elif ch.y_pos >= h:
        ch.y_pos = h

# 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리
    # 충돌 처리
    character_rect = ch.rect(character, ch)
    item_rect = it.rect(ball, it)
    weapon_rect = wp.rect(weapon, wp)
    teacher_rect = teach.rect(teacher, teach)

    # 충돌 체크
    if character_rect.colliderect(item_rect):
        it.x_pos = 1300
        it.y_pos = random.randint(0, screen_height - ball_height)

    if weapon_rect.colliderect(teacher_rect):
        wp.x_pos = 1300
        it.y_pos = random.randint(0, screen_height - weapon_height)

    # 5. 화면에 그리기
    if random_y_teacher > teach.y_pos:
        teach.y_pos += 5
    elif random_y_teacher < teach.y_pos:
        teach.y_pos -= 5
    else:
        random_y_teacher = random.randrange(0, screen_height - teacher_height, 5)

    if random_x_teacher < teach.x_pos:
        teach.x_pos -= 5
    elif random_x_teacher > teach.x_pos:
        teach.x_pos += 5
    else:
        random_x_teacher = random.randrange(screen_width/2, screen_width - teacher_width, 5)

    ch.show(background, 0, 0)  # 배경 그리기
    ch.show(character, ch.x_pos, ch.y_pos)  # 캐릭터 그리기
    teach.show(teacher, teach.x_pos, teach.y_pos)
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, character_current_hp, 25))
    pygame.draw.rect(screen, (255, 255, 255), (10, 10, hp_bar, 25), 4)
    pygame.draw.rect(screen, (255, 0, 0), (780, 10, teacher_current_hp, 25))
    pygame.draw.rect(screen, (255, 255, 255), (780, 10, hp_bar, 25), 4)

    item_time += 1
    if item_time == random_time:
        item_time = 0
        items.append([teach.x_pos, teach.y_pos + ball_height])

    for i in items:
        i[0] -= it.speed
        i_rect = ball.get_rect()
        i_rect.left = i[0]
        i_rect.top = i[1]

        it.show(ball, i[0], i[1])
        if i[0] <= 0:
            items.remove(i)

        if character_rect.colliderect(i_rect):
            items.remove(i)
            character_current_hp -= 40
            if character_current_hp < 0:
                gameover = "YOU LOSE"

    for i in weapons:
        i[0] += wp.speed
        i2_rect = weapon.get_rect()
        i2_rect.left = i[0]
        i2_rect.top = i[1]

        wp.show(weapon, i[0], i[1])
        if i[0] > 1200:
            weapons.remove(i)

        if teacher_rect.colliderect(i2_rect):
            weapons.remove(i)
            teacher_current_hp -= 40
            if teacher_current_hp < 0:
                gameover = "YOU WIN"

    if gameover:
        text_gameover = font_gameover.render(gameover, True, (255, 0, 0))

        size_text_width = text_gameover.get_rect().size[0]
        size_text_height = text_gameover.get_rect().size[1]

        x_pos_text = screen_width/2 - size_text_width/2
        y_pos_text = screen_height/2 - size_text_height/2

        screen.blit(text_gameover, (x_pos_text, y_pos_text))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    pygame.display.update()

# pygame 종료
pygame.quit()
