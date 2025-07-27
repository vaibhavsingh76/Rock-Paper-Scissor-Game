import random

mydict={"s":1 , "p": 2, "c":3}
compdict={1: "𝐒𝐓𝐎𝐍𝐄🪨" , 2:"𝐏𝐀𝐏𝐄𝐑🧻" , 3:"𝐒𝐂𝐈𝐒𝐒𝐎𝐑✂️"}

win = 0
lose = 0
draw = 0

n=int(input("How many round You want to play? : "))

for round in range(1,n+1):
    print(f" ▶   It is your round ♨️{round}")
    
    comp = random.choice([1, 2, 3])
    you = input('''Enter your choice out of :-
                s: stone 🪨, 
                p: paper 🧻, 
                c: scissor ✂️ : ''')

    if you not in mydict:
        print("❌ Invalid input! Please choose from s, p, or c.")
        continue  

    my_value = mydict[you]

    print(f"You chose: {compdict[my_value]}")
    print(f"Computer chose: {compdict[comp]}")

    if comp==my_value:
        print("                            DRAW! ⚖️")
        draw += 1

    elif(comp == 1 and my_value == 2) or \
        (comp == 2 and my_value == 3) or \
        (comp == 3 and my_value == 1):
        print("                         You won! ✅")
        win += 1

    else:
        print("                         You Loose ❌")
        lose += 1
            

print("\n🏁 Game Over!")
print(f"✅ Wins: {win}")
print(f"❌ Losses: {lose}")
print(f"⚖️  Draws: {draw}")

