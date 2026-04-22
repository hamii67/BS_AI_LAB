import random
n = random.randint(1, 50)
for a in range(7):
    g = input(f"Guess 1-50: ")
    if not g.isdigit(): 
        print(f"Not a number! Tries left: {6-a}")
        continue
    g = int(g)
    if g<1 or g>50: 
        print(f"1-50 only! Tries left: {6-a}")
        continue
    if g>n: print(f"Too high!")
    elif g<n: print(f"Too low!")
    else: 
        print(f"You win in {a+1} attempts!")
        print(f"AI training level: Beginner → Intermediate")
        break
    print(f"Tries left: {6-a}")
else: print(f"You lose! Number was {n}.")