import pygame
import random

pygame.init()  # 초기화
# 화면 크기 설정
screen_width = 1200  # 가로크기
screen_height = 800  # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Stage-2")  # 게임 이름

# FPS
clock = pygame.time.Clock()
class obj:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.to_x = 0  # 이동할 좌표
        self.to_y = 0
        self.speed = 0# 이동 속도
        self.items = [] # 리스트 추가
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

    def copy(self,item,name,index_pos,speed):#아이템 복제
        for i in self.items:
            i[index_pos] -= speed
            #충돌처리
            i_rect = name.get_rect()
            i_rect.left = i[0]
            i_rect.top = i[1]
            item.show(name,i[0],i[1])
            if i[0] <= 0:
                item.items.remove(i)
            if character_rect.colliderect(i_rect):
                print("충돌 발생")
                item.items.remove(i)
ch = obj()
background = ch.img("/Users/ho/Git/KKLHY/0_image/Yang/background.png")  # 배경 이미지 불러오기
# 캐릭터 설정
character = ch.img("/Users/ho/Git/KKLHY/0_image/Yang/character.png")  # 캐릭터 이미지 불러오기
character_width, character_height = ch.img_size(character)  # 캐릭터의 가로, 세로 크기 설정
ch.x_pos, ch.y_pos = 0, -80 + screen_height / 2  # 캐릭터 위치 설정
ch.speed = 1  # 이동 속도
# 점수
score = 0

# 아이템 설정
#아이템변수 = obj() 아이템변수 선언
R_it = obj()
UP_it = obj()

#아이템 크기설정
R_item = R_it.img("/Users/ho/Git/KKLHY/1_image/F.png")
UP_item = UP_it.img("/Users/ho/Git/KKLHY/1_image/F.png")
R_item_width, R_item_height = R_it.img_size(R_item) # 아이템의 가로, 세로 크기 설정
UP_item_width, UP_item_height = UP_it.img_size(UP_item)

# 중복으로 만들 필요없어서 삭제

random_time = random.randint(10,50) # 아이템 젠시간 설정
item_time = 0
# 장애물 생성 조건변수
elapsed_t = 0

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체  생성(폰트,크기)

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
    R_it.x_pos -= R_it.speed
    UP_it.y_pos += UP_it.speed
    # 아이템이 화면 밖으로 나갔을경우
    if R_it.x_pos < 0:
        R_it.x_pos = 1300
        R_it.y_pos = random.randint(0, screen_height - R_item_height)
    if UP_it.y_pos > 800:
        UP_it.y_pos = 0
        UP_it.x_pos = random.randint(0,screen_width - UP_item_width) #R width 수정하기

    # 충돌 처리
    character_rect = ch.rect(character, ch)
    item_rect = R_it.rect(R_item, R_it)

    # 충돌 체크
    if character_rect.colliderect(item_rect):  # colliderect함수는 사각형 부분이 () 안의 값과 충동이 있었는지 체크하는 함수
        print("충돌했다")
        R_it.x_pos = 1300
        R_it.y_pos = random.randint(0, screen_height - R_item_height)
        score += 100

    ch.show(background, 0, 0)  # 배경 그리기
    ch.show(character, ch.x_pos, ch.y_pos)  # 캐릭터 그리기
    R_it.show(R_item, R_it.x_pos, R_it.y_pos)  # 아이템 그리기
    UP_it.show(UP_item, UP_it.x_pos, UP_it.y_pos)


# ---------- 아이템
    item_time += 1
    elapsed_t += 1

    if item_time == random_time:
        item_time = 0
        if  elapsed_t < 300 or 600 < elapsed_t:
            R_it.items.append([1300, random.randint(0, screen_height - R_item_height)])
        if elapsed_t >= 300:
            UP_it.items.append([random.randint(0, screen_width - R_item_width), 0])
        #if elapsed_t >= 600: 왼쪽에서 오른쪽
            #

    #copy 아이템 그리기
    #item.copy(변수명,변수,x또는y,방향)

    R_it.copy(R_it,R_item,0,3)
    UP_it.copy(UP_it,UP_item,1,-3)

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