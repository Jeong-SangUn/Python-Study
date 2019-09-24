import pygame
import sys
import copy
import stage
import time


size=(600,480)
pygame.init()
pygame.display.set_caption("BoxMoveGame")
Window = pygame.display.set_mode(size)

ImageMan = pygame.image.load('./img/Man.png')
ImageManLeft = pygame.image.load('./img/ManLeft.png')
ImageManRight = pygame.image.load('./img/ManRight.png')
ImageManPushLeft = pygame.image.load('./img/ManPushLeft.png')
ImageManPushRight = pygame.image.load('./img/ManPushRight.png')
ImageManPushDown = pygame.image.load('./img/ManPushDown.png')
ImageManPushUp = pygame.image.load('./img/ManPushUp.png')
ImageStreet = pygame.image.load('./img/street.png')
ImageWall = pygame.image.load('./img/wall.png')
ImageBox = pygame.image.load('./img/box.png')
ImagePotal = pygame.image.load('./img/potal.png')

Image = ImageMan
HumanX = 0
HumanY = 0
Stage = 0
text_start = 'Game Start'
text_clear = 'Game Clear'
text_use = 'Replay : r'
# 3,3 3,6
# 4,3 4,6
StageMap = stage.map()
Map = copy.deepcopy(StageMap[Stage])

font = pygame.font.Font(None, 36)


def text_mid(text_message):
    text = font.render(text_message, True, (255,255,255)) #(255,255,255) color: White
    text_rect = text.get_rect()
    textX = Window.get_width() / 2 - text_rect.width / 2
    textY = Window.get_height() / 2 - text_rect.height / 2
    Window.blit(text, (textX, textY))
    pygame.display.update()
    time.sleep(1)

def text_content(text_message):
    text = font.render(text_message, True, (255,255,255)) #(255,255,255) color: White
    Window.blit(text, (0, 0))
    pygame.display.update()

count = 0
text_mid(text_start)
while True:
    text_stage = str(Stage+1) + ' Stage'
    
    EndGame = True
    for gx in range(len(Map[0])):
        for gy in range(len(Map)):
            if ' ' == Map[gy][gx]:
                Window.blit(ImageStreet,(gx*60,gy*60))
            elif '.' == Map[gy][gx]:
                Window.blit(ImagePotal,(gx*60,gy*60))
            elif '#' == Map[gy][gx]:
                if Stage == count:
                    Window.blit(ImageWall,(gx*60,gy*60))
                    if (gy,gx) == (0,0) or (gy,gx) == (0,1):  #(0,0)/(0,1)위치에 스테이지 시작 시 한번만 글과 맵을 출력하기 위함
                        text_content(text_use)
                else:
                    if (gy,gx) == (0,0) or (gy,gx) == (0,1):
                        continue
                    Window.blit(ImageWall,(gx*60,gy*60))
            elif '@' == Map[gy][gx]:
                HumanX = gx
                HumanY = gy
                Window.blit(Image ,(gx*60,gy*60))
            elif 'B' == Map[gy][gx]:
                if '.' != StageMap[Stage][gy][gx]:
                    EndGame = False
                Window.blit(ImageBox,(gx*60,gy*60))
    pygame.display.update()

    if Stage == count:
        text_mid(text_stage)
        count = count +1

    if EndGame == True:
        Stage = Stage + 1
        Image = ImageMan
        if Stage > len(StageMap) - 1 :
            text_mid(text_clear)
            pygame.quit()
            sys.exit()
        else:
            Map = copy.deepcopy(StageMap[Stage])

      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN : 
            tempX = HumanX
            tempY = HumanY
            if event.key == pygame.K_UP :
                Image = ImageMan
                tempY = tempY - 1
            elif event.key == pygame.K_DOWN :
                Image = ImageMan
                tempY = tempY + 1
            elif event.key == pygame.K_RIGHT :
                Image = ImageManRight
                tempX = tempX + 1
            elif event.key == pygame.K_LEFT :
                Image = ImageManLeft
                tempX = tempX - 1
            elif event.key == pygame.K_r :
                Image = ImageMan
                Map = copy.deepcopy(StageMap[Stage])
                count = count -1
                continue
            else:
                continue
            
            if Map[tempY][tempX] == '#':
                continue
            elif Map[tempY][tempX] == 'B':
                if Map[2*tempY-HumanY][2*tempX-HumanX] == '#':
                    continue
                elif Map[2*tempY-HumanY][2*tempX-HumanX] == 'B':
                    continue
                if tempX-HumanX > 0:
                    Image = ImageManPushRight 
                elif tempX-HumanX < 0:
                    Image = ImageManPushLeft
                elif tempY-HumanY > 0:
                    Image = ImageManPushDown
                elif tempY-HumanY < 0:
                    Image = ImageManPushUp
                Map[2*tempY-HumanY][2*tempX-HumanX] = 'B'

            if StageMap[Stage][HumanY][HumanX] != '.':
                Map[HumanY][HumanX] = ' '
            else:
                Map[HumanY][HumanX] = '.'
            HumanX = tempX
            HumanY = tempY
            Map[HumanY][HumanX]='@'