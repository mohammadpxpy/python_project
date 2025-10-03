#LOTTERY WORD

import random
import time


number_word = int(input("How mant words do you need? "))
number = 0
speed = 0.200
words = []
len_item = len(words)

while number < number_word:
    user = input("word: ").replace(" ","")
    words.append(user)
    number += 1
    if number == number_word:
        run = input("for start click ENTER ")
        if len(run) == 0:
            for i in range(len_item + 15):
                choise_word = random.choice(words)
                time.sleep(speed)
                print(f"{choise_word}         ", end="\r")
                speed += 0.050
                
                
print("=>",choise_word)
            


