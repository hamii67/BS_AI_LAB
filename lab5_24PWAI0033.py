for i in range(5):
    p = input(f"Enter password: ")
    s = (len(p)>=8) + any(c.isdigit() for c in p) + (p!=p.lower())
    print(f"Strength: {['Very Weak','Weak','Moderate','Strong'][s]}")
    if s==3:
        print(f"You created a strong password!")
        print(f"AI training Level: Beginner → Intermediate")
        break
    print(f"Attempts remaining: {4-i}")
else: print(f"Final Result: Password is not strong enough.")