import random
a = random.randint(0,9); b = random.randint(0,9);
c = random.randint(0,9); d = random.randint(0,9); proof = True
while proof:
    a = random.randint(0,9); b = random.randint(0,9); 
    c = random.randint(0,9); d = random.randint(0,9)
    print(a,b,c,d)
    if len({a,b,c,d}) < 4:
        proof = False
