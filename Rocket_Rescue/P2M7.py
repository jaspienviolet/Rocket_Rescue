import serial as s
from PIL import Image, ImageTk
import pygame
import time as t

# char code meanings
# g = good for reset
# b = not good for reset
# L = launch
# r = attempting to reset
# c = rocket parts picked
# s = sounds and image to play
# n = next image
# d = conveyor belt finished moving
# e = end and reset conveyor belt

# Initialize pygame for sound
pygame.mixer.init()
pygame.init()

black = (0, 0, 0)
w = 1920
h = 1080
screen = pygame.display.set_mode((w, h))
screen.fill((black))

# load images, scale to 1920 x 1080 scale
intro = pygame.image.load("images/intro.PNG")
rules1 = pygame.image.load("images/rules1.PNG")
rules2 = pygame.image.load("images/rules2.PNG")
rules3 = pygame.image.load("images/rules3.PNG")
rules4 = pygame.image.load("images/rules4.PNG")
rules5 = pygame.image.load("images/rules5.PNG")
rules6 = pygame.image.load("images/rules6.PNG")
compGrid = pygame.image.load("images/compGrid.PNG")
s1 = pygame.image.load("images/s1.PNG")
s2 = pygame.image.load("images/s2.PNG")
s3 = pygame.image.load("images/s3.PNG")
s4 = pygame.image.load("images/s4.PNG")
s5 = pygame.image.load("images/s5.PNG")
s6 = pygame.image.load("images/s6.PNG")
s7 = pygame.image.load("images/s7.PNG")
s8 = pygame.image.load("images/s8.PNG")
s9 = pygame.image.load("images/s9.PNG")
fact1 = pygame.image.load("images/fact1.PNG")
fact2 = pygame.image.load("images/fact2.PNG")
fact3 = pygame.image.load("images/fact3.PNG")
fact4 = pygame.image.load("images/fact4.PNG")
fact5 = pygame.image.load("images/fact5.PNG")
fact6 = pygame.image.load("images/fact6.PNG")
fact7 = pygame.image.load("images/fact7.PNG")
fact8 = pygame.image.load("images/fact8.PNG")
fact9 = pygame.image.load("images/fact9.PNG")
form = pygame.image.load("images/form.PNG")
thank = pygame.image.load("images/thank.PNG")
end = pygame.image.load("images/end.PNG")

rules = [intro, rules1, rules2, rules3, rules4, rules5, rules6, compGrid]
rules_Sound = ["intro.mp3", "rules1.mp3", "rules2.mp3", "rules3.mp3", "rules4.mp3", "rules5.mp3", "rules6.mp3", "compGrid.mp3"]
reaction = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
reaction_Sound = ["s1.mp3", "s2.mp3", "s3.mp3", "s4.mp3", "s5.mp3", "s6.mp3", "s7.mp3", "s8.mp3", "s9.mp3"]
reflection = [fact1, fact2, fact3, fact4, fact5, fact6, fact7, fact8, fact9]
reflection_Sound =["fact1.mp3", "fact2.mp3", "fact3.mp3", "fact4.mp3", "fact5.mp3", "fact6.mp3", "fact7.mp3", "fact8.mp3", "fact9.mp3"]
ending = [thank, end, form]
ending_Sound = ["thank.mp3", "end.mp3", "form.mp3"]

# game functions
def play_sound(file_path):
    """Play sound using pygame"""
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# storyline functions
def show_screen(image, sound):
    """Display screen and play associated sound file"""
    global screen
    screen.fill((black))
    screen.blit(image,(236,134))
    pygame.display.update()
    play_sound(f"sounds/{sound}")


# Serial port setup
cg1 = s.Serial(port='COM3', baudrate=9600)
cb1 = s.Serial(port='COM4', baudrate=9600)
cg2 = s.Serial(port='COM5', baudrate=9600)
cb2 = s.Serial(port='COM6', baudrate=9600)

print("Program confirmed")

while True:
    L = 0
    g1 = 0
    g2 = 0
    score1 = ''
    score2 = ''
    page = 0
    p1 = 0
    p2 = 0
    reset = 0

    while True:

        if page < 8:
            show_screen(rules[page], rules_Sound[page])
            t.sleep(1)
            page += 1

        if cg1.in_waiting > 0:
            p1 = 1

            rg1 = cg1.readline().decode().strip('\n')
            print(rg1)

            if 's' in rg1:
                rG1 = rg1.split(',')
                print(rG1)
                sG1 = rG1[1]
                show_screen(reaction[int(sG1) - 1], reaction_Sound[int(sG1) - 1])
            
            if 'c' in rg1:
                rG1 = rg1.split(',')
                print(rG1)
                cG1 = rG1[1:]
                cG1a = cG1
                print(cG1)

                match cG1[0]:    # nose
                    case '1':     # ogive
                        cG1a[0] = 3
                    case '2':     # elliptical
                        cG1a[0] = 2
                    case '3':     # conic
                        cG1a[0] = 1

                match cG1[1]:    # material
                    case '4':     # steel
                        cG1a[1] = 2
                    case '5':     # aluminium
                        cG1a[1] = 3
                    case '6':     # magnesium
                        cG1a[1] = 1

                match cG1[2]:    # fuel
                    case '7':     # coal
                        cG1a[2] = 1
                    case '8':     # ethanol
                        cG1a[2] = 2
                    case '9':     # methane
                        cG1a[2] = 3

                score1 = str(int(cG1a[0]) + int(cG1a[1]) + int(cG1a[2]))
                print(score1)

            # if 'L' in rg1:
            #     print("launch")
            #     L = 1

            if 'r' in rg1:
                print("Attempting Reset")
                res = 'r'
                cg1.write(res.encode('utf-8'))
                cg2.write(res.encode('utf-8'))

            if 'g' in rg1:
                g1 = 1
                print(rg1)

            if 'b' in rg1 :
                print('cg1',rg1)


        if cg2.in_waiting > 0:
            p2 = 1

            rg2 = cg2.readline().decode().strip('\n')
            print(rg2)

            if 's' in rg2:
                rG2 = rg2.split(',')
                print(rG2)
                sG2 = rG2[1]
                show_screen(reaction[int(sG2) - 1], reaction_Sound[int(sG2) - 1])
            
            if 'c' in rg2:
                rG2 = rg2.split(',')
                print(rG2)
                cG2 = rG2[1:]
                cG2a = cG2
                print(cG2)

                match cG2[0]:    # nose
                    case '1':     # ogive
                        cG2a[0] = 3
                    case '2':     # elliptical
                        cG2a[0] = 2
                    case '3':     # conic
                        cG2a[0] = 1

                match cG2[1]:    # material
                    case '4':     # steel
                        cG2a[1] = 2
                    case '5':     # aluminium
                        cG2a[1] = 3
                    case '6':     # magnesium
                        cG2a[1] = 1

                match cG2[2]:    # fuel
                    case '7':     # coal
                        cG2a[2] = 1
                    case '8':     # ethanol
                        cG2a[2] = 2
                    case '9':     # methane
                        cG2a[2] = 3

                score2 = str(int(cG2a[0]) + int(cG2a[1]) + int(cG2a[2]))
                print(score2)

            if 'L' in rg2:
                print("launch")
                L = 1

            if 'r' in rg2:
                print("Attempting Reset")
                res = 'r'
                cg1.write(res.encode('utf-8'))
                cg2.write(res.encode('utf-8'))

            if 'g' in rg2:
                g2 = 1
                print(rg2)

            if 'b' in rg2:
                print('cg2',rg2)

        if cb1.in_waiting > 0:
            rB1 = cb1.readline().decode().strip('\n')
            print(rB1)

            if 'd' in rB1:
                score1 = 0

        if cb2.in_waiting > 0:
            rB2 = cb2.readline().decode().strip('\n')
            print(rB2)

            if 'd' in rB2:
                score2 = 0

        if (g2 == 1) and (reset == 0):
            reset = 1
            end = 'e'
            print(end)
            cb1.write(end.encode('utf-8'))
            cb2.write(end.encode('utf-8'))
            g1 = 0
            g2 = 0
            match cG1[0]:
                case 1:
                    cG1[0] = 3
                case 2:
                    cG1[0] = 2
                case 3:
                    cG1[0] = 1
            match cG1[1]:
                case 1:
                    cG1[1] = 6
                case 2: 
                    cG1[1] = 4
                case 3:
                    cG1[1] = 5
            match cG1[2]:
                case 1:
                    cG1[2] = 7
                case 2:
                    cG1[2] = 8
                case 3:
                    cG1[2] = 9
            match cG2[0]:
                case 1:
                    cG2[0] = 3
                case 2:
                    cG2[0] = 2
                case 3:
                    cG2[0] = 1
            match cG2[1]:
                case 1:
                    cG2[1] = 6
                case 2: 
                    cG2[1] = 4
                case 3:
                    cG2[1] = 5
            match cG2[2]:
                case 1:
                    cG2[2] = 7
                case 2:
                    cG2[2] = 8
                case 3:
                    cG2[2] = 9
            print(cG1)
            show_screen(reflection[int(cG1[0]) - 1], reflection_Sound[int(cG1[0]) - 1])
            t.sleep(5)
            show_screen(reflection[int(cG1[1]) - 1], reflection_Sound[int(cG1[1]) - 1])
            t.sleep(5)
            show_screen(reflection[int(cG1[2]) - 1], reflection_Sound[int(cG1[2]) - 1])
            t.sleep(5)
            print(cG2)
            show_screen(reflection[int(cG2[0]) - 1], reflection_Sound[int(cG2[0]) - 1])
            t.sleep(5)
            show_screen(reflection[int(cG2[1]) - 1], reflection_Sound[int(cG2[1]) - 1])
            t.sleep(5)
            show_screen(reflection[int(cG2[2]) - 1], reflection_Sound[int(cG2[2]) - 1])
            t.sleep(5)
            show_screen(ending[0], ending_Sound[0])
            t.sleep(6)
            show_screen(ending[1], ending_Sound[1])
            t.sleep(6)
            show_screen(ending[2], ending_Sound[2])
            t.sleep(10)
            break
                
        if L == 1 and (score1 > "" and score2 > ""):
            cb1.write(score1.encode('utf-8'))
            cb2.write(score2.encode('utf-8'))
            L = 0




