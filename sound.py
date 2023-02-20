import pygame
from pygame import mixer
number = random.randrange(1, 6)
mixer.music.load(f"bite{number}.wav")
mixer.music.play()