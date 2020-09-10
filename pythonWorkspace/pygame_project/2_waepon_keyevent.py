import pygame
import os

pygame.init() #초기화(반드시 필요)

#화면 크기설정
screen_width = 640  #가로크기
screen_height = 480 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Pang") #게임 이름

#FPS
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") #이미지 폴더 위치 반환

#배경이미지 불러오기

background = pygame.image.load(os.path.join(image_path,"background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_height = character_size[1]
character_width = character_size[0]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height - stage_height

#캐릭터 이동 방향
character_to_x = 0

#캐릭터 이동 속도
character_speed = 5

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한 번에 여러 발 발사 가능
weapons =[]

#무기 이동속도
weapon_speed = 10

#이벤트 루프
running = True  #게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임수 설정

    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: #무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        
    #게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0

    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #무기 위치조정
    #500,200 -> 
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 이로 올리는 것

    #천정에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    #화면 그리기
    screen.blit(background, (0, 0))  #배경 그리기
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

     
    pygame.display.update() #게임화면을 다시 그리기! 반드시 해줘야 됨


# pygame 종료
pygame.quit()