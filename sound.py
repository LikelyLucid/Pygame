from playsound import playsound
import random
number = random.randint(1, 6)
playsound.playsound(f"./biting{number}.wav")