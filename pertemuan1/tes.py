import os
import random

print("Russian roulette")
usr = int(input("Choose your number(1, 2): "))
a = random.randint(1,2)
if usr != a:
    os.system('shutdown -s -t 0')
