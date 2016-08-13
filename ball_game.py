#---------------importing things----------------------------------------|
import pygame
import random
print(random.randint(0,9))





#--------------------initialize pygame and items----------------------------|
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()






#----------------------initial values----------------------------------------------|
white=(255,255,255)
red=(255,00,00)
black=(0,0,0)
color1=red
color2=black
color3=black
color4=black
flytime_meter=(255,215,0)
x=100
y=300
clock=pygame.time.Clock()
a=0
b=0
p=500
q1=1100
q2=-200
speed=5
move="no"
jump=False
stop=False
game=None
startGame=False
tick=65
angle=0
run=10
score=0
highscore=score
go=False
obs=1
wings=False
flytime=0
roll=False
howTo=False
rolltime=0
woodx=-200
wood2x=-200
newwood=False
HSsound=False
flyx=random.randint(800,10000)
startScreen=pygame.image.load("start.jpg")
img1=pygame.image.load("1.gif")
img3=pygame.image.load("wall.jpg")
obs1=pygame.image.load("obs1.gif")
obs2=pygame.image.load("obs2.gif")
sky=pygame.image.load("sky.jpg")
fly=pygame.image.load("fly.gif")
wood=pygame.image.load("wood.gif")
wood2=pygame.image.load("wood2.gif")
jump_sound=pygame.mixer.Sound("jump.wav")
collide_sound=pygame.mixer.Sound("collide.wav")
land_sound=pygame.mixer.Sound("land.wav")
fly_sound=pygame.mixer.Sound("fly.wav")
high_score=pygame.mixer.Sound("high_score.wav")
gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption("Practice")
gameExit = False
pause=None
gameDisplay.fill(white) 
pygame.display.update()
pygame.mixer.music.load("Kevin MacLeod - Carefree.mp3")
pygame.mixer.music.play(-1)






#game loop begins----------------------------------------------------------|
while not gameExit:





#-------------------------For Starting screen-----------------------------|   
    while startGame==False:
    
      gameDisplay.blit(startScreen,(0,0))
      if howTo==False:
        font=pygame.font.SysFont("forte",60)
        text1=font.render("Start",True, color1)
        gameDisplay.blit(text1,(400,170))
        text2=font.render("How to Play",True, color2)
        gameDisplay.blit(text2,(400,230))
        text3=font.render("Game Intro",True, color3)
        gameDisplay.blit(text3,(400,290))
        text4=font.render("Quit",True, color4)
        gameDisplay.blit(text4,(400,350))
      pygame.display.update()


    #-----------------For toggel through start buttons----------------------------|
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=True
            startGame=True
        if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_DOWN and color1==red:
                    color1=black
                    color2=red
                    event.key==None
                    pygame.mixer.Sound.play(fly_sound)
           elif event.key==pygame.K_DOWN and color2==red:
                    color2=black
                    color3=red
                    event.key==None
                    pygame.mixer.Sound.play(fly_sound)
           elif event.key==pygame.K_DOWN and color3==red:
                    color3=black
                    color4=red
                    event.key==None
                    pygame.mixer.Sound.play(fly_sound)
           elif event.key==pygame.K_UP and color4==red:
                    color4=black
                    color3=red
                    event.key==None
                    pygame.mixer.Sound.play(fly_sound)
           elif event.key==pygame.K_UP and color3==red:
                    color3=black
                    color2=red
                    event.key==None
                    pygame.mixer.Sound.play(fly_sound)
           elif event.key==pygame.K_UP and color2==red:
                    color2=black
                    color1=red
                    event.key==None
                    pygame.mixer.Sound.play(fly_sound)
           elif event.key==pygame.K_f:
                gameDisplay=pygame.display.set_mode((800,580),pygame.FULLSCREEN)
           elif event.key==pygame.K_SPACE:
             startScreen=pygame.image.load("start.jpg")
             howTo=False
             pygame.mixer.Sound.play(collide_sound)
           elif event.key==pygame.K_RETURN and color1==red:
            startGame=True
            pygame.mixer.Sound.play(collide_sound)
           elif event.key==pygame.K_RETURN and color2==red:
            startScreen=pygame.image.load("howToPlay.jpg")
            howTo=True
           elif event.key==pygame.K_RETURN and color3==red:
            startScreen=pygame.image.load("intro.jpg")
            howTo=True
            pygame.mixer.Sound.play(collide_sound)
           elif event.key==pygame.K_RETURN and color4==red:
            pygame.quit()
            quit()
           elif event.key==pygame.K_m:
                pygame.mixer.music.stop()
           elif event.key==pygame.K_n:
                pygame.mixer.music.play(-1)
                    
           
                







    #---------------for getting the input keys--------------------------------|
    for event in pygame.event.get():
        
      if event.type==pygame.QUIT:
            gameExit=True        

      if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT and stop==False:
                move="right"
                go=True 
                a=+5
            elif event.key==pygame.K_UP and b==0 and wings==False:
                move="no"
                jump=True
                pygame.mixer.Sound.play(jump_sound)
            elif event.key==pygame.K_DOWN and y!=300:
                move="down"
                jump=True
                wings=False
            elif event.key==pygame.K_DOWN and y==300:
                jump=False
                move="right"
                roll=True
                rolltime=0
            elif event.key==pygame.K_f:
                gameDisplay=pygame.display.set_mode((800,580),pygame.FULLSCREEN)
                gameDisplay.fill(white)
            elif event.key==pygame.K_p:
                pause=True
            elif event.key==pygame.K_ESCAPE:
                startGame=False
            elif event.key==pygame.K_m:
                pygame.mixer.music.stop()
            elif event.key==pygame.K_n:
                pygame.mixer.music.play(-1)





     #--------------------------to pause the game---------------------------|
    while pause==True:
        font=pygame.font.SysFont("forte",100)
        text=font.render("Paused",True, black)
        gameDisplay.blit(text,(250,150))
        font=pygame.font.SysFont("forte",50)
        text=font.render("Press C to continue ",True, black)
        gameDisplay.blit(text,(220,240))
        pygame.display.update()
        
        for event in pygame.event.get():
             if event.key==pygame.K_c:
                 pause=False



                

   
    #---------------for player movements--------------------------|                      
    x=x+a
    y=y+b




    

#--------------running and jumping animation-------------------------------|     
    if jump==True and y!=300:
        angle=angle+90
        img1=pygame.image.load("2.gif")
    else:
        if run<=30 and go==True:
          img1=pygame.image.load("1.gif")
        elif run>30 and run<60 or go==False:
            img1=pygame.image.load("2.gif")
        else:
            img1=pygame.image.load("3.gif")
        

    run=run+5
    if run==90:
        run=10





#-------------------to detect collision between player and power-ups------------------------|
    if((x<=flyx+40) and (x>=flyx) or (x+50<=flyx+45) and (x+45>=flyx) ):
        if(y+20>=220 and y<=270):
          pygame.draw.circle(gameDisplay,white,(flyx+25+5,220+25),32) 
          pygame.mixer.Sound.play(fly_sound)
          pygame.draw.circle(gameDisplay,white,(x+25-a,y+25),30)
          flyx=random.randint(800,10000)
          wings=True
          jump=False
          b=0
          flytime=0




          
#-------------------------------to make player fly--------------------------------------------------|
    if wings==True:
       flytime=flytime+1
       speed=speed+2

       if y>200:
           b=-speed
       elif y<=200:
            b=0

       if run<=45:
           img1=pygame.image.load("4.gif")
       else:
            img1=pygame.image.load("5.gif")
       if flytime==300:
          jump=True
          move="Down"
          wings=False

          flytime=0





          

#---------------------------to make player roll--------------------------------------|
    if roll==True and jump==False:
        rolltime=rolltime+1
        speed=speed+2
        img1=pygame.image.load("6.gif")
        y=304
        if rolltime%2==0:
            angle=angle+90
        if rolltime==50:
            angle=0
            y=300
            roll=False
    if roll==False and jump==False:
        angle=0

    img1=pygame.transform.rotate(img1,angle)






#--------------------for the moving purpose-----------------------------|
    if x>=300:
        p=p-speed
        q1=q1-speed
        q2=q2-speed
        flyx=flyx-speed
        woodx=woodx-speed
        wood2x=wood2x-speed

    if p<=-150:
        p=800
        if obs==1:
            q2=random.randint(p+250,p+700)
            obs=2
        else:
            q1=random.randint(p+250,p+700)
            obs=1
        if q1>p+500 or q2>p+500 and wood2x==-100:
            wood2x=random.randint(p+250,p+300)
     
    if flyx<=-100:
        flyx=random.randint(800,10000)
        
    if q1>=250+p and q1<=400+p and newwood==True:
        woodx=random.randint(q1+300,q1+300)
        newwood=False
    if q2>=250+p and q2<=400+p and newwood==True:
        woodx=random.randint(q2+300,q2+350)
        newwood=False
        
    if woodx<=-700:
         newwood=True







        
#------------------for printing the graphics------------------------------|    
    

    gameDisplay.fill(white) 
    gameDisplay.blit(sky,(0,0))
    gameDisplay.blit(img3,(0,350))
    gameDisplay.blit(obs1,(q1,280))
    gameDisplay.blit(obs2,(q2,280))
    gameDisplay.blit(img1,(x,y))
    gameDisplay.blit(fly,(flyx,220))
    gameDisplay.blit(wood,(woodx,197))
    gameDisplay.blit(wood2,(wood2x,284))
    pygame.draw.rect(gameDisplay,white,(p,350,100,300))
    font=pygame.font.SysFont("forte",50)
    text=font.render("Score : ",True, black)
    gameDisplay.blit(text,(10,10))
    text=font.render(str(score),True, black)
    gameDisplay.blit(text,(165,10))
    font=pygame.font.SysFont("forte",30)
    text=font.render("High Score : ",True, black)
    gameDisplay.blit(text,(10,60))
    text=font.render(str(highscore),True, black)
    gameDisplay.blit(text,(180,60))
    if wings==True:
       font=pygame.font.SysFont("forte",30)
       text=font.render("Wings : ",True, black)
       gameDisplay.blit(text,(10,98))
       pygame.draw.rect(gameDisplay,black,(118,106,152-(flytime/2),22))
       pygame.draw.rect(gameDisplay,flytime_meter,(120,108,150-(flytime/2),20))
       if flytime>=170:
           flytime_meter=red
       else:
           flytime_meter=(255,215,0)

    pygame.display.update()




#----------------To play sound for highscore--------------------|

    if score>=highscore and HSsound==True:
        pygame.mixer.Sound.play(high_score)
        HSsound=False
        
    




        

#----------increase score----------------------------------------------|
    if go==True:
        score=score+1



        

#------set the speed of game according to score---------------------------|
    if score<=500:
        tick=200
        speed=6
    if score>=500 and score<1000:
        tick=75
        speed=8
    if score>=1000 and score<1500:
        tick=95
        speed=9
    if score>=1500 and score<2500:
        tick=100
        speed=10
    if score>=2500 and score<3500:
        tick=130
        speed=12
    if score>=3500 and score<5000:
        speed=13
    if score>=5000:
        speed=15
        





#-------------------to detect collision between player and obstracles------------------------|
    if((x<=q1+40) and (x>=q1) or (x+50<=q1+45) and (x+45>=q1) ):
        if(y+20>=280 and y<=350):
          pygame.mixer.Sound.play(collide_sound)
          game="restart"


    if((x<=q2+40) and (x>=q2) or (x+50<=q2+45) and (x+45>=q2) ):
        if(y+20>=280 and y<=350):
          pygame.mixer.Sound.play(collide_sound)
          game="restart"




#-------------------to detect collision between player and wood------------------------|
    if x+40>=woodx and x+50<=woodx+166 and roll!=True:
        game="restart"
        pygame.mixer.Sound.play(collide_sound)

    if((x<=wood2x+68) and (x>=wood2x) or (x+50<=wood2x+68) and (x+45>=wood2x) and roll!=True):
        if(y+20>=284 and y<=350 and roll!=True):
          pygame.mixer.Sound.play(collide_sound)
          game="restart"


        



          
#---------when player covers 300px from the beggining new movement animation starts----------------------|          
    if x>=300:
        a=0
        stop=True






#--------------makes the player jump-----------------------|
    if jump==True:
        b=-speed
        roll=False
        if y<180 or move=="down":
            move="down"
            b=+speed
            if y>=300:
                jump=False
                move="right"
                b=0
                y=300
                flytime=0
                y=300
                




#----------------when player falls from the hole-------------------------|
    if(x>=p-25 and x<=p+75 and jump!=True and wings!=True):
        img1=pygame.image.load("2.gif")
        gameDisplay.blit(img1,(x,y))
        pygame.display.update() 
        game="restart"      
        clock.tick(20)
        for z in range(1,100,1):
            y=y+8
            pygame.draw.rect(gameDisplay,white,(p-40,300,180,250))
            pygame.draw.circle(gameDisplay,white,(x+20,y+25),26)
            gameDisplay.blit(img3,(0,350))
            pygame.draw.rect(gameDisplay,white,(p,350,100,300))
            gameDisplay.blit(img1,(x,y))
            pygame.display.update()
            if z==99:
                pygame.mixer.Sound.play(collide_sound)   
            clock.tick(500)
        





#---------------------------to restart the game-------------------------------------|
    if(game=="restart"):
        #-------------Printing Final Score------|
        font=pygame.font.SysFont("forte",80)
        text=font.render("Your Score : ",True, black)
        gameDisplay.blit(text,(120,150))
        text=font.render(str(score),True, black)
        gameDisplay.blit(text,(560,150))
        pygame.display.update()
        clock.tick(1)
        #---------Assign initial values to restart game-----|
        x=100
        y=300
        clock=pygame.time.Clock()
        a=0
        b=0
        p=500

        q1=1100
        level=1
        move="no"
        jump=False
        stop=False
        game=None
        HSsound=True
        go=False
        wings=False
        tick=65
        q2=-200
        obs=1
        flyx=random.randint(800,10000)
        if score>=highscore:
            highscore=score
        score=0
        speed=5
        woodx=-200
        wood2x=-200
        newwood=False
         


#-------------to define game speed---------------------------------------|
    clock.tick(tick)
    



#--------------------when the game exits---------------------------------------|


pygame.quit()
quit()







