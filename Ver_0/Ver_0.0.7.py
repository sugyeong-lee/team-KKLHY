# 캐릭터에 필요한 설정: 

# 아이템에 : , 스피드+이동방향, 랜덤 생성좌표(로직),아이템을 담을 리스트(로직),아이템 젠시간(로직)

# 공통적인 x_pos y_pos, 충돌처리 (로작),높이너비(변수),경로받기(로직),그리기(로직),크기,
import pygame
import random

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
    def __init__(self, address):
        self.x_pos=0;self.y_pos=0
        self.to_x = 0 ;self.to_y = 0
        self.speed = 1
        self.image = pygame.image.load(address)
        
        
    def rect(self):
        rect = self.image.get_rect()
        rect.left = self.x_pos  # 캐릭터의 x축 정보
        rect.top = self.y_pos   # 캐릭터의 y축 정보
        return rect
    
    def show(self):
        screen.blit(self.image,(self.x_pos,self.y_pos))
    
class item(obj):# obj 를 상속 받는 아이템클래스
    def __init__(self, address):
        super().__init__(address)
        self.speed = 1
        # x =1300 ,y = 랜덤으로초기화 함수
    def setRandomXY_pos(self):
        self.x_pos = 1100
        self.y_pos = random.randint(0, screen_height - self.rect().size[1])
    def shiftLeft(self):
        while self.x_pos < 300:
            self.x_pos -= self.speed
background = pygame.image.load("배경/background.png")  # 배경 이미지 불러오기
gameover = pygame.image.load("배경/Gameover.png")
# 캐릭터 객체 생성
ch = obj("캐릭터/Step_0,2,4.png")
# 캐릭터 위치 초기화
ch.x_pos = 0 ; ch.y_pos = -80 + screen_height / 2
ch.speed = 1  # 이동 속도
# 점수
score = 0

# 아이템 설정, 리스트로 초기화
p_it = [
    item("아이템/n_it1.png"),
    item("아이템/p_it2.png"),
    item("아이템/p_it3.png"),
    item("아이템/p_it4.png")
]
n_it =[
    item("아이템/n_it1.png"),
    item("아이템/n_it2.png"),
    item("아이템/n_it3.png")
]
# 아이템객체 위치 초기화
for i in range(4):
    p_it[i].setRandomXY_pos()
    
for i in range(3):
    n_it[i].setRandomXY_pos()

random_time = random.randint(10,150) # 아이템 젠시간 설정
item_time = 0

n_items = [];p_items = []

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
    w = screen_width - ch.rect().size[0]    #self.rect().size[0] 가 캐릭터의 가로크기
    h = screen_height - ch.rect().size[1]   #self.rect().size[1] 가 캐릭터의 세로크기
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
        
    # 배경 그리기
    screen.blit(background,(0,0))
    # 캐릭터 그리기
    ch.show()

# ---------- 아이템

    if random.randint(0, 30) == 0:
        p_itemIndex = random.randint(0, 3)
        p_items.append(p_it[p_itemIndex])           # 1300, random.randint(0, screen_height - p_it[itemIndex].rect().size[1])])

    if random.randint(0, 30) == 0:
        n_itemIndex = random.randint(0, 2)
        n_items.append(n_it[n_itemIndex])           # 1300, random.randint(0, screen_height - n_it[itemIndex].rect().size[1])])

    # print("추가된 아이템 길이",len(p_items) ,"/n")
    for i in p_items: #[item]
        i.setRandomXY_pos()
        i.show()
        print( i.x_pos,i.speed ,"\n")
        i.x_pos=i.x_pos-i.speed
            
        # i.show()
        # 
        # if i.x_pos<=0:
        #   p_items.remove(i)

        if ch.rect().colliderect(i.rect()):
            score += 100
            p_items.remove(i)
            
    for i in n_items: #[item]
        i.setRandomXY_pos()
        i.show()
    #     i.shiftLeft()

        if i.x_pos <= 0:
            n_items.remove(i)

        if ch.rect().colliderect(i.rect()):
            score -= 100
            n_items.remove(i)

        
#----------------------------------

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 시간단위가 ms 라서 1000으로 나누어 s 단위로 표시
    if score < 0 or elapsed_time > 60:
        screen.blit(gameover,(0,0))
        
    # Time 출력 할 글자, 색상
    timer = game_font.render("Time: "+str(int(elapsed_time)), True, (0, 0, 0))
    screen.blit(timer,(10,10))
    # score 출력 할 글자, 색상
    tscore = game_font.render("Score: "+str(int(score)), True, (0, 0, 0))
    screen.blit(tscore, (1010, 10))

    # 만약 시간이 0 이하이면 게임 종료
    
# 게임화면을 다시 그리기!
    pygame.display.update()  
# 잠시 대기후 게임 종료
pygame.time.delay(1000)
# pygame 종료!
pygame.quit()