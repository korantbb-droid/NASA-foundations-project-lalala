import pygame
import pygame_widgets
import random
from pygame_widgets.button import Button

pygame.init()

#testing git push idk if this is going to work

window = pygame.display.set_mode((1000, 1000))

#Question List

questionDictionary = {
    'Sound travels in what form?': 'Waves',
    'Sound travels faster than light.': 'False',
    'What is the name of something that travels at the speed of sound?': 'Sonic',
    'What happens when a plane travels faster than sound?': 'it creates a sonic boom',
    'What is a sonic boom?': 'loud noise caused by shock waves',
    'What is the shape of a shock wave?': "Cone",
    'Which is faster?': 'Supersonic plane',
    'What is NASAs X-59 QUESST?': 'A supersonic plane being tested',
    'Why are sonic booms a problem?:': 'They scare people and animals',
    'What do shock waves cause?': 'Sonic Booms',
    'What was the point of creating the X-59?': 'To make supersonic flight quieter',
    'The FAA Regulation (FAR) prohibits supersonic flight over the US.': 'True',
    'What sound would be loudest?': 'A jet taking off',
    'Why don\'t all planes create sonic booms?': 'They fly slower than the speed of sound',
    'What is pitch?': 'How high or low a sound is',
    'What will have a higher pitch?': 'A whistle',
    'What is the volume (amplitude) of sound?': 'How loud or quiet a sound is',
    'Increasing the energy of a wave will increase its: ': 'Amplitude',
    'What type of wave is a sound wave?': 'A longitudinal wave',
    'What do I need to reduce to make a sound wave quieter?': 'Amplitude',
    'How is sound made?': 'Vibrations that produce sound waves',
    'What do sound waves carry?': 'Energy',
    'What is the X-59 shaped the way it is?': 'To reduce the loudness of sonic booms',
    'If a sonic boom is too loud:': 'Windows can shake or shatter',
    'The sound from the X-59 is most similar to:': 'A car door slammed from 20 ft away',
    'Why does a sonic boom happen after a plane passes you?': 'Sound travels slower than the plane',
    }
wrongAnswers1 = [
    'Circles',
    'True',
    'Hypersonic',
    'It vanishes',
    'A type of engine',
    'Square',
    'Subsonic plane',
    'a new rocket',
    'They make planes stop moving',
    'Rain',
    'So we can live on Mars',
    'False',
    'A whisper',
    'Most are planes are too small',
    'How fast something moves',
    'Thunder',
    'length * width * height',
    'Pitch',
    'a regular wave',
    'Pitch',
    'By light waves',
    'color',
    'it looks cooler',
    'people can be annoyed',
    'a big boom',
    'air moves too slow'
]

wrongAnswers2 = [
    'Circles',
    ' ',
    'Supersonic',
    'It automatically stops',
    'A noise made by any object',
    'Triangle',
    'They are the same',
    'A flying car',
    'They make everything quiet',
    'Heat',
    'To make invisible planes',
    ' ',
    'a ticking clock',
    'Most planes turn their volume down',
    'How bright something is',
    'a drum',
    'Pitch',
    'Frequency',
    'A happy wave',
    'Volume',
    'Heat energy',
    'Water',
    'To only fit one person',
    'The plane will stop moving',
    'a gunshot',
    'The plane will make the sound later'

]

plane_width = 120
plane_height = 180
plane_vel = 8
plane_x = 500
plane_y = 800

#Bullet Var
bullet_width = 15
bullet_height = 30
bullet_x = plane_x + (plane_width - bullet_width)/2
bullet_y = plane_y - 50
bullet = pygame.image.load('bullet.png').convert_alpha()
bullet = pygame.transform.scale(bullet, (bullet_width, bullet_height))

isFiring = False

#Question Var
question_width = 250
question_height = 150

question_Y = 200

rightAnswer = 1

checkAnswer = False
q1Anwer = False
q2Answer = False
q3Answer = False

score = 0
scoreMultiplyer = 2

showQuestion = True
newQuestion = True

difficulty = 25
setting = False

#Lives Var
heartImg = pygame.image.load('heart.png')
heartImg = pygame.transform.scale(heartImg, (50, 50))

totalLives = 3

#Cloud Image
cloudImg = pygame.image.load('cloud2.png')
cloudImg = pygame.transform.scale(cloudImg, (question_width, question_height)).convert_alpha()

#Background Image
bgImg = pygame.image.load('background.jpg')
bgImg = pygame.transform.scale(bgImg, (1000, 1000)).convert_alpha()

bgImg2 = pygame.image.load('background2.jpg')
bgImg2 = pygame.transform.scale(bgImg2, (1000, 1000)).convert_alpha()

#Custom Screen Var
ifStart = True
ifCustom = True

#norm Plane Images
norm_small_curve = pygame.image.load('norm_small_curve.png').convert_alpha()
norm_small_curve = pygame.transform.scale(norm_small_curve, (plane_width, plane_height))

norm_small_small = pygame.image.load('norm_small_small.png').convert_alpha()
norm_small_small = pygame.transform.scale(norm_small_small, (plane_width, plane_height))

norm_small_triangle = pygame.image.load('norm_small_triangle.png').convert_alpha()
norm_small_triangle = pygame.transform.scale(norm_small_triangle, (plane_width, plane_height))

norm_triangle_curve = pygame.image.load('norm_triangle_curve.png').convert_alpha()
norm_triangle_curve = pygame.transform.scale(norm_triangle_curve, (plane_width, plane_height))

norm_triangle_small = pygame.image.load('norm_triangle_small.png').convert_alpha()
norm_triangle_small = pygame.transform.scale(norm_triangle_small, (plane_width, plane_height))

norm_triangle_triangle = pygame.image.load('norm_triangle_triangle.png').convert_alpha()
norm_triangle_triangle = pygame.transform.scale(norm_triangle_triangle, (plane_width, plane_height))

norm_wide_curve = pygame.image.load('norm_wide_curve.png').convert_alpha()
norm_wide_curve = pygame.transform.scale(norm_wide_curve, (plane_width, plane_height))

norm_wide_small = pygame.image.load('norm_wide_small.png').convert_alpha()
norm_wide_small = pygame.transform.scale(norm_wide_small, (plane_width, plane_height))

norm_wide_triangle = pygame.image.load('norm_wide_triangle.png').convert_alpha()
norm_wide_triangle = pygame.transform.scale(norm_wide_triangle, (plane_width, plane_height))

#Short Plane Images

short_small_curve = pygame.image.load('short_small_curve.png').convert_alpha()
short_small_curve = pygame.transform.scale(short_small_curve, (plane_width, plane_height))

short_small_small = pygame.image.load('short_small_small.png').convert_alpha()
short_small_small = pygame.transform.scale(short_small_small, (plane_width, plane_height))

short_small_triangle = pygame.image.load('short_small_triangle.png').convert_alpha()
short_small_triangle = pygame.transform.scale(short_small_triangle, (plane_width, plane_height))

short_triangle_curve = pygame.image.load('short_triangle_curve.png').convert_alpha()
short_triangle_curve = pygame.transform.scale(short_triangle_curve, (plane_width, plane_height))

short_triangle_small = pygame.image.load('short_triangle_small.png').convert_alpha()
short_triangle_small = pygame.transform.scale(short_triangle_small, (plane_width, plane_height))

short_triangle_triangle = pygame.image.load('short_triangle_triangle.png').convert_alpha()
short_triangle_triangle = pygame.transform.scale(short_triangle_triangle, (plane_width, plane_height))

short_wide_curve = pygame.image.load('short_wide_curve.png').convert_alpha()
short_wide_curve = pygame.transform.scale(short_wide_curve, (plane_width, plane_height))

short_wide_small = pygame.image.load('short_wide_small.png').convert_alpha()
short_wide_small = pygame.transform.scale(short_wide_small, (plane_width, plane_height))

short_wide_triangle = pygame.image.load('short_wide_triangle.png').convert_alpha()
short_wide_triangle = pygame.transform.scale(short_wide_triangle, (plane_width, plane_height))

#Skinny Plane Images

skinny_small_curve = pygame.image.load('skinny_small_curve.png').convert_alpha()
skinny_small_curve = pygame.transform.scale(skinny_small_curve, (plane_width, plane_height))

skinny_small_small = pygame.image.load('skinny_small_small.png').convert_alpha()
skinny_small_small = pygame.transform.scale(skinny_small_small, (plane_width, plane_height))

skinny_small_triangle = pygame.image.load('skinny_small_triangle.png').convert_alpha()
skinny_small_triangle = pygame.transform.scale(skinny_small_triangle, (plane_width, plane_height))

skinny_triangle_curve = pygame.image.load('skinny_triangle_curve.png').convert_alpha()
skinny_triangle_curve = pygame.transform.scale(skinny_triangle_curve, (plane_width, plane_height))

skinny_triangle_small = pygame.image.load('skinny_triangle_small.png').convert_alpha()
skinny_triangle_small = pygame.transform.scale(skinny_triangle_small, (plane_width, plane_height))

skinny_triangle_triangle = pygame.image.load('skinny_triangle_triangle.png').convert_alpha()
skinny_triangle_triangle = pygame.transform.scale(skinny_triangle_triangle, (plane_width, plane_height))

skinny_wide_curve = pygame.image.load('skinny_wide_curve.png').convert_alpha()
skinny_wide_curve = pygame.transform.scale(skinny_wide_curve, (plane_width, plane_height))

skinny_wide_small = pygame.image.load('skinny_wide_small.png').convert_alpha()
skinny_wide_small = pygame.transform.scale(skinny_wide_small, (plane_width, plane_height))

skinny_wide_triangle = pygame.image.load('skinny_wide_triangle.png').convert_alpha()
skinny_wide_triangle = pygame.transform.scale(skinny_wide_triangle, (plane_width, plane_height))

#Plane Parts
wide_wing = pygame.image.load('wide_wing.png').convert_alpha()
wide_wing = pygame.transform.scale(wide_wing, (300, 175))

triangle_wing = pygame.image.load('triangle_wing.png').convert_alpha()
triangle_wing = pygame.transform.scale(triangle_wing, (300, 175))

small_wing = pygame.image.load('small_wing.png').convert_alpha()
small_wing = pygame.transform.scale(small_wing, (300, 175))

norm_body = pygame.image.load('norm_body.png').convert_alpha()
norm_body = pygame.transform.scale(norm_body, (175, 300))
norm_body = pygame.transform.rotate(norm_body, 90)

short_body = pygame.image.load('short_body.png').convert_alpha()
short_body = pygame.transform.scale(short_body, (175, 300))
short_body = pygame.transform.rotate(short_body, 90)

skinny_body = pygame.image.load('skinny_body.png').convert_alpha()
skinny_body = pygame.transform.scale(skinny_body, (175, 300))
skinny_body = pygame.transform.rotate(skinny_body, 90)

small_tail = pygame.image.load('small_tail.png').convert_alpha()
small_tail = pygame.transform.scale(small_tail, (300, 175))

curve_tail = pygame.image.load('curve_tail.png').convert_alpha()
curve_tail = pygame.transform.scale(curve_tail, (300, 175))

triangle_tail = pygame.image.load('triangle_tail.png').convert_alpha()
triangle_tail = pygame.transform.scale(triangle_tail, (300, 175))


#set ifCustom Var False
def setCustomFalse():
    global ifCustom
    ifCustom = False

questionAnswered = 0

#Set Difficulties

def setEasy():
    global difficulty
    global scoreMultiplyer
    scoreMultiplyer = 1
    difficulty = 40

def setMedium():
    global difficulty
    global scoreMultiplyer
    scoreMultiplyer = 2
    difficulty = 25

def setHard():
    global difficulty
    global scoreMultiplyer
    scoreMultiplyer = 3
    difficulty = 15

#Custom Plane Var
body = "norm"
wing = "wide"
tail = "curve"


updatedScore = False
#Win Var
ifWin = False
ifLose = False

def resetGame():
    global score
    global totalLives
    global ifWin
    global ifCustom
    global ifStart
    global question_Y
    global showQuestion
    global ifLose
    global questionAnswered
    questionAnswered = 0
    ifLose = False
    showQuestion = True
    question_Y = 200
    score = 0
    totalLives = 3
    ifWin = False
    ifCustom = True
    ifStart = True

def displayGameOver():
    global ifWin
    global isFiring
    global button
    global button2
    global button3
    global button4
    global confirmButton
    global ifLose 
    ifLose = True
    isFiring = False
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
    window.blit(text, (500-text.get_width()//2, 300))
    pygame.display.update()
    pygame.time.delay(1000)
    showQuestion = True

def setSettingFalse():
    global setting
    setting = False

def ifStartFalse():
    global ifStart
    ifStart = False
    global startButton
    startButton = 0

def setSetting():
    global settings
    global setting
    global startButton
    startButton = 0

    setting = True

    while setting:
        window.blit(bgImg2, (0,0))
        font = pygame.font.SysFont("Arial", 75)
        text = font.render("Choose your difficulty", True, (0,0,0))
        window.blit(text, (500-text.get_width()//2, 250))

        settings = Button(window, 30, 30, 115, 115, image = settingImg, colour=(0, 0, 0, 0),hoverColour=(0, 0, 0, 0), pressedColour=(0, 0, 0, 0), onClick=lambda: setSettingFalse())


        easy = Button(window, 100, 600, 200, 75, text='Easy', fontSize=30, margin=20, onClick=lambda: setEasy())
        medium = Button(window, 400, 600, 200, 75, text='Medium', fontSize=30, margin=20, onClick=lambda: setMedium())
        hard = Button(window, 700, 600, 200, 75, text='Hard', fontSize=30, margin=20, onClick=lambda: setHard())
        
        pygame_widgets.update(pygame.event.get())
        pygame.display.update()

    



def displayWrong():
    global showQuestion
    text = font.render('Wrong!', True, (255, 0, 0))
    window.blit(text, (500-text.get_width()//2, 300))
    pygame.display.update()
    pygame.time.delay(1000)
    showQuestion = True



cycle1 = 2

def drawFirstRect():
    global cycle1

    cycle1 += 1
    if cycle1 == 4:
        cycle1 = 1

cycle2 = 2

def drawSecRect():
    global cycle2

    cycle2 += 1
    if cycle2 == 4:
        cycle2 = 1

cycle3 = 2

def drawThirdRect():
    global cycle3

    cycle3 += 1
    if cycle3 == 4:
        cycle3 = 1


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
        window.blit(bgImg, (0,0))

        font = pygame.font.SysFont('Arial', 50)

        settingImg = pygame.image.load('settings.jpg').convert_alpha()
        settingImg = pygame.transform.scale(settingImg, (115, 115))

        settings = Button(window, 30, 30, 115, 115, image = settingImg, colour=(0, 0, 0, 0),hoverColour=(0, 0, 0, 0), pressedColour=(0, 0, 0, 0), onClick=lambda: setSetting())

        if setting == False:
            startButton = Button(window, 345, 715, 300, 95, text='Play!', fontSize=60, margin=20, inactiveColour=(203, 195, 227), hoverColour=(180, 170, 200), radius=20, onClick=lambda: ifStartFalse())
        else:
            startButton = Button(window, 0, 0, 0, 0,)
        area = pygame.Rect(25, 25, 125, 125)
        pygame.draw.rect(window, (255, 255, 255), area, 3)

        pygame_widgets.update(pygame.event.get())
        pygame.display.update()

        #Checking for Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                ifStart = False
                ifCustom = False
                ifQuestion = False

#Custom Screen for Plane
    while ifCustom:
        window.blit(bgImg2, (0,0))
        font = pygame.font.SysFont('Arial', 50)
        # pygame.draw.rect(window, (0,255,0), (75,100,450,800))

        #Drawing Buttons
        settings = 0
        button = Button(window, 912.5,225,75,75, text='>', fontSize=30, margin=20, onClick=lambda: drawFirstRect())
        button2 = Button(window, 912.5,450,75,75, text='>', fontSize=30, margin=20, onClick=lambda: drawSecRect())
        button3 = Button(window, 912.5,675,75,75, text='>', fontSize=30, margin=20, onClick=lambda: drawThirdRect())
        confirmButton = Button(window, 175,905,200,75, text="Confirm Plane", fontSize=30, margin=20, onClick=lambda: setCustomFalse())

        #Draw Custom Boxes for Diff Parts
        if cycle1 == 1:
            window.blit(wide_wing, (600,175))
            wing = "wide"
        elif cycle1 == 2:
            window.blit(triangle_wing, (600,175))
            wing = "triangle"
        elif cycle1 == 3:
            window.blit(small_wing, (600,175))
            wing = "small"

        if cycle2 == 1:
            window.blit(norm_body, (600,400))
            body = "norm"
        elif cycle2 == 2:
            window.blit(short_body, (600,400))
            body = "short"
        elif cycle2 == 3:
            window.blit(skinny_body, (600,400))
            body = "skinny"
        
        if cycle3 == 1:
            window.blit(small_tail, (600,625))
            tail = "small"
        elif cycle3 == 2:
            window.blit(curve_tail, (600,625))
            tail = "curve"
        elif cycle3 == 3:
            window.blit(triangle_tail, (600,625))
            tail = "triangle"

        plane1 = globals()[f"{body}_{wing}_{tail}"]
        plane1 = pygame.transform.scale(plane1, (450,800))
        window.blit(plane1, (50, 50))
        planeName = [f"{body}_{wing}_{tail}"]
        print(planeName)
        if planeName == ['skinny_triangle_triangle'] and updatedScore == False:
            scoreMultiplyer *= 2
            updatedScore = True

        print(scoreMultiplyer)

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
    if keys[pygame.K_SPACE] and isFiring == False and ifLose == False:  
        bullet_x = plane_x + (plane_width - bullet_width)/2
        isFiring = True
    if keys[pygame.K_t]:
        showQuestion = True
    

          
#White Background
    window.blit(bgImg2, (0,0))

#Check if Game Over
    if totalLives == 0 or score == 10:
        showQuestion = False

#Displaying Question
    if showQuestion and questionAnswered <= 10 and  ifLose == False:
        font = pygame.font.SysFont('Arial', 30)
        if newQuestion:
            randomQuestion = random.randint(0, len(questionDictionary)-1)
            questionText = font.render(list(questionDictionary.keys())[randomQuestion], True, (0, 0, 0))
            
            font = pygame.font.SysFont('Arial', 20)
            answer1 = font.render(str(questionDictionary[list(questionDictionary.keys())[randomQuestion]]), True, (0, 0, 0))
            answer2 = font.render(wrongAnswers1[randomQuestion], True, (0, 0, 0))
            answer3 = font.render(wrongAnswers2[randomQuestion], True, (0, 0, 0))

            del questionDictionary[list(questionDictionary.keys())[randomQuestion]]
            del wrongAnswers1[randomQuestion]
            del wrongAnswers2[randomQuestion]

            answerChoices = [answer1, answer2, answer3]
            random.shuffle(answerChoices)

            newQuestion = False
            questionAnswered += 1

        window.blit(questionText, (500-questionText.get_width()//2, 400))
        pygame.display.update()
        pygame.time.delay(5000)
        showQuestion = False

#Drawing Plane
    plane1 = pygame.transform.scale(plane1, (plane_width, plane_height))
    window.blit(plane1, (plane_x, plane_y))

#Drawing the 3 Possible Questions
    window.blit(cloudImg, (100, question_Y))
    window.blit(cloudImg, (400, question_Y))
    window.blit(cloudImg, (700, question_Y))

    window.blit(answerChoices[0], (100 + (question_width - answerChoices[0].get_width())//2, question_Y + (question_height - answerChoices[0].get_height())//2))
    window.blit(answerChoices[1], (400 + (question_width - answerChoices[1].get_width())//2, question_Y + (question_height - answerChoices[1].get_height())//2))
    window.blit(answerChoices[2], (700 + (question_width - answerChoices[2].get_width())//2, question_Y + (question_height - answerChoices[2].get_height())//2))

    if answerChoices[0] == answer1:
        rightAnswer = 1
    elif answerChoices[1] == answer1:
        rightAnswer = 2  
    else:
        rightAnswer = 3

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
    if questionAnswered >= 10:
        displayWin()

#Bulllet Drawing + Firing
    if isFiring and (bullet_y > 0):   
        window.blit(bullet, (bullet_x, bullet_y))
        bullet_y -= 10
    else:
        isFiring = False
        bullet_y = plane_y - 25

#Check Collision

    q1BoundaryLeft = (100 - bullet_width)
    q1BouondaryRight = (350 - bullet_width)

    q2BoundaryLeft = (400 - bullet_width)
    q2BouondaryRight = (650 - bullet_width)
                        
    q3BoundaryLeft = (700 - bullet_width)
    q3BoundaryRight = (950 - bullet_width)

    if bullet_y < (question_Y + 135) and (q1BoundaryLeft < bullet_x < q1BouondaryRight) and isFiring:
         q1Anwer = True
         isFiring = False
         checkAnswer = True
         newQuestion = True

    if bullet_y < (question_Y + 135) and (q2BoundaryLeft < bullet_x < q2BouondaryRight) and isFiring:
         q2Answer = True
         isFiring = False
         checkAnswer = True
         newQuestion = True

    if bullet_y < (question_Y + 135) and (q3BoundaryLeft < bullet_x < q3BoundaryRight) and isFiring:
         q3Answer = True
         isFiring = False
         checkAnswer = True
         newQuestion = True

    if (question_Y > 600) and (not ifWin):
        question_Y = 200
        showQuestion = True
        newQuestion = True
        totalLives -= 1

#Set Question Movement
    if q1Anwer or q2Answer or q3Answer:
        question_Y = 200
    else:
        question_Y += 2

#Check if Correct Answer
    if checkAnswer:
        if q1Anwer:
            if rightAnswer == 1:
                score += (1000 * scoreMultiplyer)
                displayCorrect()
            else:
                totalLives -= 1
                displayWrong()

        elif q2Answer:
            if rightAnswer == 2:
                score += (1000 * scoreMultiplyer)
                displayCorrect()
            else:
                totalLives -= 1
                displayWrong()
        else:
            if rightAnswer == 3:
                score += (1000 * scoreMultiplyer)
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