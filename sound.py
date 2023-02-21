from playsound import playsound
import random
number = random.randint(1, 6)
playsound(f"./biting{number}.wav")