import pygame
import random


# 속도 바꾸기
# 충돌처리
# 중복생성

pygame.init()  # 초기화


# 화면 크기 설정
screen_width = 1200  # 가로크기
screen_height = 800  # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("KKLHY")  # 게임 이름

# FPS
clock = pygame.time.Clock()



class obj:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.to_x = 0  # 이동할 좌표
        self.to_y = 0
        self.speed = 0  # 이동 속도

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

    def show(self, k, a, b):
        screen.blit(k, (a, b))  # 배경 그리기


ch = obj()

background = ch.img("0_image/Yang/background.png")  # 배경 이미지 불러오기

# 캐릭터 설정
character = ch.img("0_image/Yang/character.png")  # 캐릭터 이미지 불러오기
character_width, character_height = ch.img_size(character)  # 캐릭터의 가로, 세로 크기 설정
ch.x_pos, ch.y_pos = 0, -80 + screen_height / 2  # 캐릭터 위치 설정
ch.speed = 1  # 이동 속도

# 점수
score = 0

# 아이템 설정
p_it0 = obj()
p_item0 = p_it0.img("아이템/p_it1.png")
p_item0_width, p_item0_height = p_it0.img_size(p_item0) # 아이템의 가로, 세로 크기 설정

# p_item
p_it1 = obj()
p_it2 = obj()
p_it3 = obj()
p_item1 = p_it1.img("아이템/p_it2.png")
p_item1_width, p_item1_height = p_it1.img_size(p_item1)  # 아이템의 가로, 세로 크기 설정
p_it1.x_pos, p_it1.y_pos = 1300, random.randint(0, screen_height - p_item1_height)  # 아이템 위치 설정(random)
p_it1.speed = 5
p_item2 = p_it2.img("아이템/p_it3.png")
p_item2_width, p_item2_height = p_it2.img_size(p_item2)  # 아이템의 가로, 세로 크기 설정
p_it2.x_pos, p_it2.y_pos = 1300, random.randint(0, screen_height - p_item2_height)  # 아이템 위치 설정(random)
p_it2.speed = 5
p_item3 = p_it3.img("아이템/p_it4.png")
p_item3_width, p_item3_height = p_it3.img_size(p_item2)  # 아이템의 가로, 세로 크기 설정
p_it3.x_pos, p_it3.y_pos = 1300, random.randint(0, screen_height - p_item3_height)  # 아이템 위치 설정(random)
p_it3.speed = 5

# N_item
N_it1 = obj()
N_it2 = obj()
N_it3 = obj()
N_item1 = N_it1.img("아이템/n_it1.png")
N_item1_width, N_item1_height = N_it1.img_size(N_item1)  # 아이템의 가로, 세로 크기 설정
N_it1.x_pos, N_it1.y_pos = 1300, random.randint(0, screen_height - N_item1_height)  # 아이템 위치 설정(random)
N_it1.speed = 5
N_item2 = N_it2.img("아이템/n_it2.png")
N_item2_width, N_item2_height = N_it2.img_size(N_item2)  # 아이템의 가로, 세로 크기 설정
N_it2.x_pos, N_it2.y_pos = 1300, random.randint(0, screen_height - N_item2_height)  # 아이템 위치 설정(random)
N_it2.speed = 5
N_item3 = N_it3.img("아이템/n_it3.png")
N_item3_width, N_item3_height = N_it3.img_size(N_item3)  # 아이템의 가로, 세로 크기 설정
N_it3.x_pos, N_it3.y_pos = 1300, random.randint(0, screen_height - N_item3_height)  # 아이템 위치 설정(random)
N_it3.speed = 5


# 아이템 좌표
p_it0.x_pos, p_it0.y_pos = 1300, random.randint(0, screen_height - p_item0_height)  # 아이템 위치 설정(random)
p_it1.x_pos, p_it1.y_pos = 1300, random.randint(0, screen_height - p_item1_height)
p_it2.x_pos, p_it2.y_pos = 1300, random.randint(0, screen_height - p_item2_height)
p_it3.x_pos, p_it3.y_pos = 1300, random.randint(0, screen_height - p_item3_height)
N_it1.x_pos, N_it1.y_pos = 1300, random.randint(0, screen_height - N_item1_height)
N_it2.x_pos, N_it2.y_pos = 1300, random.randint(0, screen_height - N_item2_height)
N_it3.x_pos, N_it3.y_pos = 1300, random.randint(0, screen_height - N_item3_height)

p_it0.speed = 3
p_it1.speed = 5
p_it2.speed = 5
p_it3.speed = 5
N_it1.speed = 5
N_it2.speed = 5
N_it3.speed = 5
items = []
items1 =[]
items2 =[]
items3 =[]
items4 =[]
items5 =[]
items6 =[]
random_time = random.randint(10,150) # 아이템 젠시간 설정
item_time = 0


# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체  생성(폰트,크기)

# 총 시간 (총시간을 이용하면 타이머 생성가능)
total_time = 10

# 시작 시간정보
start_ticks = pygame.time.get_ticks()  # 시작 tick 을 받아옴

# 이벤트 루프
running = True  # 게임이 진행중인가?
started = False  # if 실행 제어조건
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        # 캐릭터 이동 처리
        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                ch.to_x -= ch.speed  # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                ch.to_x += ch.speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                ch.to_y -= ch.speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                ch.to_y += ch.speed
        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ch.to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ch.to_y = 0
    ch.x_pos += ch.to_x * dt
    ch.y_pos += ch.to_y * dt


    # 캐릭터 화면 탈출 방지
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

    # 아이템 이동처리
    p_it0.x_pos -= p_it0.speed
    p_it1.x_pos -= p_it1.speed
    p_it2.x_pos -= p_it2.speed
    p_it3.x_pos -= p_it3.speed
    N_it1.x_pos -= N_it1.speed
    N_it2.x_pos -= N_it2.speed
    N_it3.x_pos -= N_it3.speed
    # 아이템이 화면 밖으로 나갔을경우
    if p_it0.x_pos < 0:
        p_it0.x_pos = 1300
        p_it0.y_pos = random.randint(0, screen_height - p_item0_height)

    # 충돌 처리
    character_rect = ch.rect(character, ch)
    item_rect = p_it0.rect(p_item0, p_it0)

    # 충돌 체크
    if character_rect.colliderect(item_rect):  # colliderect함수는 사각형 부분이 () 안의 값과 충동이 있었는지 체크하는 함수
        print("충돌했다")
        p_it0.x_pos = 1300
        p_it0.y_pos = random.randint(0, screen_height - p_item0_height)
        score += 100

    ch.show(background, 0, 0)  # 배경 그리기
    ch.show(character, ch.x_pos, ch.y_pos)  # 캐릭터 그리기
    p_it0.show(p_item0, p_it0.x_pos, p_it0.y_pos)  # 아이템 그리기
    p_it1.show(p_item1, p_it1.x_pos, p_it1.y_pos)
    p_it2.show(p_item2, p_it2.x_pos, p_it2.y_pos)
    p_it3.show(p_item3, p_it3.x_pos, p_it3.y_pos)
    N_it1.show(N_item1, N_it1.x_pos, N_it1.y_pos)
    N_it2.show(N_item2, N_it2.x_pos, N_it2.y_pos)
    N_it3.show(N_item3, N_it3.x_pos, N_it3.y_pos)

# ---------- 아이템
    item_time += 1

    if item_time == random_time:
        item_time = 0
        items.append([1300, random.randint(0, screen_height - p_item0_height)])

    for i in items:
        i[0] -= 3
        # 충돌처리
        i_rect = p_item0.get_rect()
        i_rect.left = i[0]
        i_rect.top = i[1]

        p_it0.show(p_item0,i[0],i[1])
        if i[0] <= 0:
            items.remove(i)

        if character_rect.colliderect(i_rect):
            score += 100
            items.remove(i)
    # p1
    if item_time == random.randint(10,300):
        item_time = 0
        items1.append([1300, random.randint(0, screen_height - p_item1_height)])

    for j in items1:
        j[0] -= 3
        # 충돌처리
        j_rect = p_item1.get_rect()
        j_rect.left = j[0]
        j_rect.top = j[1]

        p_it1.show(p_item1,j[0],j[1])
        if j[0] <= 0:
            items1.remove(j)

        if character_rect.colliderect(j_rect):
            score += 100
            items1.remove(j)
     # 아이템 p2
    if item_time == random.randint(10,300):
        item_time = 0
        items2.append([1300, random.randint(0, screen_height - p_item2_height)])

    for j in items2:
        j[0] -= 3
        # 충돌처리
        j_rect = p_item2.get_rect()
        j_rect.left = j[0]
        j_rect.top = j[1]

        p_it2.show(p_item2,j[0],j[1])
        if j[0] <= 0:
            items2.remove(j)

        if character_rect.colliderect(j_rect):
            score += 100
            items2.remove(j)

        # p3
        if item_time == random.randint(10,300):
            item_time = 0
            items4.append([1300, random.randint(0, screen_height - N_item1_height)])

        for j in items4:
            j[0] -= 3
            # 충돌처리
            j_rect = N_item1.get_rect()
            j_rect.left = j[0]
            j_rect.top = j[1]

            N_it1.show(N_item1, j[0], j[1])
            if j[0] <= 0:
                items4.remove(j)

            if character_rect.colliderect(j_rect):
                score -= 500
                items4.remove(j)
        # p5
        if item_time == random.randint(10,300):
            item_time = 0
            items5.append([1300, random.randint(0, screen_height - N_item2_height)])

        for j in items5:
            j[0] -= 3
            # 충돌처리
            j_rect = N_item2.get_rect()
            j_rect.left = j[0]
            j_rect.top = j[1]

            N_it2.show(N_item2, j[0], j[1])
            if j[0] <= 0:
                items5.remove(j)

            if character_rect.colliderect(j_rect):
                score -= 100
                items5.remove(j)


 #----------------------------------





    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 시간단위가 ms 라서 1000으로 나누어 s 단위로 표시

    # 출력 할 글자 색상
    timer = game_font.render(str(int(elapsed_time)), True, (255, 0, 0))
    tscore = game_font.render(str(int(score)), True, (255, 0, 0))
    ch.show(timer, 10, 10)
    ch.show(tscore, 1110, 10)



    # 만약 시간이 0 이하이면 게임 종료

    pygame.display.update()  # 게임화면을 다시 그리기!

# 잠시 대기후 게임 종료
pygame.time.delay(2000)

# pygame 종료!
pygame.quit()