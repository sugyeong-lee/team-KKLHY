import pygame
import random
# 중복 아이템 생성

pygame.init() #초기화
# 화면 크기 설정
screen_width = 1200 # 가로크기
screen_height = 800 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#이동할 좌표
to_x = 0
to_y = 0

#아이템 정보 변수
item_to_x= 0
item_time = 0
items = [] # 중복 생성을 위한 리스트
random_time = random.randrange(10,20) # 아이템 생성속도

# 점수
score = 0
#이동 속도
character_speed = 1

# 화면 타이틀 설정
pygame.display.set_caption("KKLHY") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("0_image/HO/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("0_image/HO/character.png") # 121 / 113
character_size = character.get_rect().size # 캐릭터 가로,세로 크기 불러오기
character_width =character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = 0 # 화면 가로의 캐릭터 위치설정
character_y_pos = -80 + screen_height/2  # 화면 세로의 캐릭터 위치 설정

# 아이템 추가
item = pygame.image.load("0_image/HO/item.png")# 중복 생성을 위한 리스트화
item_size = character.get_rect().size # 캐릭터 가로,세로 크기 불러오기
item_width =character_size[0] # 캐릭터의 가로 크기
item_height = character_size[1] # 캐릭터의 세로 크기
item_x_pos = 1300 # random
item_y_pos = random.randint(0,screen_height -item_height) # random
item_speed = 10

#폰트 정의
game_font =pygame.font.Font(None, 40) # 폰트 객체  생성(폰트,크기)

# 총 시간 (총시간을 이용하면 타이머 생성가능)
total_time = 10

# 시작 시간정보
start_ticks = pygame.time.get_ticks() # 시작 tick 을 받아옴

# 이벤트 루프
running = True # 게임이 진행중인가?
started = False # if 실행 제어조건
while running:
  dt =clock.tick(60) # 게임화면의 초당 프레임 수를 설정


  for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
    if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
      running = False # 게임이 진행중이 아님

    if event.type == pygame.KEYDOWN:# 키가 눌러졌는지 확인
      if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
        to_x -= character_speed # to_x = to_x - 5
      elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
        to_x += character_speed
      elif event.key == pygame.K_UP: #캐릭터를 위로
        to_y -= character_speed
      elif event.key == pygame.K_DOWN: #캐릭터를 아래로
        to_y += character_speed



    if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0

# 캐릭터 , 아이템 이동속도 계산
  character_x_pos += to_x * dt
  character_y_pos += to_y * dt

  #캐릭터 화면 탈출 방지
  #가로 경계값 처리
  if character_x_pos <= 0: # = 추가
    character_x_pos = 0
  elif character_x_pos >= screen_width - character_width:
    character_x_pos =screen_width - character_width


  #세로 경계값처리
  if character_y_pos <= 0:
    character_y_pos = 0
  elif character_y_pos >= screen_height -character_height:
    character_y_pos = screen_height - character_height

  #아이템 이동처리
  item_x_pos -= item_speed

  #아이템이 화면 밖으로 나갔을경우
  if item_x_pos < 0:
      item_x_pos = 1300
      item_y_pos = random.randint(0,screen_height-item_height)



 # 충돌 처리
  character_rect = character.get_rect()
  character_rect.left = character_x_pos #캐릭터의 x축 정보
  character_rect.top = character_y_pos # 캐릭터의 y축 정보

  item_rect = item.get_rect()
  item_rect.left = item_x_pos
  item_rect.top = item_y_pos

 # 충돌 체크
  if character_rect.colliderect(item_rect): # colliderect함수는 사각형 부분이 () 안의 값과 충동이 있었는지 체크하는 함수
      print("충돌했다")
      item_x_pos = 1300
      item_y_pos = random.randint(0, screen_height - item_height)
      score += 100
  # 화면에 그리기
  screen.blit(background,(0,0)) #배경 그리기
  screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기
  screen.blit(item,(item_x_pos,item_y_pos))  # 아이템 그리기

  item_time += 1
  if item_time == random_time:
    item_time = 0
    items.append([1300,random.randint(0,screen_height-item_height)])

  for i in items:
    i[0] -= item_speed
    # 충동처리
    i_rect = item.get_rect()
    i_rect.left = i[0]
    i_rect.top = i[1]

    screen.blit(item,(i[0],i[1]))
    if i[0] <= 0:
      items.remove(i)

    if character_rect.colliderect(i_rect):
      score += 100
      items.remove(i)



  # 타이머 집어 넣기
  # 경과 시간 계산
  elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
  # 시간단위가 ms 라서 1000으로 나누어 s 단위로 표시

  # 출력 할 글자 색상
  timer = game_font.render(str(int(elapsed_time)), True, (255,0,0))
  tscore = game_font.render(str(int(score)),True,(255,0,0))
  screen.blit(timer, (10, 10))
  screen.blit(tscore,(1110,10)) # 스코어 정보

# 만약 시간이 0 이하이면 게임 종료


  pygame.display.update() # 게임화면을 다시 그리기!

# 잠시 대기후 게임 종료
pygame.time.delay(2000)

# pygame 종료!
pygame.quit()