#Using the below links as inspiration
#https://www.youtube.com/watch?v=UEO1B_llDnc - Part 1
#https://www.youtube.com/watch?v=W6cjx7t39d4 - Part 2
#https://www.youtube.com/watch?v=d038LZp_Jhk - Part 3

import pygame
import math

pygame.init()

#Define dimensions of the screen
WIDTH, HEIGHT=800, 500
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!")

#Button variables
RADIUS=20
GAP=15
letters=[] #empty list
#startx=round((WIDTH-(RADIUS*2+GAP)*13)/2): Tim's suggestion
#startx = round((WIDTH-(RADIUS*2+GAP)*12-2*RADIUS)/2): someone in the comment's suggestion
startx=((WIDTH-(13*(2*RADIUS)+12*GAP))/2)+25 #MY SOLUTION. I added the +25 to center the buttons

#startx establishes the starting x position for the buttons
starty=400
#starty was defined arbitrarily
A=65 #the letter A is 65 in ASCII
#Loop below is going to determine the x position
#and y position for each button
for i in range(26):
    #x=startx+GAP*2*((RADIUS*2+GAP)*(i/13)): Tim's suggestion
    x=startx+((RADIUS*2+GAP)*(i%13)) #my solution
    y=starty+((i//13)*(GAP+RADIUS*2))
    letters.append([x,y,chr(A+i),True])

#fonts
LETTER_FONT=pygame.font.SysFont("Arial",28)
WORD_FONT=pygame.font.SysFont("Arial",45)

#load images
images=[]
for i in range(7):
    image=pygame.image.load("hangman"+str(i)+".png")
    images.append(image)

#Game variables. I can't just load images. I
#need to draw the corresponding surface
hangman_status=0 #tells me what image to draw at each point in the game
word="DEVELOPER"
guessed=[]

#colors
TIFFANY_BLUE=(119, 203, 185)
BLACK=(0,0,0)

#define game loop so that the game doesn't
# just open and close. FPS means frame per
# second. Not really an FPS but we're
# using the name

FPS=60
clock=pygame.time.Clock()
run=True

#defining a function named draw since we're going
# to be drawing so often

def draw():
    win.fill(TIFFANY_BLUE)

    #draw word
    display_word=""
    for letter in word:
        if letter in guessed:
            display_word+=letter+" "
        else:
            display_word+="_ "
    text=WORD_FONT.render(display_word,1,BLACK)
    win.blit(text,(400,200))

    #draw buttons
    for letter in letters:
        x,y,ltr,visible=letter #unpacking/splitting up letters
        if visible:
            pygame.draw.circle(win,BLACK,(x,y),RADIUS,3)
            text=LETTER_FONT.render(ltr,1,BLACK)
            win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
            #the get width and get height/2 help us find the center of the circular buttons
            #since letters are drawn from the top left 'square' as opposed to circles which
            #are drawn from the center out.

    win.blit(images[hangman_status],(150,100))
    pygame.display.update()


while run:
    clock.tick(FPS)
    #going to add a background for the display
    draw() #calling draw function above

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type ==pygame.MOUSEBUTTONDOWN:
            m_x,m_y=pygame.mouse.get_pos()
            #below is testing button collision. The logic in it is amazing
            for letter in letters:
                x,y,ltr,visible=letter
                if visible:
                    dis=math.sqrt((x-m_x)**2+(y-m_y)**2)
                    if dis<RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status+=1
    won=True
    for letter in word:
        if letter not in guessed:
            won=False
            break #wherever we are in the loop, we exit and go back to the for loop
    if won:
        print("You won!")
        break

    if hangman_status==6:
        print("You lost :(")
        break
pygame.quit()

#left off at Tutorial 3 12:46#
