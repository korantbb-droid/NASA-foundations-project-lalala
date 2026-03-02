import pygame
import pygame_widgets
import random
from pygame_widgets.button import Button

pygame.init()

window = pygame.display.set_mode((1000, 1000))

#Question List
questionList = ['What is 2 + 2?', 'What is the capital of France?', 'What color is the sky?', 'What is the largest mammal?', 'What is the boiling point of water?', 'What is the smallest prime number?', 
                'What is the currency of Japan?', 'What is the chemical symbol for gold?', 'What is the tallest mountain in the world?', 'What is the largest ocean on Earth?', 'What is the square root of 16?', 
                'What is the capital of Australia?', 'What is the largest planet in our solar system?', 'What is the chemical symbol for oxygen?', 'What is the longest river in the world?', 
                'What is the currency of the United States?', 'What is the smallest country in the world?', 'What is the chemical symbol for carbon?', 'What is the highest waterfall in the world?', 
                'What is the largest desert on Earth?', 'What is the capital of Canada?', 'What is the chemical symbol for hydrogen?', 'What is the longest mountain range in the world?', 
                'What is the currency of the United Kingdom?', 'What is the smallest continent in the world?', 'What is the chemical symbol for nitrogen?', 'What is the highest mountain in Africa?', 
                'What is the largest lake in the world?', 'What is the capital of Germany?', 'What is the chemical symbol for helium?']

#Plane Var
plane_x = 250
plane_y = 700
plane_width = 40
plane_height = 60
plane_vel = 8

#Bullet Var
bullet_width = 10
bullet_height = 20
bullet_x = plane_x + (plane_width - bullet_width)/2
bullet_y = plane_y-50

isFiring = False

#Question Var
question_width = 200
question_height = 100

question_Y = 200

rightAnswer = 1

checkAnswer = False
q1Anwer = False
q2Answer = False
q3Answer = False

score = 0
showQuestion = True

difficulty = 40

#Lives Var
heartImg = pygame.image.load('heart.png')
heartImg = pygame.transform.scale(heartImg, (50, 50))

totalLives = 3

#Custom Screen Var
ifStart = True
ifCustom = True

#set ifCustom Var False
def setCustomFalse():
    global ifCustom
    ifCustom = False


#Set Difficulties

def setEasy():
    global difficulty
    difficulty = 40

def setMedium():
    global difficulty
    difficulty = 25

def setHard():
    global difficulty
    difficulty = 15

#Cycle Var
cycle1 = 2
color1 = (0,255,0)

#Win Var
ifWin = False

def resetGame():
    global score
    global totalLives
    global ifWin
    global ifCustom
    global ifStart
    global question_Y
    global showQuestion
    showQuestion = True
    question_Y = 200
    score = 0
    totalLives = 3
    ifWin = False
    ifCustom = True
    ifStart = True

def displayGameOver():
    global ifWin
    global button
    global button2
    global button3
    global button4
    global confirmButton
    window.fill((0,0,0))
    font = pygame.font.SysFont('Arial', 100)
    text = font.render('Game Over', True, (255, 0, 0))
    window.blit(text, (500-text.get_width()//2, 300))
    text2 = font.render(f'Final Score: {score}', True, (255, 0, 0))
    window.blit(text2, (500-text2.get_width()//2, 400))
    restartButton = Button(window, 400, 700, 200, 75, text='Restart', fontSize=30, margin=20, onClick=lambda: resetGame())
    button = 0
    button2 = 0
    button3 = 0
    button4 = 0
    confirmButton = 0
    pygame_widgets.update(pygame.event.get())
    pygame.display.update()

def displayWin():
    global ifWin
    global button
    global button2
    global button3
    global button4
    global confirmButton
    ifWin = True
    window.fill((0,0,0))
    font = pygame.font.SysFont('Arial', 100)
    text = font.render('You Win!', True, (0, 255, 0))
    window.blit(text, (500-text.get_width()//2, 300))
    text2 = font.render(f'Final Score: {score}', True, (0, 255, 0))
    window.blit(text2, (500-text2.get_width()//2, 400))
    restartButton = Button(window, 400, 700, 200, 75, text='Restart', fontSize=30, margin=20, onClick=lambda: resetGame())
    button = 0
    button2 = 0
    button3 = 0
    button4 = 0
    confirmButton = 0
    pygame_widgets.update(pygame.event.get())
    pygame.display.update()

    
def displayCorrect():
    global showQuestion
    text = font.render('Correct!', True, (0, 255, 0))
    window.blit(text, (400, 500))
    pygame.display.update()
    pygame.time.delay(1000)
    showQuestion = True

def setSettingFalse():
    global setting
    setting = False

def setSetting():
    global settings
    global setting
    setting = True
    while setting:
        window.fill((255,255,255))
        font = pygame.font.SysFont("Arial", 75)
        text = font.render("Choose your difficulty", True, (0,0,0))
        window.blit(text, (500-text.get_width()//2, 250))

        settings = Button(window, 50, 50, 100, 100, text='Go Back', fontSize=30, margin=20, onClick=lambda: setSettingFalse())

        easy = Button(window, 100, 600, 200, 75, text='Easy', fontSize=30, margin=20, onClick=lambda: setEasy())
        medium = Button(window, 400, 600, 200, 75, text='Medium', fontSize=30, margin=20, onClick=lambda: setMedium())
        hard = Button(window, 700, 600, 200, 75, text='Hard', fontSize=30, margin=20, onClick=lambda: setHard())
        pygame_widgets.update(pygame.event.get())

        pygame.display.update()

    



def displayWrong():
    global showQuestion
    text = font.render('Wrong!', True, (255, 0, 0))
    window.blit(text, (400, 500))
    pygame.display.update()
    pygame.time.delay(1000)
    showQuestion = True

def drawFirstRect():
    global cycle1
    global color1
    if cycle1 == 1:
        color1 = (0,255,0)
    elif cycle1 == 2:
        color1 = (255,0,0)
    elif cycle1 == 3:
        color1 = (0,0,255)
    else:
        cycle1 = 1
        color1 = (0,255,0) 
    cycle1 += 1

cycle2 = 2
color2 = (0,255,0)

def drawSecRect():
    global cycle2
    global color2
    if cycle2 == 1:
        color2 = (0,255,0)
    elif cycle2 == 2:
        color2 = (255,0,0)
    elif cycle2 == 3:
        color2 = (0,0,255)
    else:
        cycle2 = 1
        color2 = (0,255,0) 
    cycle2 += 1

cycle3 = 2
color3 = (0,255,0)

def drawThirdRect():
    global cycle3
    global color3
    if cycle3 == 1:
        color3 = (0,255,0)
    elif cycle3 == 2:
        color3 = (255,0,0)
    elif cycle3 == 3:
        color3 = (0,0,255)
    else:
        cycle3 = 1
        color3 = (0,255,0) 
    cycle3 += 1

cycle4 = 2
color4 = (0,255,0)

def drawFourthRect():
    global cycle4
    global color4
    if cycle4 == 1:
        color4 = (0,255,0)
    elif cycle4 == 2:
        color4 = (255,0,0)
    elif cycle4 == 3:
        color4 = (0,0,255)
    else:
        cycle4 = 1
        color4 = (0,255,0) 
    cycle4 += 1


run = True

#Keep Running
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            ifStart = False
            ifCustom = False
            ifQuestion = False

    pygame.time.delay(difficulty)

#Start Screen
    while ifStart:
        window.fill((255, 255, 255))

        font = pygame.font.SysFont('Arial', 50)

        intro = font.render('Welcome to the Quiz Game!', True, (0, 0, 255))
        window.blit(intro, (500 - intro.get_width()//2, 400))
        start = font.render('Press Y to Start', True, (0, 0, 255))
        window.blit(start, (500 - start.get_width()//2, 500))

        settings = Button(window, 50, 50, 100, 100, text='Settings', fontSize=30, margin=20, onClick=lambda: setSetting())

        pygame_widgets.update(pygame.event.get())
        pygame.display.update()
                
        #Y Trigger to start game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_y]:
            ifStart = False

        #Checking for Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                ifStart = False
                ifCustom = False
                ifQuestion = False

#Custom Screen for Plane
    while ifCustom:
        window.fill(((255, 255, 255)))
        font = pygame.font.SysFont('Arial', 50)
        pygame.draw.rect(window, (0,255,0), (75,100,450,800))


        #Drawing Buttons
        settings = 0
        button = Button(window, 912.5,125,75,75, text='>', fontSize=30, margin=20, onClick=lambda: drawFirstRect())
        button2 = Button(window, 912.5,350,75,75, text='>', fontSize=30, margin=20, onClick=lambda: drawSecRect())
        button3 = Button(window, 912.5,575,75,75, text='>', fontSize=30, margin=20, onClick=lambda: drawThirdRect())
        button4 = Button(window, 912.5,800,75,75, text='>', fontSize=30, margin=20, onClick=lambda: drawFourthRect())
        confirmButton = Button(window, 200,905,200,75, text="Confirm Plane", fontSize=30, margin=20, onClick=lambda: setCustomFalse())

        #Draw Custom Boxes for Diff Parts
        pygame.draw.rect(window, (color1), (600,75,300,175))
        pygame.draw.rect(window, (color2), (600,300,300,175))
        pygame.draw.rect(window, (color3), (600,525,300,175))
        pygame.draw.rect(window, (color4), (600,750,300,175))


        #Update Buttons and Display
        pygame_widgets.update(pygame.event.get())
        pygame.display.update()

        #Checking for Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                ifStart = False
                ifCustom = False
                ifQuestion = False



#Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and plane_x > 50:
            plane_x -= plane_vel
    if keys[pygame.K_RIGHT] and plane_x < 900:
            plane_x += plane_vel
    if keys[pygame.K_SPACE] and isFiring == False:  
        bullet_x = plane_x + (plane_width - bullet_width)/2
        isFiring = True
    if keys[pygame.K_t]:
        showQuestion = True
    if keys[pygame.K_p]:
        score = 10000

          
#White Background
    window.fill((255, 255, 255))

#Check if Game Over
    if totalLives == 0 or score == 10:
        showQuestion = False

#Displaying Question
    if showQuestion:
        font = pygame.font.SysFont('Arial', 30)
        randomQuestion = random.randint(0, len(questionList)-1)
        questionText = font.render(questionList[randomQuestion], True, (0, 0, 0))
        window.blit(questionText, (500-questionText.get_width()//2, 400))
        pygame.display.update()
        pygame.time.delay(3000)
        showQuestion = False

#Drawing Plane
    pygame.draw.rect(window, (255, 0, 0), (plane_x, plane_y, plane_width, plane_height))

#Drawing the 3 Possible Questions
    pygame.draw.rect(window, (0,255,0), (100,question_Y,question_width,question_height))
    pygame.draw.rect(window, (0,255,0), (400,question_Y,question_width,question_height))
    pygame.draw.rect(window, (0,255,0), (700,question_Y,question_width,question_height))

#Update Score
    font = pygame.font.SysFont('Arial', 50)
    scoreText = font.render(f'Score: {score}', True, (0, 0, 0))
    window.blit(scoreText, (700, 50))

#Drawing Lives & Checking Win/Lose
    if totalLives == 3:
        window.blit(heartImg, (50, 50))
        window.blit(heartImg, (110, 50))
        window.blit(heartImg, (170, 50))   
    elif totalLives == 2:
        window.blit(heartImg, (50, 50))
        window.blit(heartImg, (110, 50))
    elif totalLives == 1:
        window.blit(heartImg, (50, 50))
    else:
        displayGameOver() 
    if score == 10000:
        displayWin()

#Bulllet Drawing + Firing
    if isFiring and (bullet_y > 0):   
        pygame.draw.rect(window,(0,0,255),(bullet_x,bullet_y, bullet_width,bullet_height))
        bullet_y -= 10
    else:
        isFiring = False
        bullet_y = plane_y - 25

#Check Collision

    q1BoundaryLeft = (100 - bullet_width)
    q1BouondaryRight = (300 - bullet_width)

    q2BoundaryLeft = (400 - bullet_width)
    q2BouondaryRight = (600 - bullet_width)
                        
    q3BoundaryLeft = (700 - bullet_width)
    q3BoundaryRight = (900 - bullet_width)

    if bullet_y < (question_Y + 90) and (q1BoundaryLeft < bullet_x < q1BouondaryRight) and isFiring:
         q1Anwer = True
         isFiring = False
         checkAnswer = True

    if bullet_y < (question_Y + 90) and (q2BoundaryLeft < bullet_x < q2BouondaryRight) and isFiring:
         q2Answer = True
         isFiring = False
         checkAnswer = True

    if bullet_y < (question_Y + 90) and (q3BoundaryLeft < bullet_x < q3BoundaryRight) and isFiring:
         q3Answer = True
         isFiring = False
         checkAnswer = True

    if (question_Y > 600) and (not ifWin):
        displayGameOver()

#Set Question Movement
    if q1Anwer or q2Answer or q3Answer:
        question_Y = 200
    else:
        question_Y += 2

#Check if Correct Answer
    if checkAnswer:
        if q1Anwer:
            if rightAnswer == 1:
                score += 1000
                displayCorrect()
            else:
                totalLives -= 1
                displayWrong()

        elif q2Answer:
            if rightAnswer == 2:
                score += 1000
                displayCorrect()
            else:
                totalLives -= 1
                displayWrong()
        else:
            if rightAnswer == 3:
                score += 1000
                displayCorrect()
            else:
                totalLives -= 1
                displayWrong()
        
        checkAnswer = False
        q1Anwer = False
        q2Answer = False
        q3Answer = False


#Update Display
    pygame.display.update()

pygame.quit()