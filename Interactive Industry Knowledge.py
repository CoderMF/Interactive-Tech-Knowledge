from pygame import * 
import os
import random
#moving screen to top left corner
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 20)
init()

size = 1000, 700
screen = display.set_mode(size)

#colours
BLACK = (0, 0, 0)
WHITE = (255,255,255)
PASTELRED = (255,153,153)
PASTELPURPLE = (204,153,255)
PASTELGREEN = (102, 255,178)
DEEPBLUE = (0,0,102)
STRONGTEAL = (0,128,255)
PASTELYELLOW = (255,255,102)
#randomizing colours
RAND1 = random.randint (0,255)
RAND2 = random.randint (0,255)
RAND3 = random.randint (0,255)
RANDOM = (RAND1,RAND2,RAND3)

# define states
STATEMENU = 0
STATEAI   = 1
STATECITY = 2
STATENANO = 3
STATEQUIT = 4
STATEAITREND1 = 5
STATEAITREND2 = 6
STATEAITREND3 = 7
STATENANOTREND1 = 8
STATENANOTREND2 = 9
STATENANOTREND3 = 10
STATECITYTREND1 = 11
STATECITYTREND2 = 12
STATECITYTREND3 = 13
STATEBALLRIGHT = 14
STATEBALLLEFT = 15
STATEBALLSTOP = 16

#fonts
Modern = font.SysFont("Modern No. 20",60)
Heading = font.SysFont("Modern No. 20",75)
ModernSubHeading = font.SysFont("Modern No. 20",50)
ModernWriting = font.SysFont("Modern No. 20",26)

# initial states
state = STATEMENU
subState = STATEAI
ballState = STATEBALLSTOP
ballState2 = STATEBALLSTOP
ballState3 = STATEBALLSTOP

#images
   #load menu page background
mainBackdrop = image.load ("mainback.jpg")
   #scaling the image to fit the screen
mainBackdrop = transform.scale (mainBackdrop,[1000,700])
   #load spotify logo
spotify = image.load ("spotify.jpg")
   #scaling the image to fit the screen
spotify = transform.scale (spotify,[150,100])
   #load drone delivering
drone1 = image.load ("drone1.jpg")
   #scaling the image to fit the screen
drone1 = transform.scale (drone1,[125,100])
   #load cyber security image
cyber = image.load ("cyber.jpg")
   #scaling the image to fit the screen
cyber = transform.scale (cyber,[150,100])
   #load smart car image
car = image.load ("car.jpg")
   #scaling the image to fit the screen
car = transform.scale (car,[150,100])
   #load smart data image
data = image.load ("data.png")
   #scaling the image to fit the screen
data = transform.scale (data,[175,120])
   #load smart dashboard image
dashboard = image.load ("dashboard.jpg")
   #scaling the image to fit the screen
dashboard = transform.scale (dashboard,[175,120])
   #load smart grids image
grid = image.load ("grid.jpg")
   #scaling the image to fit the screen
grid = transform.scale (grid,[150,120])
   #load smart grids image
solar = image.load ("solar.jpg")
   #scaling the image to fit the screen
solar = transform.scale (solar,[150,100])
   #load nanobots in bloodstream image
bot = image.load ("bot.jpg")
   #scaling the image to fit the screen
bot = transform.scale (bot,[200,150])
   #load nanobots in bloodstream image
graph = image.load ("graph1.jpg")
   #scaling the image to fit the screen
graph = transform.scale (graph,[275,200])
   #load nanotechnology laser image
laser = image.load ("laser.jpg")
   #scaling the image to fit the screen
laser = transform.scale (laser,[225,125])
   #load nanobomb image
bomb = image.load ("bomb.jpg")
   #scaling the image to fit the screen
bomb = transform.scale (bomb,[225,125])
   #load AI image
AI = image.load ("AI.jpg")
   #scaling the image to fit the screen
AI = transform.scale (AI,[225,125])
   #load AI image
nano = image.load ("nano.jpg")
   #scaling the image to fit the screen
nano = transform.scale (nano,[225,125])
   #load AI image
city = image.load ("city.jpg")
   #scaling the image to fit the screen
city = transform.scale (city,[225,125])

#creating the menu page
def drawScene(screen, curState,curSubState):
    #if the current state of the program is the menu page then options for information will show up (the current state is the menu page)
    if curState == STATEMENU:
        #picture as background
        screen.blit (mainBackdrop, Rect (0,0,1000,700))
        #AI button
        draw.rect (screen, DEEPBLUE, (250,150,450,75))
            # Setting up the AI Text
        text1 = Modern.render("AI", 1, PASTELPURPLE) 
            # getting the width of the text
        text1Width = Modern.size("AI")[0] 
            # getting the height of the text
        text1Height = Modern.size("AI")[1] 
            # blitting "AI" to the screen
        screen.blit(text1, Rect(175 + (600 - text1Width)/2, 150 + (80 - text1Height)/2, text1Width, text1Height)) 
        
        #Nanotechnology Button
        draw.rect (screen, DEEPBLUE, (250,275,450,75))
            # Setting up the Nanotechnology Text
        text1 = Modern.render("Nanotechnology", 1, PASTELRED) 
            # getting the width of the text
        text1Width = Modern.size("Nanotechnology")[0]
            # getting the height of the text
        text1Height = Modern.size("NanoTechnology")[1] 
            # blitting "Nanotechnology" to the screen
        screen.blit(text1, Rect(175 + (600 - text1Width)/2, 275 + (80 - text1Height)/2, text1Width, text1Height))
        
        #Smart Cities Button
        draw.rect (screen, DEEPBLUE, (250,400,450,75))
            # Setting up the Smart Cities Text
        text1 = Modern.render("Smart Cities", 1, PASTELGREEN) 
            # getting the width of the text
        text1Width = Modern.size("Smart Cities")[0] 
            # getting the height of the text
        text1Height = Modern.size("Smart Cities")[1] 
            # blitting "Smart Cities" to the screen
        screen.blit(text1, Rect(175 + (600 - text1Width)/2, 400 + (80 - text1Height)/2, text1Width, text1Height))         
        
        #Quit Button
        draw.rect (screen, DEEPBLUE, (250,525,450,75)) 
            # Setting up the Quit Text
        text1 = Modern.render("Quit", 1, WHITE) 
            # getting the width of the text
        text1Width = Modern.size("Quit")[0] 
            # getting the height of the text
        text1Height = Modern.size("Quit")[1] 
            # blitting "Quit" to the screen
        screen.blit(text1, Rect(175 + (600 - text1Width)/2, 525 + (80 - text1Height)/2, text1Width, text1Height)) 
        #Virus
        screen.blit (AI,Rect (posx,posy,(posx+225),(posy+125))) 
        screen.blit (nano,Rect (posx2,posy2,(posx2+225),(posy2+125)))
        screen.blit (city,Rect (posx3,posy3,(posx3+225),(posy3+125)))
    #if the user clicks on the AI Button, info about AI will show up    
    elif state == STATEAI:
        screen.fill (PASTELPURPLE)
        #top bar
        draw.rect (screen,STRONGTEAL,(0,0,1000,125))
        #Back button
        draw.rect (screen,WHITE,(325,50,150,50))
            # Setting up the Back Text
        text1 = ModernSubHeading.render("Back", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Back")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Back")[1]
            # blitting "Back" to the screen
        screen.blit(text1, Rect(325 + (150 - text1Width)/2, 50 + (50 - text1Height)/2, text1Width, text1Height))   
        
        #Quit button
        draw.rect (screen,WHITE, (625,50,150,50))
            # Setting up the Quit Text
        text1 = ModernSubHeading.render("Quit", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Quit")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Quit")[1]
            # blitting "Quit" to the screen
        screen.blit(text1, Rect(625 + (150 - text1Width)/2, 50 + (50 - text1Height)/2, text1Width, text1Height)) 
        
        #SIDE bar 
        draw.rect (screen, PASTELYELLOW, (0,0,200,700))  
        #Trend 1
        draw.rect (screen, WHITE, (25,225,150,50))
            # Setting up the Trend 1 Text
        text1 = ModernSubHeading.render("Trend 1", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Trend 1")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Trend 1")[1]
            # blitting "Trend 1" to the screen
        screen.blit(text1, Rect(25 + (150 - text1Width)/2, 225 + (50 - text1Height)/2, text1Width, text1Height))
        
        #Trend 2
        draw.rect (screen, WHITE, (25,375,150,50))
           # Setting up the Trend 2 Text
        text1 = ModernSubHeading.render("Trend 2", 1, RANDOM)
           # getting the width of the text
        text1Width = ModernSubHeading.size("Trend 2")[0]
           # getting the height of the text
        text1Height = ModernSubHeading.size("Trend 2")[1]
           # blitting "Trend 2" to the screen
        screen.blit(text1, Rect(25 + (150 - text1Width)/2, 375 + (50 - text1Height)/2, text1Width, text1Height))
        
        #Trend 3
        draw.rect (screen,WHITE, (25,525,150,50))
            # Setting up the Trend 1 Text
        text1 = ModernSubHeading.render("Trend 3", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Trend 1")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Trend 1")[1]
            # blitting "Trend 3" to the screen
        screen.blit(text1, Rect(25 + (150 - text1Width)/2, 525 + (50 - text1Height)/2, text1Width, text1Height))   
        
        #once on AI page, user has 3 options to choose from
            # If user chooses the first trend/button on AI page:
        if curSubState == STATEAITREND1:
            text11 = Heading.render("AI in Music",1,BLACK)
            text1 = ModernWriting.render("AI has come a far way when it comes to the music industry. In fact, AI can already",1,BLACK)
            text2 = ModernWriting.render ("analyze music well enough to create its own human-inspired sonds. It is ",1,BLACK)
            text3 = ModernWriting.render ("predicted that computers can break down music to its components then analyze",1,BLACK)
            text4 = ModernWriting.render ("those components to find similar music in the future.",1,BLACK)
            text5 = ModernWriting.render ("Spotify is already ahead of the game. It uses a simple AI",1,BLACK)
            text6 = ModernWriting.render ("by having weekly personalized playlists for every user.",1,BLACK) 
            text7 = ModernWriting.render ("They present new releases of artists they have",1,BLACK)
            text8 = ModernWriting.render ("currently listens to. As a result, this causes these",1,BLACK)
            text9 = ModernWriting.render ("algorithms to become more human-like and more friendly ",1,BLACK)
            text10 = ModernWriting.render ("to both the users and the programmers.", 1,BLACK)
                # blitting info on trend 1 to the screen
            screen.blit(text1, Rect(275, 250, 350, 50))
            screen.blit (text2, Rect (275,275,350,50))
            screen.blit (text3, Rect (275,300,350,50))
            screen.blit (text4, Rect (275,325,350,50))
            screen.blit (text5, Rect (275,400,350,50))
            screen.blit (text6, Rect (275,425,350,50))
            screen.blit (text7, Rect (275,450,350,50))
            screen.blit (text8, Rect (275,475,350,50))
            screen.blit (text9, Rect (275,500,350,50))
            screen.blit (text10, Rect (275,525,350,50))
            screen.blit (text11, Rect (450,175,350,100))
            screen.blit (spotify, Rect (780,425,100,100))
            # if user chooses the second trend/button on AI page:
        elif curSubState == STATEAITREND2:
            text13 = Heading.render ("Security",1,BLACK)
            text1 = ModernWriting.render("     With advancement of drones, there is an opportunity to do more routine checks ",1,BLACK)
            text2 = ModernWriting.render("where it is normally difficult for humans to go to. In current day and age, ",1,BLACK)
            text3 = ModernWriting.render("drones allow easy transport over short distances and complex spaces. As a result,",1,BLACK)
            text4 = ModernWriting.render("this will allow more secure areas and even fewer thefts.",1,BLACK)
            text5 = ModernWriting.render("    In the future, AIs will specifically target on increasing and improving  ",1,BLACK)
            text6 = ModernWriting.render("cybersecurity. AI helps by automating complex processes for detecting attacks and ",1,BLACK)
            text7 = ModernWriting.render("reacting to breaches. These applications are becoming more sophisticated as AI is ",1,BLACK)
            text8 = ModernWriting.render("deployed for security. Additionally, data deception technology products can",1,BLACK)
            text9 = ModernWriting.render("automatically detect, analyze, and defend against advanced attacks by proactively", 1,BLACK)
            text10 = ModernWriting.render("detecting and tricking attackers. Currently, these cybersecurity technologies have",1,BLACK)
            text11 = ModernWriting.render("been absent however, once this is inputted, it will provide a competitive edge to",1,BLACK)
            text12 = ModernWriting.render("companies and even people protecting their data and secrets.",1,BLACK)
                # blitting info on trend 2 to the screen
            screen.blit (text1, Rect(275, 250, 350, 50))
            screen.blit (text2, Rect (275,275,350,50))
            screen.blit (text3, Rect (275,300,350,50))
            screen.blit (text4, Rect (275,325,350,50))
            screen.blit (text5, Rect (275,475,350,50))
            screen.blit (text6, Rect (275,500,350,50))
            screen.blit (text7, Rect (275,525,350,50))
            screen.blit (text8, Rect (275,550,350,50))
            screen.blit (text9, Rect (275,575,350,50))
            screen.blit (text10, Rect (275,600,350,50))
            screen.blit (text11, Rect (275,625,350,50))
            screen.blit (text12, Rect (275,650,350,50)) 
            screen.blit (text13, Rect (475,175,350,100))
            screen.blit (drone1, Rect (450,360,125,100))
            screen.blit (cyber, Rect (600,360,100,200))
            #if user chooses the third trend/button on AI page:
        elif curSubState == STATEAITREND3:
            text14 = Heading.render ("Productivity",1,BLACK)
            text1 = ModernWriting.render("     Many think that AI will replace many professions in all industries or significantly ",1,BLACK)
            text2 = ModernWriting.render("impact the industry making it difficult for people to keep up. This is a recurring ",1,BLACK)
            text3 = ModernWriting.render("misinterpretation that occurs when technology is involved. The Department of ",1,BLACK)
            text4 = ModernWriting.render("Labour collected a Dataset called ONET. While there are many tasks the AI do,",1,BLACK)
            text5 = ModernWriting.render("perform better in there were still plenty of tasks that humans excelled at over",1,BLACK)
            text6 = ModernWriting.render("AI and machine learning.",1,BLACK)
            text7 = ModernWriting.render("     In most cases, AIs will only allow people to focus more on the creative ",1,BLACK)
            text8 = ModernWriting.render("aspect of a project rather than putting more effort with tenuous or tedious task",1,BLACK)
            text9 = ModernWriting.render("could be automotive. This will reduce human errors enhancing not only economic",1,BLACK)
            text10 = ModernWriting.render("growth but also productivity within the firm or economy. Additionally, there will",1,BLACK)
            text11 = ModernWriting.render("be an increase in communication due to AI. For a successful company, a strong",1,BLACK)
            text12 = ModernWriting.render("support system is needed. AIs will provide more smooth transitions between ",1,BLACK)
            text13 = ModernWriting.render("different levels of the company without the risk of security breaches.",1,BLACK) 
                # blitting info on trend 2 to the screen
            screen.blit (text1, Rect(275, 250, 350, 50))
            screen.blit (text2, Rect (275,275,350,50))
            screen.blit (text3, Rect (275,300,350,50))
            screen.blit (text4, Rect (275,325,350,50))
            screen.blit (text5, Rect (275,350,350,50))
            screen.blit (text6, Rect (275,375,350,50))
            screen.blit (text7, Rect (275,425,350,50))
            screen.blit (text8, Rect (275,450,350,50))
            screen.blit (text9, Rect (275,475,350,50))
            screen.blit (text10, Rect (275,500,350,50))
            screen.blit (text11, Rect (275,525,350,50))
            screen.blit (text12, Rect (275,550,350,50))                        
            screen.blit (text13, Rect (275,575,350,50))
            screen.blit (text14, Rect (460,175,350,100))
            
    #if the user clicks on the "Nanotechnology" Button, info about Nanotechnology will show up 
    elif state == STATENANO:
        screen.fill (PASTELRED)
        #top bar
        draw.rect (screen,STRONGTEAL,(0,0,1000,125))
                #Back button
        draw.rect (screen,WHITE,(325,50,150,50))
            # Setting up the Back Text
        text1 = ModernSubHeading.render("Back", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Back")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Back")[1]
            # blitting "Back" to the screen
        screen.blit(text1, Rect(325 + (150 - text1Width)/2, 50 + (50 - text1Height)/2, text1Width, text1Height))   
        
        #Quit button
        draw.rect (screen,WHITE, (625,50,150,50))
            # Setting up the Quit Text
        text1 = ModernSubHeading.render("Quit", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Quit")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Quit")[1]
            # blitting "Quit" to the screen
        screen.blit(text1, Rect(625 + (150 - text1Width)/2, 50 + (50 - text1Height)/2, text1Width, text1Height)) 
        
        #SIDE bar 
        draw.rect (screen, PASTELYELLOW, (0,0,200,700))  
        #Trend 1
        draw.rect (screen, WHITE, (25,225,150,50))
            # Setting up the Trend 1 Text
        text1 = ModernSubHeading.render("Trend 1", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Trend 1")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Trend 1")[1]
            # blitting "Trend 1" to the screen
        screen.blit(text1, Rect(25 + (150 - text1Width)/2, 225 + (50 - text1Height)/2, text1Width, text1Height))
        
        #Trend 2
        draw.rect (screen, WHITE, (25,375,150,50))
           # Setting up the Trend 2 Text
        text1 = ModernSubHeading.render("Trend 2", 1, RANDOM)
           # getting the width of the text
        text1Width = ModernSubHeading.size("Trend 2")[0]
           # getting the height of the text
        text1Height = ModernSubHeading.size("Trend 2")[1]
           # blitting "Trend 2" to the screen
        screen.blit(text1, Rect(25 + (150 - text1Width)/2, 375 + (50 - text1Height)/2, text1Width, text1Height))
        
        #Trend 3
        draw.rect (screen,WHITE, (25,525,150,50))
            # Setting up the Trend 1 Text
        text1 = ModernSubHeading.render("Trend 3", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Trend 1")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Trend 1")[1]
            # blitting "Trend 3" to the screen
        screen.blit(text1, Rect(25 + (150 - text1Width)/2, 525 + (50 - text1Height)/2, text1Width, text1Height))
        
        # Once on Nanotechnology page, user has 3 options to choose from
            # If user chooses the first trend/button on Nanotechnology page:        
        if curSubState == STATENANOTREND1:
            text14 = Heading.render ("Nanobots in Medicine",1,BLACK)
            text1 = ModernWriting.render ("     Although nanobots do not yet exist, there is a possibility that it could be",1,BLACK)
            text2 = ModernWriting.render ("used for medicinal purposes. According to IFL Science, DNA robots are already being",1,BLACK)
            text3 = ModernWriting.render ("tested on humans to seek and destroy cancer cells. If the trials go well, these",1,BLACK)
            text4 = ModernWriting.render ("could become revolutionary to cancer and other cell research. Theoretically, ",1,BLACK)
            text5 = ModernWriting.render ("nanobots could be used to constantly monitor our ",1,BLACK)
            text6 = ModernWriting.render ("body for diseases by continuously transmitting ",1,BLACK)
            text7 = ModernWriting.render ("information to a cloud where medical staff monitor ",1,BLACK)
            text8 = ModernWriting.render ("it closely. By using this cloud, they can easily ",1,BLACK)
            text9 = ModernWriting.render ("prevent fatal illnesses fromoccurring. However, a ",1,BLACK)
            text10 = ModernWriting.render ("cloud is something far into the future ascurrently,",1,BLACK)
            text11 = ModernWriting.render ("engineers are focusing on developing nanobots first.",1,BLACK)
            text12 = ModernWriting.render ("     Nanobots are also predicted to soon deliver drugs to humans with much accuracy.",1,BLACK)
            text13 = ModernWriting.render ("So accurate that the patient could potentially prevent harmful side effects.",1,BLACK)
                #blitting trend 1 onto the screen
            screen.blit (text1, Rect(275, 250, 350, 50))
            screen.blit (text2, Rect (275,275,350,50))
            screen.blit (text3, Rect (275,300,350,50))
            screen.blit (text4, Rect (275,325,350,50))
            screen.blit (text5, Rect (275,350,350,50))
            screen.blit (text6, Rect (275,375,350,50))
            screen.blit (text7, Rect (275,400,350,50))
            screen.blit (text8, Rect (275,425,350,50))
            screen.blit (text9, Rect (275,450,350,50))
            screen.blit (text10, Rect (275,475,350,50))
            screen.blit (text11, Rect (275,500,350,50))
            screen.blit (text12, Rect (275,550,350,50))
            screen.blit (text13, Rect (275,575,350,50))
            screen.blit (text14, Rect (350,175,350,100)) 
            screen.blit (bot, Rect (730,360,100,100))
            # if user chooses the second trend/button on Nanotechnology page:
        elif curSubState == STATENANOTREND2:
            text13 = Heading.render ("NanoTech Weapons",1,BLACK)
            text1 = ModernWriting.render ("     Nanotechnology is not difficult to acquire. Many countries such as Mexico,",1,BLACK)
            text2 = ModernWriting.render ("Thailand and China are heavily investing in nanotechnology industries. This could",1,BLACK)
            text3 = ModernWriting.render ("serve as a potential game changer in the military sector. Militaries can use",1,BLACK)
            text4 = ModernWriting.render ("nanotech for concepts such as clothing with a large range of climate control, ",1,BLACK)
            text5 = ModernWriting.render ("lighter and faster aircrafts that require less fuel. Currently, the DoD ",1,BLACK) 
            text6 = ModernWriting.render ("(Department of Defense) are developing weaponry such as compact, powerful",1,BLACK)
            text7 = ModernWriting.render ("bombs that use nanometals to cause ultra-high burn rates and chemical explosives",1,BLACK)
            text8 = ModernWriting.render ("more powerful than conventional bombs. Other advancements include super lasers",1,BLACK)
            text9 = ModernWriting.render ("that could potentially trigger small thermonuclear fusion explosions which will",1,BLACK)
            text10 = ModernWriting.render ("be untraceable due to its miniscule size. Jurgen Altmann, a professor at the ",1,BLACK)
            text11 = ModernWriting.render ("University of Dortmund, Germany emphasized the need for preventive control",1,BLACK)
            text12 = ModernWriting.render ("taken in advance of dangerous development.",1,BLACK)
                #blitting trend 2 onto the screen
            screen.blit (text1, Rect(275, 250, 350, 50))
            screen.blit (text2, Rect (275,275,350,50))
            screen.blit (text3, Rect (275,300,350,50))
            screen.blit (text4, Rect (275,325,350,50))
            screen.blit (text5, Rect (275,350,350,50))
            screen.blit (text6, Rect (275,375,350,50))
            screen.blit (text7, Rect (275,400,350,50))
            screen.blit (text8, Rect (275,425,350,50))
            screen.blit (text9, Rect (275,450,350,50))
            screen.blit (text10, Rect (275,475,350,50))
            screen.blit (text11, Rect (275,500,350,50))
            screen.blit (text12, Rect (275,525,350,50))
            screen.blit (text13, Rect (350,175,350,100))   
            screen.blit (laser, Rect (350,550,100,100))
            screen.blit (bomb, Rect (650,550,100,100))

            # if user chooses the third trend/button on Nanotechnology page:
        elif curSubState == STATENANOTREND3:
            text14 = Heading.render ("Nanopollutants",1,BLACK)
            text1 = ModernWriting.render ("     These are small enough to enter your lungs or can even be absorbed by the skin. ",1,BLACK)
            text2 = ModernWriting.render ("At the moment, there is little to no nanopollutants in the atmosphere as engineers",1,BLACK)
            text3 = ModernWriting.render (" are still in the developmental stage of nanotechnology. However, once usage will  ",1,BLACK)
            text4 = ModernWriting.render ("become more common, it is predicted that there will be a sharp incline of pollution ",1,BLACK)
            text5 = ModernWriting.render ("in the already polluted environment. The health effects of it are yet to be ",1,BLACK)
            text6 = ModernWriting.render ("understood although it is thought to be deadly if too much is absorbed.",1,BLACK)
            text7 = ModernWriting.render ("     In this graph, it is shown that the usage",1,BLACK)
            text8 = ModernWriting.render ("is only increasing at an upwards slope and will",1,BLACK)
            text9 = ModernWriting.render ("soon open to mass market in the near future ",1,BLACK)
            text10 = ModernWriting.render ("(estimated to occur around 2020). When it ",1,BLACK)
            text11 = ModernWriting.render ("enters the mass market, there will be an  ",1,BLACK)
            text12 = ModernWriting.render ("increase in usage resulting to ultimately, an",1,BLACK)
            text13 = ModernWriting.render ("increase in nanopollution.",1,BLACK)
                #blitting trend 3 onto the screen
            screen.blit (text1, Rect(275, 250, 350, 50))
            screen.blit (text2, Rect (275,275,350,50))
            screen.blit (text3, Rect (275,300,350,50))
            screen.blit (text4, Rect (275,325,350,50))
            screen.blit (text5, Rect (275,350,350,50))
            screen.blit (text6, Rect (275,375,350,50))
            screen.blit (text7, Rect (275,450,350,50))
            screen.blit (text8, Rect (275,475,350,50))
            screen.blit (text9, Rect (275,500,350,50))
            screen.blit (text10, Rect (275,525,350,50))
            screen.blit (text11, Rect (275,550,350,50))
            screen.blit (text12, Rect (275,575,350,50))  
            screen.blit (text13, Rect (275,600,350,50))
            screen.blit (text14, Rect (400,175,350,100))
            screen.blit (graph, Rect (675,445,100,100))
            
    #if the user clicks on the "Smart Cities" Button, info about Smart Cities will show up 
    elif state == STATECITY:
        screen.fill (PASTELGREEN)
        #top bar
        draw.rect (screen,STRONGTEAL,(0,0,1000,125))
                #Back button
        draw.rect (screen,WHITE,(325,50,150,50))
            # Setting up the Back Text
        text1 = ModernSubHeading.render("Back", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Back")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Back")[1]
            # blitting "Back" to the screen
        screen.blit(text1, Rect(325 + (150 - text1Width)/2, 50 + (50 - text1Height)/2, text1Width, text1Height))   
        
        #Quit button
        draw.rect (screen,WHITE, (625,50,150,50))
            # Setting up the Quit Text
        text1 = ModernSubHeading.render("Quit", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Quit")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Quit")[1]
            # blitting "Quit" to the screen
        screen.blit(text1, Rect(625 + (150 - text1Width)/2, 50 + (50 - text1Height)/2, text1Width, text1Height)) 
        
        #SIDE bar 
        draw.rect (screen, PASTELYELLOW, (0,0,200,700))  
        #Trend 1
        draw.rect (screen, WHITE, (25,225,150,50))
            # Setting up the Trend 1 Text
        text1 = ModernSubHeading.render("Trend 1", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Trend 1")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Trend 1")[1]
            # blitting "Trend 1" to the screen
        screen.blit(text1, Rect(25 + (150 - text1Width)/2, 225 + (50 - text1Height)/2, text1Width, text1Height))

        #Trend 2
        draw.rect (screen, WHITE, (25,375,150,50))
           # Setting up the Trend 2 Text
        text1 = ModernSubHeading.render("Trend 2", 1, RANDOM)
           # getting the width of the text
        text1Width = ModernSubHeading.size("Trend 2")[0]
           # getting the height of the text
        text1Height = ModernSubHeading.size("Trend 2")[1]
           # blitting "Trend 2" to the screen
        screen.blit(text1, Rect(25 + (150 - text1Width)/2, 375 + (50 - text1Height)/2, text1Width, text1Height))
        
        #Trend 3
        draw.rect (screen,WHITE, (25,525,150,50))
            # Setting up the Trend 1 Text
        text1 = ModernSubHeading.render("Trend 3", 1, RANDOM)
            # getting the width of the text
        text1Width = ModernSubHeading.size("Trend 1")[0]
            # getting the height of the text
        text1Height = ModernSubHeading.size("Trend 1")[1]
            # blitting "Trend 3" to the screen
        screen.blit(text1, Rect(25 + (150 - text1Width)/2, 525 + (50 - text1Height)/2, text1Width, text1Height))  
        
        # Once on Smart Cities page, user has 3 options to choose from
            # If user chooses the first trend/button on Smart Cities page:         
        if curSubState == STATECITYTREND1:
            text11 = Heading.render ("Smart Data",1,BLACK)
            text1 = ModernWriting.render ("     There are 1.3 million people moving into cities each week, and by 2040, 65% of ",1,BLACK)
            text2 = ModernWriting.render ("the world's population is expected to be living in cities, with 90% of this urban",1,BLACK)
            text3 = ModernWriting.render ("population growth set to occur in Africa and Asia. To help combat this, data will",1,BLACK)
            text4 = ModernWriting.render ("always be collected and used to assess patterns and inefficiencies to improve living",1,BLACK)
            text5 = ModernWriting.render ("standards. Ultimately, it will improve city operations and enhance city services",1,BLACK)
            text6 = ModernWriting.render ("     For example, a display on your dashboard alerts that weather has made the ",1,BLACK)
            text7 = ModernWriting.render ("route chosen less favourable. It will then recalculate your route to meet",1,BLACK)
            text8 = ModernWriting.render ("optimal conditions. Once arrived, it can alert you of the nearest parking space.",1,BLACK)
            text9 = ModernWriting.render ("Already several cities are adopting Big Data technologies as shown through single-",1,BLACK)
            text10 = ModernWriting.render ("purpose applications such as smart street lighting.",1,BLACK)
                # blitting info on trend 2 to the screen
            screen.blit (text1, Rect(275, 250, 350, 50))
            screen.blit (text2, Rect (275,275,350,50))
            screen.blit (text3, Rect (275,300,350,50))
            screen.blit (text4, Rect (275,325,350,50))
            screen.blit (text5, Rect (275,350,350,50))
            screen.blit (text6, Rect (275,500,350,50))
            screen.blit (text7, Rect (275,525,350,50))
            screen.blit (text8, Rect (275,550,350,50))
            screen.blit (text9, Rect (275,600,350,50))
            screen.blit (text10, Rect (275,625,350,50))
            screen.blit (text11, Rect (460,175,350,100))
            screen.blit (data, Rect (400,375,175,125))
            screen.blit (dashboard, Rect (600,375,175,125))
            
            # if user chooses the third trend/button on Smart Cities page:
        elif curSubState == STATECITYTREND2:
            text15 = Heading.render ("Smart Transportation",1,BLACK)
            text1 = ModernWriting.render("     One of the many challenges that cities face is traffic congestion and immobility. ",1,BLACK)
            text2 = ModernWriting.render("Congestion impacts everyone including commuters,companies and tourists. Smart",1,BLACK)
            text3 = ModernWriting.render("Parking is one way to make drivers'' lives easier when finding free parking spots.",1,BLACK)
            text4 = ModernWriting.render("Smart Parking services are able to significantly ease these problems by guiding a ",1,BLACK)
            text5 = ModernWriting.render("driver directly to a parking space. China is already ahead of the game by partnering ",1,BLACK)
            text6 = ModernWriting.render("up with DTMobile. They have initiated two separate smart parking pilots using the ",1,BLACK)
            text7 = ModernWriting.render("Internet of things (NB-IoT) connectivity. It has a long battery life and offers ",1,BLACK)
            text8 = ModernWriting.render("improved coverage allowing for sensors to be placed in any location. Their solution",1,BLACK)
            text9 = ModernWriting.render("also covers license plate recognition, mobile payments, and parking guidance ",1,BLACK)
            text10 = ModernWriting.render("for drivers.",1,BLACK)
            text11 = ModernWriting.render("     A future of driverless cars are starting to become a reality. Fully autonomous ",1,BLACK)
            text12 = ModernWriting.render("vehicles that can communicate with surrounding vehicles and streets. These  ",1,BLACK)
            text13 = ModernWriting.render("vehicles promise increased safety, reduced emissions and  ",1,BLACK)
            text14 = ModernWriting.render ("a potentially streamlined public transportation.",1,BLACK)
                # blitting info on trend 2 to the screen
            screen.blit (text1, Rect(275, 250, 350, 50))
            screen.blit (text2, Rect (275,275,350,50))
            screen.blit (text3, Rect (275,300,350,50))
            screen.blit (text4, Rect (275,325,350,50))
            screen.blit (text5, Rect (275,350,350,50))
            screen.blit (text6, Rect (275,375,350,50))
            screen.blit (text7, Rect (275,400,350,50))
            screen.blit (text8, Rect (275,425,350,50))
            screen.blit (text9, Rect (275,450,350,50))
            screen.blit (text10, Rect (275,475,350,50))
            screen.blit (text11, Rect (275,525,350,50))
            screen.blit (text12, Rect (275,550,350,50))             
            screen.blit (text13, Rect (275,575,350,50)) 
            screen.blit (text14, Rect (275,600,350,50))
            screen.blit (text15, Rect (325,175,350,100))
            screen.blit (car, Rect (780,575,125,100))
            # if user chooses the third trend/button on Smart Cities page:
        elif curSubState == STATECITYTREND3:
            text14 = Heading.render ("Smart Energy",1,BLACK)
            text1 = ModernWriting.render ("     The world will reach a point of no return if we do not shrink our carbon ",1,BLACK)
            text2 = ModernWriting.render ("footprint and waste energy. To tackle the situation smart cities can become",1,BLACK)
            text3 = ModernWriting.render ("a zero emission city. This means the city runs completely on renewable",1,BLACK)
            text4 = ModernWriting.render ("resources. As a result, there will be no carbon footprint and greenhouse",1,BLACK)
            text5 = ModernWriting.render ("gases will reduce substantially. In the future, solar energy will be the",1,BLACK)
            text6 = ModernWriting.render ("most common renewable resource used. This is due to easy maintenance and",1,BLACK)
            text7 = ModernWriting.render ("the never-ending supply of power. In India, it has already been mandated that",1,BLACK)
            text8 = ModernWriting.render ("10% of smart cities' energy requirement must come from solar power." ,1,BLACK)
            text9 = ModernWriting.render ("     Another useful way to conserve energy are Smart grids.   ",1,BLACK)
            text10 = ModernWriting.render ("Smart Grids are electrical supply networks that uses ",1,BLACK)
            text11 = ModernWriting.render ("digital communications technology to detect and react to local  ",1,BLACK)
            text12 = ModernWriting.render ("changes in usage. Ultimately, this increases the intelligence ",1,BLACK)
            text13 = ModernWriting.render ("of infrastructure bettering the quality of life.",1,BLACK)
                # blitting info on trend 2 to the screen
            screen.blit (text1, Rect(275, 250, 350, 50))
            screen.blit (text2, Rect (275,275,350,50))
            screen.blit (text3, Rect (275,300,350,50))
            screen.blit (text4, Rect (275,325,350,50))
            screen.blit (text5, Rect (275,350,350,50))
            screen.blit (text6, Rect (275,375,350,50))
            screen.blit (text7, Rect (275,400,350,50))
            screen.blit (text8, Rect (275,425,350,50))
            screen.blit (text9, Rect (275,550,350,50))
            screen.blit (text10, Rect (275,575,350,50))
            screen.blit (text11, Rect (275,600,350,50))
            screen.blit (text12, Rect (275,625,350,50)) 
            screen.blit (text13, Rect (275,650,350,50))
            screen.blit (text14, Rect (420,175,350,100))
            screen.blit (grid, Rect (800,560,100,100))
            screen.blit (solar, Rect (450,450,125,100))
    display.flip()
    
#once in a state, there will be options presented to find more information about the technology
def changeSubState (button, mousex, mousey, curState,curSubState):
    #occurs if the user presses the mouse button down
    if button == 1:
        # if the user chooses to read about AI 
        if curState == STATEAI:
            # gives the x coordinate range for all three buttons
            if 25 <= mousex <= 175:
                #gives the y coordinate range for the first button. If true, then user will find infomartion on the first trend
                if 225 <= mousey <= 275:
                    curSubState = STATEAITREND1                    
                #gives the y coordinate range for the second button. If true, then user will find infomartion on the second trend
                elif 375 <= mousey <= 425:
                    curSubState = STATEAITREND2
                #gives the y coordinate range for the third button. If true, then user will find infomartion on the third trend
                elif 525 <= mousey <= 575:
                    curSubState = STATEAITREND3
        
        # if the user chooses to read about Nanotechnology
        if curState == STATENANO:
            # gives the x coordinate range for all three buttons
            if 25 <= mousex <= 175:
                #gives the y coordinate range for the first button. If true, then user will find infomartion on the first trend
                if 225 <= mousey <= 275:
                    curSubState = STATENANOTREND1
                #gives the y coordinate range for the second button. If true, then user will find infomartion on the second trend
                elif 375 <= mousey <= 425:
                    curSubState = STATENANOTREND2
                #gives the y coordinate range for the third button. If true, then user will find information on the third trend
                elif 525 <= mousey <= 575:
                    curSubState = STATENANOTREND3
                    
        # if the user chooses to read about Smart Cities                   
        if curState == STATECITY:
            # gives the x coordinate range for all three buttons
            if 25 <= mousex <= 175:
                #gives the y coordinate range for the first button. If true, then user will find information on the first trend
                if 225 <= mousey <= 275:
                    curSubState = STATECITYTREND1
                #gives the y coordinate range for the second button. If true, then user will find information on the second trend    
                elif 375 <= mousey <= 425:
                    curSubState = STATECITYTREND2
                #gives the y coordinate range for the third button. If true, then user will find information on the third trend
                elif 525 <= mousey <= 575:
                    curSubState = STATECITYTREND3
    return curSubState

def moveBall (button, mousex,mousey,posx,posy,curState,curBallState):
    if button == 1:
        if curState == STATEMENU:
            if 0 <= mousex <= 225 and posy <= mousey <= (posy+125):                     
                curBallState = STATEBALLRIGHT
            # move the image
    if curBallState == STATEBALLRIGHT:  
        posx += 5       
        if posx >= 780:   
            curBallState = STATEBALLLEFT 
    elif curBallState == STATEBALLLEFT:
        posx -= 5 
        if posx <= 0:
            curBallState = STATEBALLRIGHT
    return curBallState,posx

#allows the user to move through the different pages of information 
def changeState(button, mousex, mousey, curState,curSubState):
    # everything only occurs when the user presses the mouse button down
    if button == 1:
        #with default showing menu page, user has 4 buttons to choose between
        if curState == STATEMENU:
             # the x coordinate's position for ALL boxes
            if 250 <= mousex <= 800:
                #the y position for the 4 button individually 
                    # Range for Quit Button
                if 525 <= mousey <= 600: 
                    curState = STATEQUIT
                    # Range for AI Button
                elif 150 <= mousey <= 225:
                    curState = STATEAI
                    # Range for NanoTech Button
                elif 275 <= mousey <= 350:
                    curState = STATENANO
                    # Range for Smart Cities Button 
                elif 400 <= mousey <= 475:
                    curState = STATECITY
        
        #if user chooses AI page, it will display             
        elif curState == STATEAI: 
            #if user clicks back button, page moves from AI page to menu
            if 325 <= mousex <= 475:
                if 50 <= mousey <= 100:
                    curState = STATEMENU
            #if user clicks Quit button or the X button, the program closes
            elif 625 <= mousex <= 775:
                if 50 <= mousey <= 100:
                    curState = STATEQUIT
        
        #if user chooses Nanotechnology page, it will display 
        elif curState == STATENANO:
            #if user clicks back button, page moves from AI page to menu
            if 325 <= mousex <= 475:
                if 50 <= mousey <= 100:
                    curState = STATEMENU
            #if user clicks Quit button or the X button, the program closes
            elif 625 <= mousex <= 775:
                if 50 <= mousey <= 100:
                    curState = STATEQUIT     
                    
        #if user chooses Smart Cities page, it will display            
        elif curState == STATECITY:
            #if user clicks back button, page moves from AI page to menu
            if 325 <= mousex <= 475:
                if 50 <= mousey <= 100:
                    curState = STATEMENU
            #if user clicks Quit button or the X button, the program closes
            elif 625 <= mousex <= 775:
                if 50 <= mousey <= 100:
                    curState = STATEQUIT

        curSubState = changeSubState (button, mousex, mousey, curState,curSubState)
    return curState,curSubState

#x and y coordinates for moving images
posx = 0
posx2 = 0
posx3 = 0
posy = 100
posy2 = 300
posy3 = 500

# Game Loop
#continue the loop until the user quits the program
while state != STATEQUIT:
    button = 0
    mx = my = 0
    # checks all events that happen
    for evnt in event.get():             
        if evnt.type == QUIT:
            state = STATEQUIT
        if evnt.type == MOUSEBUTTONDOWN:
            mx, my = evnt.pos 
            button = evnt.button
            
    drawScene(screen, state, subState)
    state,subState = changeState(button, mx, my,state,subState)  
    ballState,posx =  moveBall (button,mx,my,posx,posy,state,ballState)
    ballState2,posx2 =  moveBall (button,mx,my,posx2,posy2,state,ballState2)
    ballState3,posx3 =  moveBall (button,mx,my,posx3,posy3,state,ballState3)
    # waits long enough to have 60 fps
    myClock = time.Clock()  
    myClock.tick(60)             
quit()