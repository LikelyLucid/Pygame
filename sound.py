import pygame
from pygame import mixer
import random
mixer.init()
number = random.randrange(1, 6)
print(number)
mixer.music.load("biting1.wav")
mixer.Sound.play(mixer.music)
mixer.music.play()