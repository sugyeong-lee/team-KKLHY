import pygame

pygame.init() #초기화ㅓ
# 화면 크기 설정
screen_width = 1200 # 가로크기
screen_height = 800 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("KKLHY") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("/Users/ho/Git/KKLHY/image/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/ho/Git/KKLHY/image/character.png")
character_size = character.get_rect().size # 캐릭터 가로,세로 크기 불러오기
character_width =character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width / 10 - character_width/2 # 화면 가로의 캐릭터 위치설정
character_y_pos = screen_height - character_height # 화면 세로의 캐릭터 위치 설정


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
  for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
    if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
      running = False # 게임이 진행중이 아님


  screen.blit(background,(0,0)) #배경 그리기

  screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기

  pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료!
pygame.quit()