import random
import sys
p_hand1 = 1
p_hand2 = 1
AI_hand1 = 1
AI_hand2 = 1
nothing = 0
turns_per_p = 1
swap_boolean = 0
nothing1 = 0
turns_lasted = 0
history=[0, 0, 0, 0]
history_for_p_hand2=0
undo_charges=3





#SUUS

#HOW TO WIN: Get the player to have a 2/0, and the AI to have a 2/1. Then hit their 2 with your 2, they hit your 2 with a 1, then finally hit their 1 with your 3.

#HOW TO WIN AGAINST PLAYERS AND THE AI: Get yourself to 4/1, and the other person to 3/0. Then combine into 3/2. The bot will combine, but from there, you should just win.

#HOW TO PLAY:
#The first question during your turn is "What do you want to hit?"
#The second question, if you answered hand1 or hand2, is "With what hand?"
#If you answered 'combine' for the first question, then the second question is, "After the combination, what will be the bigger hand?"
#If you answered 'combine' for the first question, then the third question is, "How many fingers do you want to move to the bigger hand?"

#How to code:
#p_hand1 is the player's right hand
#p_hand2 is the player's left hand
#AI_hand1 is the AI's left hand
#AI_hand2 is the AI's right hand
#The variables:
#   p_big_hand
#   p_subtract_x_from_the_lesser_hand
#only do anything if the player wants to combine.
#For the Huge amount of code that the AI has, I count like this...  1, 2, 3, 4, 0, stop. But that doesn't make sense. It's just how I count in this program

def sswap():
    global p_hand1, p_hand2, AI_hand1, AI_hand2, random_chance, swap_boolean, swap, turns_per_p, turns_lasted, before_p_hand1, before_p_hand2
    swap_boolean=1
    swap=AI_hand1
    AI_hand1=AI_hand2
    AI_hand2=swap

def check():
    global p_hand1, p_hand2, AI_hand1, AI_hand2, random_chance, swap_boolean, swap, turns_per_p, turns_lasted, before_p_hand1, before_p_hand2
    if AI_hand1 > 4:
        AI_hand1 -= 5
    if AI_hand2 > 4:
        AI_hand2 -= 5
    if p_hand1 > 4:
        p_hand1 -= 5
    if p_hand2 > 4:
        p_hand2 -= 5
    if p_hand1==0:
        if p_hand2==0:
            print("The AI won.")
            print(f"The player lasted {turns_lasted} turns!")
            sys.exit()
    if AI_hand1==0:
        if AI_hand2==0:
            print("The player won!")
            print(f"The player took {turns_lasted} turns to beat the AI!")
            sys.exit()

def player_turn():
    global p_hand1, p_hand2, AI_hand1, AI_hand2, random_chance, swap_boolean, swap, turns_per_p, turns_lasted, before_p_hand1, before_p_hand2, history, history_for_p_hand2, undo_charges
    before_p_hand1 = p_hand1
    before_p_hand2 = p_hand2
    print(f"You have {undo_charges} undo charges.")
    player_response1 = input(f"Your turn! You have a {p_hand1} and a {p_hand2}. What do you want to hit, my hand1; it's at {AI_hand1}, or my hand2; it's at {AI_hand2}? Or do you want to combine/undo? Don't use spaces.\n")
    if (player_response1=="undo" or player_response1=="u") and history!=[0, 0, 0, 0]:
        AI_hand2=history[0]
        AI_hand1=history[1]
        p_hand1=history[2]
        p_hand2=history[3]
        undo_charges-=1
        player_turn()
        return
    else:
        history[0]=AI_hand2
        history[1]=AI_hand1
        history[2]=p_hand1
        history[3]=p_hand2
    if player_response1 == "cOMaNDs":
        print("Commands successful. To all you nerds, I know I mispelled 'commands' wrong.")
        undo_charges=input("How many undo charges should you get?\n")
        undo_charges=int(undo_charges)
        turns_per_p=input("How many turns do you want each player to go?\n")
        turns_per_p=int(turns_per_p)
        AI_hand2=input("What should AI_hand2 be?\n")
        AI_hand2=int(AI_hand2)
        AI_hand1=input("What should AI_hand1 be?\n")
        AI_hand1=int(AI_hand1)
        p_hand1=input("What should player_hand1 be?\n")
        p_hand1=int(p_hand1)
        p_hand2=input("What should player_hand2 be?\n")
        p_hand2=int(p_hand2)
        if turns_per_p > 1:
            player_turn()
            check()
        if turns_per_p == 3:
            player_turn()
            check()
        check()
        player_turn()
    elif player_response1 != "combine" and player_response1 != "c":
        if player_response1 == "1":
            player_response1 = "hand1"
        if player_response1 == "2":
            player_response1 = "hand2"
        if player_response1=="hand1":
            if AI_hand1==0:
                print("You must've hit a hand with 0 on accident. I'm going to give your turn back.")
                player_turn()
                return
        if player_response1=="hand2":
            if AI_hand2==0:
                print("You must've hit a hand with 0 on accident. I'm going to give your turn back.")
                player_turn()
                return
        player_response2 = input(f"And want do you want to hit my {player_response1} with? Your hand 1, {p_hand1}, or your hand 2, {p_hand2}? No spaces again please.\n")
        if player_response2 == "1":
            player_response2 = "hand1"
        if player_response2 == "2":
            player_response2 = "hand2"
        if player_response2=="hand1":
            if p_hand1==0:
                print("You must've tried use a hand with 0 on accident. I'm going to give your turn back.")
                player_turn()
                return
        if player_response2=="hand2":
            if p_hand2==0:
                print("You must've tried use a hand with 0 on accident. I'm going to give your turn back.")
                player_turn()
                return
        if player_response1 == "hand2":
            if player_response2 == "hand1":
                AI_hand2 = AI_hand2 + p_hand1
            elif player_response2 == "hand2":
                AI_hand2 = AI_hand2 + p_hand2
            else:
                print("Invalid response. Please choose 'hand1' or 'hand2'. I'm going to give your turn back.")
                player_turn()
                return
            check()
            print(f"AI's hand 2 is now: {AI_hand2}")
        elif player_response1 == "hand1":
            if player_response2 == "hand2":
                AI_hand1 = AI_hand1 + p_hand2
            elif player_response2 == "hand1":
                AI_hand1 = AI_hand1 + p_hand1
            else:
                print("Invalid response. Please choose 'hand1' or 'hand2'. I'm going to give your turn back.")
                player_turn()
                return
            check()
            print(f"AI's hand 1 is now: {AI_hand1}")
        else:
            print("Invalid response. Please choose 'hand1' or 'hand2'. I'm going to give your turn back.")
            player_turn()
            return
    else:                     #if p_response1 is "combine":
        p_big_hand=input("Which hand do you want to add fingers to?\n")
        if p_big_hand == "1":
            p_big_hand = "hand1"
        if p_big_hand == "2":
            p_big_hand = "hand2"
        p_subtract_x_from_lesser_hand=input(f"And how much do you want add to your {p_big_hand}? It can't be 0 or less.\n")
        if int(p_subtract_x_from_lesser_hand)>0:
            if p_big_hand=="hand1":
                if int(p_subtract_x_from_lesser_hand) <= int(p_hand2):
                    p_hand1 += int(p_subtract_x_from_lesser_hand)
                    p_hand2 -= int(p_subtract_x_from_lesser_hand)
                else:
                    print("You tried to subtract more fingers than you had. I'm going to give your turn back now. Don't misbehave.")
                    player_turn()
                    return
            elif p_big_hand=="hand2":
                if int(p_subtract_x_from_lesser_hand) <= int(p_hand1):
                    p_hand2 += int(p_subtract_x_from_lesser_hand)
                    p_hand1 -= int(p_subtract_x_from_lesser_hand)
                else:
                    print("You tried to subtract more fingers than you had. I'm going to give your turn back now. Don't misbehave.")
                    player_turn()
                    return
            else:
                print("Invalid response. Please choose 'hand1' or 'hand2'. I'm going to give your turn back.")
                player_turn()
                return
        else:
            print("You should not've made it 0. I'm going to give your turn back.")
            player_turn()
            return
        check()
        if p_hand1 == before_p_hand2:
            if p_hand2 == before_p_hand1:
                print("Changing the position doesn't take a turn. Here's your turn back:")
                player_turn()
                return
    if player_response1=="combine":
        print(f"Your new hands are, {p_hand1} and {p_hand2}.")

def AI_turn():                         #AI TURN
    global p_hand1, p_hand2, AI_hand1, AI_hand2, random_chance, swap_boolean, swap, turns_per_p, turns_lasted, before_p_hand1, before_p_hand2
    if AI_hand2 == 0:
        sswap()
    elif AI_hand2 == 4:
        sswap()
    if AI_hand2 == 1:
        if AI_hand1 == 1:
            if p_hand1 == 1:
                if p_hand2 == 1:
                    random_chance=random.randint(0, 1)
                    if random_chance==0:
                        p_hand1 = 2
                        print("The AI hit your hand 1 for 1 finger. It's at 1 finger.")
                    else:
                        AI_hand1=2
                        AI_hand2=0
                        print("The AI combined.")
                elif p_hand2 == 2:
                    random_chance=random.randint(0, 1)
                    if random_chance==0:
                        p_hand1 = 2
                        print("The AI hit your hand 2 for 1 finger. It's at 2 fingers.")
                    else:
                        AI_hand1=0
                        AI_hand2=2
                        print("The AI combined.")
                elif p_hand2 == 3:
                    p_hand2 = 4
                    print("The AI hit your hand 1 for 1 finger. It's at 4 fingers.")
                elif p_hand2 == 4:
                    p_hand2 = 0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2 == 0:
                    AI_hand1=2
                    AI_hand2=0
                    print("The AI combined.")
                else:
                    print("Something broke.")
            elif p_hand1 ==2:
                if p_hand2 == 1:
                    random_chance=random.randint(0, 1)
                    if random_chance==0:
                        p_hand2 = 2
                        print("The AI hit your hand 2 for 1 finger. It's at 2 fingers.")
                    else:
                        AI_hand1=0
                        AI_hand2=2
                        print("The AI combined.")
                elif p_hand2 == 2:
                    random_chance=random.randint(0, 1)
                    if random_chance==0:
                        p_hand2 = 3
                        print("The AI hit your hand 2 for 1 finger. It's at 3 fingers.")
                    else:
                        AI_hand1=0
                        AI_hand2=2
                        print("The AI combined.")
                elif p_hand2 == 3:
                    p_hand1 = 3
                    print("The AI hit your hand 1 for 1 finger. It's at 3 fingers.")
                elif p_hand2 == 4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2 == 0: #Mason came up w/ this
                    AI_hand1=2
                    AI_hand2=0
                    print("The AI combined.")
                else:
                    print("Something broke.")
            elif p_hand1 == 3:
                if p_hand2==1:
                    p_hand1 = 4
                    print("The AI hit your hand 1 for 1 finger. It's at 4 fingers.")
                elif p_hand2==2:
                    p_hand2 = 3
                    print("The AI hit your hand 2 for 1 finger. It's at 3 fingers.")
                elif p_hand2==3:
                    p_hand2=4
                    print("The AI hit your hand 2 for 1 finger. It's at 4 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=4
                    print("The AI hit your hand 2 for 1 finger. It's at 4 fingers.")
                else:
                    print("Something broke")
            elif p_hand1 == 4:
                if p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers. The AI won.")
                else:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
            elif p_hand1 == 0:
                if p_hand2==1:
                    AI_hand1=0
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==2:
                    AI_hand1=2
                    AI_hand2=0
                    print("The AI combined.")
                elif p_hand2==3:
                    p_hand2=4
                    print("The AI hit your hand 2 for 1 finger. It's at 4.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers. The AI won.")
                elif p_hand1==0:
                    print("Why did you combine? The AI won, I guess.")
        elif AI_hand1 == 2:
            if p_hand1 == 1:
                if p_hand2 == 1:
                    AI_hand1=3
                    AI_hand2=0
                    print("The AI combined.")
                elif p_hand2 == 2:
                    p_hand2=4
                    print("The AI hit your hand 2 for 2 fingers. It's at 4 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    AI_hand1=3
                    AI_hand2=0
                    print("The AI combined.")
            elif p_hand1 == 2:
                if p_hand2==1:
                    p_hand2=2
                    print("The AI hit your hand 2 for 1 finger. It's at 2 fingers.")
                elif p_hand2 == 2:
                    p_hand1=4
                    print("The AI hit your hand 2 for 2 fingers. It's down to 4 fingers.")
                elif p_hand2 == 3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2 == 4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2 == 0:
                    p_hand2=4
                    print("The AI hit your hand 2 for 2 fingers. It's at 4 fingers.")
                else:
                    print("Something broke")
            elif p_hand1 == 3:
                p_hand1=0
                print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
            elif p_hand1 == 4:
                if p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                else:
                    p_hand1 = 0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
            elif p_hand1 == 0:
                if p_hand2 == 1:
                    AI_hand1=0
                    AI_hand2=3
                    print("The AI combined.")
                elif p_hand2 == 2:
                    p_hand2=4
                    print("The AI hit your hand 2 for 2 fingers. It's at 4 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==0:
                    print("Why did you combine? The AI won, I guess.")
        elif AI_hand1 == 3:
            if p_hand1 == 1:
                if p_hand2==1:
                    AI_hand1=2
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    AI_hand1=2
                    AI_hand2=2
                    print("The AI combined.")
                else:
                    print("Something broke")
            elif p_hand1==2:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    AI_hand1=2
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==3:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers. The AI won.")
                else:
                    print("Something broke")
            elif p_hand1==3:
                if p_hand2==1:
                    p_hand1=1
                    print("The AI hit your hand 1 for 3 fingers. It's down to 1 fingers.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand1=1
                    print("The AI hit your hand 1 for 3 fingers. It's down to 1 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 fingers. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=1
                    print("The AI hit your hand 1 for 3 fingers. It's down to 1 fingers.")
                else:
                    print("Something broke")
            elif p_hand1==4:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers. The AI won.")
            elif p_hand1==0:
                if p_hand2==1:
                    AI_hand1=2
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers. The AI won.")
                elif p_hand2==0:
                    print("Why did you combine? The AI won, I guess.")
        elif AI_hand1==4:
            if p_hand1==1:
                if p_hand2==1:
                    AI_hand1=2
                    AI_hand2=3
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand1=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand1=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers. The AI won.")
                else:
                    print("Something broke")
            elif p_hand1==2:
                if p_hand2==1:
                    p_hand2=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand1=3
                    print("The AI hit your hand 1 for 1 finger. It's at 3 fingers.")
                elif p_hand2==3:
                    p_hand1=3
                    print("The AI hit your hand 1 for 1 finger. It's at 3 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=3
                    print("The AI hit your hand 1 for 1 finger. It's at 3 fingers.")
                else:
                    print("Something broke")
            elif p_hand1==3:
                if p_hand2==1:
                    p_hand2=0
                    print("The AI hit your hand 2 for 4 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand1=4
                    print("The AI hit your hand 1 for 1 finger. It's at 4 fingers.")
                elif p_hand2==3:
                    p_hand1=4
                    print("The AI hit your hand 1 for 1 finger. It's at 4 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==0:
                    AI_hand1=2
                    AI_hand2=3
                    print("The AI combined.")
                else:
                    print("Something broke")
            elif p_hand1==4:
                if p_hand2==1:
                    p_hand2=0
                    print("The AI hit your hand 2 for 4 finger. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand2=1
                    print("The AI hit your hand 2 for 4 finger. It's down to 1 finger.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    AI_hand1=3
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers. The AI won.")
                else:
                    print("Something broke")
            elif p_hand1==0:
                if p_hand2==1:
                    p_hand2=0
                    print("The AI hit your hand 2 for 4 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==2:
                    p_hand2=3
                    print("The AI hit your hand 2 for 1 finger. It's down to 3 fingers.")
                elif p_hand2==3:
                    AI_hand1=3
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers. The AI won.")
                elif p_hand2==0:
                    print("Why did you combine? The AI won, I guess.")
        elif AI_hand1==0:
            if p_hand1==1:
                if p_hand2==1:
                    p_hand1=2
                    print("The AI hit your hand 1 for 1 finger. It's at 2 fingers.")
                elif p_hand2==2:
                    random_chance=random.randint(0,1)
                    if random_chance==1:
                        p_hand2=3
                        print("The AI hit your hand 2 for 1 finger. It's at 3 fingers.")
                    else:
                        p_hand1=2
                        print("The AI hit your hand 1 for 1 finger. It's at 2 fingers.")
                elif p_hand2==3:
                    p_hand1=2
                    print("The AI hit your hand 1 for 1 finger. It's at 2 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=2
                    print("The AI hit your hand 1 for 1 finger. It's at 2 fingers.")
                else:
                    print("Something broke")
            elif p_hand1==2:
                if p_hand2==1:
                    random_chance=random.randint(0,1)
                    if random_chance==1:
                        p_hand2=3
                        print("The AI hit your hand 2 for 1 finger. It's at 3 fingers.")
                    else:
                        p_hand1=2
                        print("The AI hit your hand 1 for 1 finger. It's at 2 fingers.")
                elif p_hand2==2:
                    p_hand2=3
                    print("The AI hit your hand 2 for 1 finger. It's at 3 fingers.")
                elif p_hand2==3:
                    p_hand1=3
                    print("The AI hit your hand 1 for 1 finger. It's at 3 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=3
                    print("The AI hit your hand 1 for 1 finger. It's at 3 fingers.")
                else:
                    print("Something broke")
            elif p_hand1==3:
                if p_hand2==1:
                    p_hand2=2
                    print("The AI hit your hand 2 for 1 finger. It's at 2 fingers.")
                elif p_hand2==2:
                    p_hand2=3
                    print("The AI hit your hand 2 for 1 finger. It's at 3 fingers.")
                elif p_hand2==3:
                    p_hand2=4
                    print("The AI hit your hand 2 for 1 finger. It's at 4 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=4
                    print("The AI hit your hand 1 for 1 finger. It's at 4 fingers.")
                else:
                    print("Something broke")
            elif p_hand1==4:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                else:
                    print("Something broke")
            elif p_hand1==0:
                if p_hand2==1:
                    p_hand2=2
                    print("The AI hit your hand 2 for 1 finger. It's at 2 fingers.")
                elif p_hand2==2:
                    p_hand2=3
                    print("The AI hit your hand 2 for 1 finger. It's at 3 fingers.")
                elif p_hand2==3:
                    p_hand2=4
                    print("The AI hit your hand 2 for 1 finger. It's at 4 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers. The AI won.")
                elif p_hand2==0:
                    print("Why did you combine? The AI won, I guess.")
                else:
                    print("Something broke")
    elif AI_hand2==2:############################################A FIFTH DONE!!!!
        if AI_hand1==1:
            if p_hand1==1:
                if p_hand2==1:
                    AI_hand1=3
                    AI_hand2=0
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand1=2
                    print("The AI hit your hand 1 for 1 finger. It's at 1 finger.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    AI_hand2=0
                    AI_hand1=3
                    print("The AI combined.")
                else:
                    print("Something broke")
            elif p_hand1==2:
                if p_hand2==1:
                    p_hand2=2
                    print("The AI hit your hand 2 for 1 finger. It's at 2 fingers.")
                elif p_hand2==2:
                    p_hand2=4
                    print("The AI hit your hand 2 for 2 fingers. It's at 4 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=4
                    print("The AI hit your hand 1 for 2 fingers. It's at 4 fingers.")
                else:
                    print("Something broke")
            elif p_hand1==3:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers. The AI won.")
            elif p_hand1==4:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers. The AI won.")
                else:
                    print("Something broke")
            elif p_hand1==0:
                if p_hand2==1:
                    AI_hand1=0
                    AI_hand2=3
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand2=4
                    print("The AI hit your hand 2 for 2 fingers. It's at 4 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers. The AI won.")
                elif P_hand2==0:
                    print("Why did you combine? The AI won, I guess.")
                else:
                    print("Something broke")
        elif AI_hand1==2:
            if p_hand1==1:
                if p_hand2==1:
                    p_hand2=3
                    print("The AI hit your hand 2 for 2 fingers. It's at 3 fingers.")
                elif p_hand2==2:
                    p_hand2=4
                    print("The AI hit your hand 2 for 2 fingers. It's at 4 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand2=1
                    print("The AI hit your hand 2 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==0:
                    AI_hand1=3
                    AI_hand2=1
                    print("The AI combined.")
                else:
                    print("Something broke")
            elif p_hand1==2:
                if p_hand2==1:
                    p_hand1=4
                    print("The AI hit your hand 1 for 2 fingers. It's at 4 fingers.")
                elif p_hand2==2:
                    p_hand1=4
                    print("The AI hit your hand 2 for 2 fingers. It's at 4 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=4
                    print("The AI hit your hand 1 for 2 fingers. It's at 4 fingers.")
                else:
                    print("Something broke")
            elif p_hand1==3:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers. The AI won.")
                else:
                    print("Something broke")
            elif p_hand1==4:
                if p_hand2==1:
                    p_hand1=1
                    print("The AI hit your hand 1 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==2:
                    p_hand1=1
                    print("The AI hit your hand 1 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=1
                    print("The AI hit your hand 1 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==0:
                    p_hand1=1
                    print("The AI hit your hand 1 for 2 fingers. It's down to 1 finger.")
                else:
                    print("Something broke")
            elif p_hand1==0:
                if p_hand2==1:
                    AI_hand1=3
                    AI_hand2=1
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand2=4
                    print("The AI hit your hand 2 for 2 fingers. It's at 4 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==4:
                    p_hand2=1
                    print("The AI hit your hand 2 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==0:
                    print("Why did you combine? The AI won, I guess.")
                else:
                    print("Something broke")
        elif AI_hand1==3:
            if p_hand1==1:
                if p_hand2==1:
                    p_hand1=4
                    print("The AI hit your hand 1 for 3 fingers. It's at 4 fingers.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=3
                    print("The AI hit your hand 1 for 2 fingers. It's at 3 fingers.")
                elif p_hand2==0:
                    p_hand1=3
                    print("The AI hit your hand 1 for 2 fingers. It's at 3 fingers.")
                else:
                    print("Something broke")
            elif p_hand1==2:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers. The AI won.")
                else:
                    print("Something broke")
            elif p_hand1==3:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers. The AI won.")
            elif p_hand1==4:
                if p_hand2==1:
                    p_hand2=3
                    print("The AI hit your hand 2 for 2 fingers. It's at 3 fingers.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand2=1
                    print("The AI hit your hand 2 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==0:
                    p_hand1=1
                    print("The AI hit your hand 1 for 2 fingers. It's down to 1 finger.")
            elif p_hand1==0:
                if p_hand2==1:
                    p_hand2=3
                    print("The AI hit your hand 2 for 2 fingers. It's at 3 fingers.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==4:
                    p_hand2=1
                    print("The AI hit your hand 2 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==0:
                    print("Why did you combine? The AI won, I guess.")
                else:
                    print("Something broke")
        elif AI_hand1==4:
            if p_hand1==1:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    AI_hand1=3
                    AI_hand2=3
                    print("The AI combined.")
                elif p_hand2==3:
                    p_hand1=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers. The AI won.")
                else:
                    print("Something broke")
            elif p_hand1==2:
                if p_hand2==1:
                    AI_hand1=3
                    AI_hand2=3
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand2=4
                    print("The AI hit your hand 2 for 2 finger. It's at 4 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=4
                    print("The AI hit your hand 1 for 2 fingers. It's at 4 fingers.")
                elif p_hand2==0:
                    p_hand1=1
                    print("The AI hit your hand 1 for 4 fingers. It's down to 1 finger.")
                else:
                    print("Something broke")
            elif p_hand1==3:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers. The AI won.")
                else:
                    print("Something broke")
            elif p_hand1==4:
                if p_hand2==1:
                    p_hand1=1
                    print("The AI hit your hand 1 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==2:
                    AI_hand1=3
                    AI_hand2=3
                    print("The AI combined")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    AI_hand1=3
                    AI_hand2=3
                    print("The AI combined")
                elif p_hand2==0:
                    p_hand1=1
                    print("The AI hit your hand 1 for 2 fingers. It's down to 1 finger.")
                else:
                    print("Something broke")
            elif p_hand1==0:
                if p_hand2==1:
                    p_hand2=0
                    print("The AI hit your hand 2 for 4 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==2:
                    p_hand2=1
                    print("The AI hit your hand 2 for 4 fingers. It's down to 1 finger.")
                elif p_hand2==3:
                    AI_hand1=3
                    AI_hand2=3
                    print("The AI combined")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers. The AI won.")
                elif p_hand2==0:
                    print("Why did you combine? The AI won, I guess.")
                else:
                    print("Something broke")
        elif AI_hand1==0:
            if p_hand1==1:
                if p_hand2==1:
                    AI_hand1=1
                    AI_hand2=1
                    print("The AI combined.")
                elif p_hand2==2:
                    AI_hand1=1
                    AI_hand2=1
                    print("The AI combined.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand2=1
                    print("The AI hit your hand 2 for 1 finger. It's down to 1 finger.")
                elif p_hand2==0:
                    AI_hand1=1
                    AI_hand2=1
                    print("The AI combined.")
                else:
                    print("Something broke")
            elif p_hand1==2:
                if p_hand2==1:
                    AI_hand1=1
                    AI_hand2=1
                    print("The AI combined.")
                elif p_hand2==2:
                    AI_hand1=1
                    AI_hand2=1
                    print("The AI combined.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand2=1
                    print("The AI hit your hand 2 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==0:
                    AI_hand1=1
                    AI_hand2=1
                    print("The AI combined.")
                else:
                    print("Something broke")
            elif p_hand1==3:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    AI_hand1=1
                    AI_hand2=1
                    print("The AI combined.")
                elif p_hand2==4:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers. The AI won.")
            elif p_hand1==4:
                if p_hand2==1:
                    AI_hand1=1
                    AI_hand2=1
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand1=1
                    print("The AI hit your hand 1 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==0:
                    p_hand1=1
                    print("The AI hit your hand 1 for 2 fingers. It's down to 1 finger.")
            elif p_hand1==0:
                if p_hand2==1:
                    AI_hand1=1
                    AI_hand2=1
                    print("The AI combined.")
                elif p_hand2==2:
                    random_chance=random.randint(0,1)
                    if random_chance==1:
                        AI_hand1=1
                        AI_hand2=1
                        print("The AI combined.")
                    else:
                        p_hand2=4
                        print("The AI hit your hand 2 for 2 fingers. It's at 4 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand2=1
                    print("The AI hit your hand 2 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==0:
                    print("Why did you combine? The AI won, I guess.")
    elif AI_hand2==3:#############HALF WAY!!EVEN MORE THAN HALF!!!!
        if AI_hand1==1:
            if p_hand1==1:
                if p_hand2==1:
                    AI_hand1=2
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    AI_hand1=2
                    AI_hand2=2
                    print("The AI combined.")
            elif p_hand1==2: #This is supposed to be like this.
                if p_hand2==2:
                    AI_hand1=2
                    AI_hand2=2
                    print("The AI combined.")
                else:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
            elif p_hand1==3:
                if p_hand2==1:
                    p_hand1=1
                    print("The AI hit your hand 1 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers.")
                elif p_hand2==0:
                    p_hand1=1
                    print("The AI hit your hand 1 for 3 fingers. It's down to 1 finger.")
            elif p_hand1==4:
                p_hand1=0
                print("The AI hit your hand 1 for 1 finger. It's down to 0 fingers.")
            elif p_hand1==0:
                if p_hand2==1:
                    AI_hand1=2
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==4:
                    p_hand2=0
                    print("The AI hit your hand 2 for 1 finger. It's down to 0 fingers. The AI won.")
                elif p_hand2==0:
                    print("Why would you combine? The AI won, I guess.")
        elif AI_hand1==2:
            if p_hand1==1:
                if p_hand2==1:
                    p_hand1=4
                    print("The AI hit your hand 1 for 3 fingers. It's at 4 fingers.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==4:
                    p_hand1=3
                    print("The AI hit your hand 1 for 2 fingers. It's at 3 fingers.")
                elif p_hand2==0:
                    p_hand1=4
                    print("The AI hit your hand 1 for 3 fingers. It's at 4 fingers.")
            elif p_hand1==2:
                p_hand1=0
                print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
            elif p_hand1==3:
                p_hand1=0
                print("The AI hit your hand 1 for 2 fingers. It's down to 0 fingers.")
            elif p_hand1==4:
                if p_hand2==1:
                    p_hand1=1
                    print("The AI hit your hand 1 for 2 fingers. It's down to 1 finger.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                else:
                    p_hand1=1
                    print("The AI hit your hand 1 for 2 fingers. It's down to 1 finger.")
            elif p_hand1==0:
                if p_hand2==1:
                    p_hand2=3
                    print("The AI hit your hand 2 for 2 fingers. It's at 3.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's at 0 fingers. The AI won.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's at 0 fingers. The AI won.")
                elif p_hand2==4:
                    p_hand2=1
                    print("The AI hit your hand 2 for 2 fingers. It's at 1 fingers.")
        elif AI_hand1==3:
            if p_hand1==1:
                if p_hand2==1:
                    p_hand1=4
                    print("The AI hit your hand 1 for 3 fingers. It's at 4 fingers.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==4:
                    p_hand2=2
                    print("The AI hit your hand 2 for 3 fingers. It's down to 2 fingers.")
                elif p_hand2==0:
                    AI_hand1=2
                    AI_hand2=4
                    print("The AI combined.")
            elif p_hand1==2:
                p_hand1=0
                print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
            elif p_hand1==3:
                if p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                else:
                    p_hand1=1
                    print("The AI hit your hand 1 for 3 fingers. It's down to 1 finger.")
            elif p_hand1==4:
                if p_hand2==1:
                    p_hand1=2
                    print("The AI hit your hand 1 for 3 fingers. It's down to 2 fingers.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==4:
                    random_chance=random.randint(0,1)
                    if random_chance==1:
                        AI_hand1=4
                        AI_hand2=2
                        print("The AI combined.")
                    else:
                        p_hand2=2
                        print("The AI hit your hand 2 for 4 fingers. It's down to 2 fingers.")
                elif p_hand2==0:
                    p_hand1=2
                    print("The AI hit your hand 2 for 3 fingers. It's down to 2 fingers.")
            elif p_hand1==0:
                if p_hand2==1:
                    AI_hand1=4
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==4:
                    p_hand2=2
                    print("The AI hit your hand 2 for 3 fingers. It's down to 2 fingers.")
                elif p_hand2==0:
                    print("Why did you combine? The AI won, I guess.")
        elif AI_hand1==4:
            if p_hand1==1:
                if p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                else:
                    p_hand1=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers.")
            elif p_hand1==2:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=0
                    print("The AI hit your hand 2 for 2 fingers. It's at 0 fingers.")
                elif p_hand2==4:
                    AI_hand1=3
                    AI_hand2=3
                    print("The AI combined.")
                elif p_hand2==0:
                    p_hand1=1
                    print("The AI hit your hand 1 for 4 fingers. It's at 1 finger.")
            elif p_hand1==3:
                if p_hand2==1:
                    p_hand1=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
                else:
                    p_hand1=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
            elif p_hand1==4:
                if p_hand2==1:
                    p_hand2=0
                    print("The AI hit your hand 2 for 4 fingers. It's down to 0 fingers.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand1=3
                    print("The AI hit your hand 1 for 4 fingers. It's down to 3 fingers.")
                elif p_hand2==4:
                    p_hand1=3
                    print("The AI hit your hand 1 for 4 fingers. It's down to 3 fingers.")
                elif p_hand2==0:
                    AI_hand1=1
                    AI_hand2=1
                    print("The AI combined.") #Me while editing wonders why there's no "elif p_hand1==0"
            else:
                print("Something broke, somehow, somehow.")
        elif AI_hand1==0:
            if p_hand1==1:
                if p_hand2==1:
                    p_hand1=4
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==4:
                    AI_hand2=2
                    AI_hand1=1
                    print("The AI combined.")
                elif p_hand2==0:
                    AI_hand1=1
                    AI_hand2=2
                    print("The AI combined.")
            elif p_hand1==2:
                if p_hand2==2:
                    AI_hand1=1
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==3:
                    AI_hand1=2
                    AI_hand2=1
                    print("The AI combined.")
                else:
                    p_hand1=0
                    print("The AI hit your hand 1 for 3 fingers. It's down to 0 fingers.")
            elif p_hand1==3:
                if p_hand2==1:
                    p_hand1=1
                    print("The AI hit your hand 1 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==2:
                    AI_hand1=2
                    AI_hand2=1
                    print("The AI combined.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==4:
                    p_hand1=1
                    print("The AI hit your hand 1 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==0:
                    p_hand1=1
                    print("The AI hit your hand 1 for 3 fingers. It's down to 1 finger.")
            elif p_hand1==4:
                if p_hand2==1:
                    AI_hand1=1
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                else:
                    AI_hand1=1
                    AI_hand2=2
                    print("The AI combined.")
            elif p_hand1==0:
                if p_hand2==1:
                    AI_hand1=1
                    AI_hand2=2
                    print("The AI combined.")
                elif p_hand2==2:
                    p_hand2=0
                    print("The AI hit your hand 2 for 3 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==3:
                    p_hand2=1
                    print("The AI hit your hand 2 for 3 fingers. It's down to 1 finger.")
                elif p_hand2==4:
                    AI_hand1=2
                    AI_hand2=1
                    print("The AI combined.")
    elif AI_hand2==4:
            if AI_hand1==4:
                print("This is the built in way to win. It should be extremely hard to make the AI get two 4s, so I'm going to give you a choice. I can have you win instantly, or I can have the AI keep playing, your choice. Inputs are:")
                p_response3=input("Yes, I want to win, or no, I don't. No caps.\n")
                if p_response3=="yes":
                    print("OK, here is your free win. Congrats!")
                    sys.exit()
                elif p_response3=="no":
                    if p_hand1 == 1:
                        if p_hand2==2:
                            AI_hand1=1
                            AI_hand2=2
                            print("The AI combined.")
                        else:
                            p_hand1=0
                            print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers.")
                    elif p_hand1 == 2:
                        if p_hand2==1:
                            p_hand2=0
                            print("The AI hit your hand 2 for 4 fingers. It's down to 0 fingers.")
                        elif p_hand2==2:
                            AI_hand1=1
                            AI_hand2=2
                            print("The AI combined.")
                        elif p_hand2==3:
                            p_hand2=2
                            print("The AI hit your hand 2 for 4 fingers. It's down to 2 fingers.")
                        elif p_hand2==4:
                            p_hand1=1
                            print("The AI hit your hand 1 for 4 fingers. It's down to 1 finger.")
                        elif p_hand2==0:
                            p_hand2=1
                            print("The AI hit your hand 2 for 4 fingers. It's down to 1 finger.")
                    elif p_hand1==3:
                        if p_hand2==1:
                            p_hand2=0
                            print("The AI hit your hand 2 for 4 fingers. It's down to 0 fingers.")
                        else:
                            p_hand1=p_hand1-1
                            print(f"The AI hit your hand 1 for 4 fingers. It's down to {p_hand1} fingers. []") #the [ ] is here so that in case I want to investigate the plurals, I can Ctrl F for it.
                    elif p_hand1==4:
                        if p_hand2==1:
                            p_hand2=0
                            print("The AI hit your hand 2 for 4 fingers. It's down to 0 fingers.")
                        else:
                            p_hand1=p_hand1-1
                            print(f"The AI hit your hand 1 for 4 fingers. It's down to {p_hand1} fingers. ||") #the | | is the same as above
                    elif p_hand1==0:
                        if p_hand2==1:
                            p_hand2=0
                            print("The AI hit your hand 2 for 4 fingers. It's down to 0 fingers.")
                        elif p_hand2==2:
                            p_hand2=1
                            print("The AI hit your hand 2 for 4 fingers. It's down to 1 finger.")
                        elif p_hand2==3:
                            p_hand2=2
                            print("The AI hit your hand 2 for 4 fingers. It's down to 2 fingers.")
                        elif p_hand2==4:
                            AI_hand1=1
                            AI_hand2=2
                            print("The AI combined.")

                else:
                    print("Um... you broke it. I'm going to say it's a tie. You should've put in either 'yes' or 'no'")
                    sys.exit()
            elif AI_hand1==0:
                if p_hand1==0:
                    if p_hand2==1:
                        p_hand2=0
                        print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers. The AI won.")
                    else: #this is if the AI has a 0 and a 4.
                        AI_hand1=2
                        AI_hand2=2
                        print("The AI combined.")
                elif p_hand1==1:
                    if p_hand2==0:
                        p_hand1=0
                        print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers. The AI won.")
                    elif p_hand2==1:
                        AI_hand1=3
                        AI_hand2=1
                        print("The AI combined.")
                    else:
                        AI_hand1=2
                        AI_hand2=2
                        print("The AI combined.")
                else: #this is if the AI has a 0 and a 4.
                    AI_hand1=2
                    AI_hand2=2
                    print("The AI combined.")
            else:
                print("Something broke. Somehow.")
    elif AI_hand2==0: ##########SOOOOOOO CLOSE!! BTW, it's exactly 8AM on the fourteenth of December 2024. Ig I'm also close to Cristmas. The 3rd week of advent is tomorrow.
        if AI_hand1==4:
            if p_hand1==0:
                if p_hand2==1:
                    p_hand2=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers. The AI won.")
                else: #this is if the AI has a 0 and a 4.
                    AI_hand1=2
                    AI_hand2=2
                    print("The AI combined.")
            elif p_hand1==1:
                if p_hand2==0:
                    p_hand1=0
                    print("The AI hit your hand 1 for 4 fingers. It's down to 0 fingers. The AI won.")
                elif p_hand2==1:
                    AI_hand1=3
                    AI_hand2=1
                    print("The AI combined.")
                else:
                    AI_hand1=2
                    AI_hand2=2
                    print("The AI combined.")
            else:
                AI_hand1=2
                AI_hand2=2
                print("The AI combined.")
        else:
            print("Something broke. Somehow.")
    else:
        print("Something broke, somehow.")
    if swap_boolean==1:
        sswap()
        swap_boolean=0

while True:
    if nothing>1:
        if turns_per_p == 1:
            turns_lasted += 1
            player_turn()
            check()
            AI_turn()
            check()
        elif turns_per_p == 2:
            turns_lasted += 1
            player_turn()
            check()
            turns_lasted += 1
            player_turn()
            check()
            AI_turn()
            check()
            AI_turn()
            check()
        elif turns_per_p == 3:
            turns_lasted += 1
            player_turn()
            check()
            turns_lasted += 1
            player_turn()
            check()
            turns_lasted += 1
            player_turn()
            check()
            AI_turn()
            check()
            AI_turn()
            check()
            AI_turn()
            check()
    else:
        nothing+=1
        if nothing1==1:
            player_response0=input("Do you want to start? The inputs are, 'yes' or 'no' or 'random'.\n")
            if player_response0=="random" or player_response0=="r":
                random_chance=random.randint(0, 1)
                if random_chance==1:
                    player_response0="no"
                    print("The AI starts.")
            if player_response0=="no" or player_response0=="n":
                AI_turn()
                check()
        else:
            nothing1=1
            print("Welcome to my Chopsticks AI!! This is a pre-programmed AI that's meant to never lose. But that might not be true! Try and see if you can beat it!!")

