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

white = (255, 255, 255)
w = 1920
h = 1080
screen = pygame.display.set_mode((w, h))
screen.fill((white))

# load images, scale to 1920 x 1080 scale
intro = pygame.image.load("images/intro.PNG")
# intro = pygame.transform.scale(intro, (1920, 1080))
rules1 = pygame.image.load("images/rules1.PNG")
# rules1 = pygame.transform.scale(rules1, (1920, 1080))
rules2 = pygame.image.load("images/rules2.PNG")
# rules2 = pygame.transform.scale(rules2, (1920, 1080))
rules3 = pygame.image.load("images/rules3.PNG")
# rules3 = pygame.transform.scale(rules3, (1920, 1080))
rules4 = pygame.image.load("images/rules4.PNG")
# rules4 = pygame.transform.scale(rules4, (1920, 1080))
rules5 = pygame.image.load("images/rules5.PNG")
# rules5 = pygame.transform.scale(rules5, (1920, 1080))
rules6 = pygame.image.load("images/rules6.PNG")
# rules6 = pygame.transform.scale(rules6, (1920, 1080))
compGrid = pygame.image.load("images/compGrid.PNG")
# compGrid = pygame.transform.scale(compGrid, (1920, 1080))
s1 = pygame.image.load("images/s1.PNG")
# s1 = pygame.transform.scale(s1, (1920, 1080))
s2 = pygame.image.load("images/s2.PNG")
# s2 = pygame.transform.scale(s2, (1920, 1080))
s3 = pygame.image.load("images/s3.PNG")
# s3 = pygame.transform.scale(s3, (1920, 1080))
s4 = pygame.image.load("images/s4.PNG")
# s4 = pygame.transform.scale(s4, (1920, 1080))
s5 = pygame.image.load("images/s5.PNG")
# s5 = pygame.transform.scale(s5, (1920, 1080))
s6 = pygame.image.load("images/s6.PNG")
# s6 = pygame.transform.scale(s6, (1920, 1080))
s7 = pygame.image.load("images/s7.PNG")
# s7 = pygame.transform.scale(s7, (1920, 1080))
s8 = pygame.image.load("images/s8.PNG")
# s8 = pygame.transform.scale(s8, (1920, 1080))
s9 = pygame.image.load("images/s9.PNG")
# s9 = pygame.transform.scale(s9, (1920, 1080))
fact1 = pygame.image.load("images/fact1.PNG")
# fact1 = pygame.transform.scale(fact1, (1920, 1080))
fact2 = pygame.image.load("images/fact2.PNG")
# fact1 = pygame.transform.scale(fact2, (1920, 1080))
fact3 = pygame.image.load("images/fact3.PNG")
# fact3 = pygame.transform.scale(fact3, (1920, 1080))
fact4 = pygame.image.load("images/fact4.PNG")
# fact4 = pygame.transform.scale(fact4, (1920, 1080))
fact5 = pygame.image.load("images/fact5.PNG")
# fact5 = pygame.transform.scale(fact5, (1920, 1080))
fact6 = pygame.image.load("images/fact6.PNG")
# fact6 = pygame.transform.scale(fact6, (1920, 1080))
fact7 = pygame.image.load("images/fact7.PNG")
# fact7 = pygame.transform.scale(fact7, (1920, 1080))
fact8 = pygame.image.load("images/fact8.PNG")
# fact8 = pygame.transform.scale(fact8, (1920, 1080))
fact9 = pygame.image.load("images/fact9.PNG")
# fact9 = pygame.transform.scale(fact9, (1920, 1080))
form = pygame.image.load("images/form.PNG")
# form = pygame.transform.scale(form, (1920, 1080))
thank = pygame.image.load("images/thank.PNG")
# thank = pygame.transform.scale(thank, (1920, 1080))
end = pygame.image.load("images/end.PNG")
# end = pygame.transform.scale(end, (1920, 1080))

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
    screen.fill((white))
    screen.blit(image,(236,134))
    pygame.display.update()
    play_sound(f"sounds/{sound}")

for i in range(8):
    show_screen(rules[i], rules_Sound[i])
    t.sleep(3)