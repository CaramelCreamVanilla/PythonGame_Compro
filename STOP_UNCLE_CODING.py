import time 

print('name :')
name = input()
print('game start in...')
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)


import pygame,random
from pygame import mixer
from csv import *

pygame.init()
pygame.display.set_caption('ลักพาตัวนักการเมือง')
screen = pygame.display.set_mode((550,700))

mixer.music.load('BG_song.mp3')
pygame.mixer.music.set_volume(.1)
mixer.music.play()

clock = pygame.time.Clock()
counter  = 30 
time_count = '30'
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.Font('alagard.ttf',25)

bg = pygame.image.load(r'sky.jpg')

i_drop = 0
i = [pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงไม่รู้.png'),
     pygame.image.load(r'ลุงพล.png'),
     pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงไม่รู้.png'),
     pygame.image.load(r'ลุงไม่รู้.png'),
     pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงไม่รู้.png'),
     pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงพล.png'),
     pygame.image.load(r'ลุงไม่รู้.png'),
     pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงพล.png'),
     pygame.image.load(r'ลุงไม่รู้.png'),
     pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงไม่รู้.png'),
     pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงพล.png'),
     pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงไม่รู้.png'),
     pygame.image.load(r'ลุงตู่.png'),
     pygame.image.load(r'ลุงพล.png'),]

i_x = random.randrange(20,500) ; i_show = 1
i_y = random.randrange(-700,0)
i_x2 = random.randrange(20,500) ; i_show2 = 1
i_y2 = random.randrange(-1000,-700)
i_x3 = random.randrange(20,500) ; i_show3 = 1
i_y3 = random.randrange(-1300,-1000) 
i_x4 = random.randrange(20,500) ; i_show4 = 1
i_y4 = random.randrange(-1600,-1300) 
i_x5 = random.randrange(20,500) ; i_show5 = 1
i_y5 = random.randrange(-1900,-1600) 
i_x6 = random.randrange(20,500) ; i_show6 = 1
i_y6 = random.randrange(-2100,-1900) 
i_x7 = random.randrange(20,500) ; i_show7 = 1
i_y7 = random.randrange(-2400,-2100) 
i_x8 = random.randrange(20,500) ; i_show8 = 1
i_y8 = random.randrange(-2700,-2400) 
i_x9 = random.randrange(20,500) ; i_show9 = 1
i_y9 = random.randrange(-3000,-2700) 
i_x10 = random.randrange(20,500) ; i_show10 = 1
i_y10 = random.randrange(-3300,-3000) 
i_x11 = random.randrange(20,500) ; i_show11 = 1
i_y11 = random.randrange(-3600,-3300) 
i_x12 = random.randrange(20,500) ; i_show12 = 1
i_y12 = random.randrange(-3900,-3600) 
i_x13 = random.randrange(20,500) ; i_show13 = 1
i_y13 = random.randrange(-4500,-4200) 
i_x14 = random.randrange(20,500) ; i_show14 = 1
i_y14 = random.randrange(-4700,-4500) 
i_x15 = random.randrange(20,500) ; i_show15 = 1
i_y15 = random.randrange(-5000,-4700) 
i_x16 = random.randrange(20,500) ; i_show16 = 1
i_y16 = random.randrange(-5300,-5000)
i_x17 = random.randrange(20,500) ; i_show17 = 1
i_y17 = random.randrange(-5600,-5300) 
i_x18 = random.randrange(20,500) ; i_show18 = 1
i_y18 = random.randrange(-5900,-5600) 
i_x19 = random.randrange(20,500) ; i_show19 = 1
i_y19 = random.randrange(-6100,-5900)
i_x20 = random.randrange(20,500) ; i_show20 = 1
i_y20 = random.randrange(-6400,-6100)
i_x21 = random.randrange(20,500) ; i_show21 = 1
i_y21 = random.randrange(-6700,-6400) 
i_x22 = random.randrange(20,500) ; i_show22 = 1
i_y22 = random.randrange(-7000,-6700)
i_x23 = random.randrange(20,500) ; i_show23 = 1
i_y23 = random.randrange(-7300,-7000) 
i_x24 = random.randrange(20,500) ; i_show24 = 1
i_y24 = random.randrange(-7600,-7300) 
i_x25 = random.randrange(20,500) ; i_show25 = 1
i_y25 = random.randrange(-7900,-7600)

t = [pygame.image.load(r'ยาน 1.png'),
     pygame.image.load(r'ยาน 2.png'),
     pygame.image.load(r'ยาน 3.png')]
x = 235
y = 250
num = 0
animate = 0

score = 0

try:
    with open("high_score.csv",'r') as f:
        r = reader(f)
        l = list(r)
    high_score = l[0][1]
    name_score = l[0][0]
except:
    print('filenoload')

while True :
    screen.blit(bg,(0,0))
    pygame.time.delay(12)
    screen.blit(font.render("Time : "+ time_count, True, (255, 250, 205, 255)), (0,40))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.USEREVENT:
            counter -= 1
            time_count = str(counter) if counter > 0 else ' UP !'
            try :
                if int(score) > int(high_score):
                    with open("high_score.csv",'w') as f:
                        w = writer(f,lineterminator = '\n')
                        w.writerow([name,str(score)])
            except:
                print('filenosave')
                


    i_drop = i_drop + 5
    if i_show == 1 and \
        x >= i_x and \
        x <= (i_x + i[0].get_width()) and \
        y >= i_y+i_drop and \
        y <= (i_y + i[0].get_height()+i_drop) :
            i_show = 0
            score = score + 5
    if i_show == 1 :
        screen.blit(i[0],(i_x,i_y+i_drop))

    if i_show2 == 1 and \
        x >= i_x2 and \
        x <= (i_x2 + i[1].get_width()) and \
        y >= i_y2 + i_drop and \
        y <= (i_y2 + i[1].get_height()+i_drop)  :
            i_show2 = 0
            score = score + 5
    if i_show2 == 1 :
        screen.blit(i[1],(i_x2,i_y2+i_drop))

    if i_show3 == 1 and \
        x >= i_x3 and \
        x <= (i_x3 + i[2].get_width()) and \
        y >= i_y3 + i_drop and \
        y <= (i_y3 + i[2].get_height()+i_drop)  :
            i_show3 = 0
            score = score + 10
    if i_show3 == 1 :
        screen.blit(i[2],(i_x3,i_y3+i_drop))

    if i_show4 == 1 and \
        x >= i_x4 and \
        x <= (i_x4 + i[3].get_width()) and \
        y >= i_y4 + i_drop and \
        y <= (i_y4 + i[3].get_height()+i_drop)  :
            i_show4 = 0
            score = score - 10
    if i_show4 == 1 :
        screen.blit(i[3],(i_x4,i_y4+i_drop))

    if i_show5 == 1 and \
        x >= i_x5 and \
        x <= (i_x5 + i[4].get_width()) and \
        y >= i_y5 + i_drop and \
        y <= (i_y5 + i[4].get_height()+i_drop)  :
            i_show5 = 0
            score = score + 5
    if i_show5 == 1 :
        screen.blit(i[4],(i_x5,i_y5+i_drop))

    if i_show6 == 1 and \
        x >= i_x6 and \
        x <= (i_x6 + i[5].get_width()) and \
        y >= i_y6+i_drop and \
        y <= (i_y6 + i[5].get_height()+i_drop)  :
            i_show6 = 0
            score = score + 10
    if i_show6 == 1 :
        screen.blit(i[5],(i_x6,i_y6+i_drop))
        
    if i_show7 == 1 and \
        x >= i_x7 and \
        x <= (i_x7 + i[6].get_width()) and \
        y >= i_y7+i_drop and \
        y <= (i_y7 + i[6].get_height()+i_drop)  :
            i_show7 = 0
            score = score + 10
    if i_show7 == 1 :
        screen.blit(i[6],(i_x7,i_y7+i_drop))

    if i_show8 == 1 and \
        x >= i_x8 and \
        x <= (i_x8 + i[7].get_width()) and \
        y >= i_y8 + i_drop and \
        y <= (i_y8 + i[7].get_height()+i_drop)  :
            i_show8 = 0
            score = score + 5
    if i_show8 == 1 :
        screen.blit(i[7],(i_x8,i_y8+i_drop))

    if i_show9 == 1 and \
        x >= i_x9 and \
        x <= (i_x9 + i[8].get_width()) and \
        y >= i_y9 + i_drop and \
        y <= (i_y9 + i[8].get_height()+i_drop)  :
            i_show9 = 0
            score = score + 10
    if i_show9 == 1 :
        screen.blit(i[8],(i_x9,i_y9+i_drop))

    if i_show10 == 1 and \
        x >= i_x10 and \
        x <= (i_x10 + i[9].get_width()) and \
        y >= i_y10 + i_drop and \
        y <= (i_y10 + i[9].get_height()+i_drop)  :
            i_show10 = 0
            score = score + 5
    if i_show10 == 1 :
        screen.blit(i[9],(i_x10,i_y10+i_drop))
        
    if i_show11 == 1 and \
        x >= i_x11 and \
        x <= (i_x11 + i[10].get_width()) and \
        y >= i_y11 + i_drop and \
        y <= (i_y11 + i[10].get_height()+i_drop)  :
            i_show11 = 0
            score = score - 10
    if i_show11 == 1 :
        screen.blit(i[10],(i_x11,i_y11+i_drop))

    if i_show12 == 1 and \
        x >= i_x12 and \
        x <= (i_x12 + i[11].get_width()) and \
        y >= i_y12 + i_drop and \
        y <= (i_y12 + i[11].get_height()+i_drop)  :
            i_show12 = 0
            score = score + 10
    if i_show12 == 1 :
        screen.blit(i[11],(i_x12,i_y12+i_drop))

    if i_show13 == 1 and \
        x >= i_x13 and \
        x <= (i_x13 + i[12].get_width()) and \
        y >= i_y13 + i_drop and \
        y <= (i_y13 + i[12].get_height()+i_drop)  :
            i_show13 = 0
            score = score + 5
    if i_show13 == 1 :
        screen.blit(i[12],(i_x13,i_y13+i_drop))

    if i_show14 == 1 and \
        x >= i_x14 and \
        x <= (i_x14 + i[13].get_width()) and \
        y >= i_y14 + i_drop and \
        y <= (i_y14 + i[13].get_height()+i_drop)  :
            i_show14 = 0
            score = score - 10
    if i_show14 == 1 :
        screen.blit(i[13],(i_x14,i_y14+i_drop))

    if i_show15 == 1 and \
        x >= i_x15 and \
        x <= (i_x15 + i[14].get_width()) and \
        y >= i_y15 + i_drop and \
        y <= (i_y15 + i[14].get_height()+i_drop)  :
            i_show15 = 0
            score = score + 10
    if i_show15 == 1 :
        screen.blit(i[14],(i_x15,i_y15+i_drop))

    if i_show16 == 1 and \
        x >= i_x16 and \
        x <= (i_x16 + i[15].get_width()) and \
        y >= i_y16 + i_drop and \
        y <= (i_y16 + i[15].get_height()+i_drop)  :
            i_show16 = 0
            score = score + 5
    if i_show16 == 1 :
        screen.blit(i[15],(i_x16,i_y16+i_drop))

    if i_show17 == 1 and \
        x >= i_x17 and \
        x <= (i_x17 + i[16].get_width()) and \
        y >= i_y17 + i_drop and \
        y <= (i_y17 + i[16].get_height()+i_drop)  :
            i_show17 = 0
            score = score + 5
    if i_show17 == 1 :
        screen.blit(i[16],(i_x17,i_y17+i_drop))

    if i_show18 == 1 and \
        x >= i_x18 and \
        x <= (i_x18 + i[17].get_width()) and \
        y >= i_y18 + i_drop and \
        y <= (i_y18 + i[17].get_height()+i_drop)  :
            i_show18 = 0
            score = score + 10
    if i_show18 == 1 :
        screen.blit(i[17],(i_x18,i_y18+i_drop))

    if i_show19 == 1 and \
        x >= i_x19 and \
        x <= (i_x19 + i[18].get_width()) and \
        y >= i_y19 + i_drop and \
        y <= (i_y19 + i[18].get_height()+i_drop)  :
            i_show19 = 0
            score = score + 5
    if i_show19 == 1 :
        screen.blit(i[18],(i_x19,i_y19+i_drop))

    if i_show20 == 1 and \
        x >= i_x20 and \
        x <= (i_x20 + i[19].get_width()) and \
        y >= i_y20 + i_drop and \
        y <= (i_y20 + i[19].get_height()+i_drop)  :
            i_show20 = 0
            score = score - 10
    if i_show20 == 1 :
        screen.blit(i[19],(i_x20,i_y20+i_drop))

        if i_show21 == 1 and \
        x >= i_x21 and \
        x <= (i_x21 + i[20].get_width()) and \
        y >= i_y21 + i_drop and \
        y <= (i_y21 + i[20].get_height()+i_drop)  :
            i_show21 = 0
            score = score + 5
    if i_show21 == 1 :
        screen.blit(i[20],(i_x21,i_y21+i_drop))

    if i_show22 == 1 and \
        x >= i_x22 and \
        x <= (i_x22 + i[21].get_width()) and \
        y >= i_y22 + i_drop and \
        y <= (i_y22 + i[21].get_height()+i_drop)  :
            i_show22 = 0
            score = score + 5
    if i_show22 == 1 :
        screen.blit(i[21],(i_x22,i_y22+i_drop))

    if i_show23 == 1 and \
        x >= i_x23 and \
        x <= (i_x23 + i[22].get_width()) and \
        y >= i_y23 + i_drop and \
        y <= (i_y23 + i[22].get_height()+i_drop)  :
            i_show23 = 0
            score = score + 10
    if i_show23 == 1 :
        screen.blit(i[22],(i_x23,i_y23+i_drop))

    if i_show24 == 1 and \
        x >= i_x24 and \
        x <= (i_x24 + i[23].get_width()) and \
        y >= i_y24 + i_drop and \
        y <= (i_y24 + i[23].get_height()+i_drop)  :
            i_show24 = 0
            score = score + 5
    if i_show24 == 1 :
        screen.blit(i[23],(i_x24,i_y24+i_drop))

    if i_show25 == 1 and \
        x >= i_x25 and \
        x <= (i_x25 + i[24].get_width()) and \
        y >= i_y25 + i_drop and \
        y <= (i_y25 + i[24].get_height()+i_drop)  :
            i_show25 = 0
            score = score - 10
    if i_show25 == 1 :
        screen.blit(i[24],(i_x25,i_y25+i_drop))

    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > 0:
        x = x - 7
    if keys[pygame.K_d] and x < 500:
        x = x + 7
    if keys[pygame.K_w] and y > 0:
        y = y - 7
    if keys[pygame.K_s] and y < 650:
        y = y + 7
        
    if num % 15 == 0:
        animate = animate + 1
        if animate > 2 :
            num = 0
            animate = 0
    num = num + 1


    screen.blit(font.render("High Score : " + high_score,1, (0, 255, 255, 255)), (220,0))
    screen.blit(font.render("High Score name : "+name_score,1, (0, 255, 255, 255)), (220,40))
    text = font.render("Score : " + str(score),1,(124, 252, 0, 255))
    
    screen.blit(text,(0,0))
    
    screen.blit(t[animate],(x,y))
    pygame.display.update()
    clock.tick(60)

