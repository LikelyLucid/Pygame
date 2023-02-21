import pygame
from pygame import mixer
import random
number = random.randrange(1, 6)
mixer.music.load(f"biting{number}.wav")
mixer.music.play()