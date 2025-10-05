#game word

import random

words = "game","war","phone","laptop","paper"
select_word = random.choice(words)

len_word = len(select_word)
chans = 10
truly_chosen = []

while chans > 0:

        for i in select_word:
            if i in truly_chosen:
                print(i, end="")
            else:
                print("_ ", end="")
                    
        user = str(input(" your guss: "))
        if user not in truly_chosen and user in select_word:
            print("new found🎁")
            truly_chosen.append(user)

        if len(truly_chosen) == len(set(select_word)):
            print("\nYou Won!😎")
            break
        chans -= 1
