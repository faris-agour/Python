import random
import time

import pyfiglet
from colorama import init, Fore

init()

# Define the suits and ranks
suit = "H D S C".split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()

# Create the deck of cards and shuffle it
cards = [(r, s) for r in ranks for s in suit]
random.shuffle(cards)

# some var
flag = True
flag1 = True
round = 1
points = 0

# Stash for computer and player
com = []
ply = []
com_stash = []
ply_stash = []


# the delay functions
def print_with_delay(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.03)
    return ''


def print_with_delay_faster(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.009)
    return ''


def print_with_delay_V_faster(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.00000001)
    return ''


# GAME STARTED
print_with_delay_V_faster(Fore.CYAN + pyfiglet.figlet_format("WELCOME to - WAR CARD - GAME\n", width=170) + Fore.RESET)
time.sleep(1)

# plyer name
plyName = input(print_with_delay("\n>> What's your name? "))
print_with_delay_faster(
    Fore.MAGENTA + "\n In this game you and com will play 2 cards \n Whose card has bigger number, will take the cards\n"
                   " AT tie you both take 3 cards\n\n" + Fore.RESET)
time.sleep(1)

# while for repeating the game
while flag:
    # choose the mode of the game
    random.shuffle(cards)
    com = []
    ply = []
    while flag1:
        round_num = input(print_with_delay_faster(
            "\n>> If you want the full '26' rounds (press '1'), for '16' rounds (press '2'), and (press '3') for '10' rounds : "))
        if (round_num == '1'):
            com = cards[:26]
            ply = cards[26:]
            flag1 = False
        elif (round_num == '2'):
            com = cards[:16]
            ply = cards[36:]
            flag1 = False
        elif (round_num == '3'):
            com = cards[:10]
            ply = cards[42:]
            flag1 = False
        else:
            print("\n Invalid input .. try again ")
            flag1 = True
    print_with_delay_faster("\n-------- OK LET'S PLAY --------")
    random.shuffle(cards)
    com_stash = []
    ply_stash = []
    time.sleep(1)
    round = 0
    while com and ply:
        com_card = com.pop()
        ply_card = ply.pop()
        print("\n\n Your card is : " + str(ply_card))
        print(" Com card is : " + str(com_card))
        time.sleep(.12)

        if com_card[0] == ply_card[0]:
            if len(ply) > 3:
                com_stash.extend([com_card] + com[-3:])
                com = com[:-3]
                com.append(com_stash.pop())
                ply_stash.extend([ply_card] + ply[-3:])
                ply = ply[:-3]
                ply.append(ply_stash.pop())
            else:
                # com_stash.extend([com_card] + com[-1:])
                # com = com[:-1]
                # com.append(com_stash.pop())
                # ply_stash.extend([ply_card] + ply[-1:])
                # ply = ply[:-1]
                # ply.append(ply_stash.pop())
                pass

            print_with_delay(Fore.LIGHTYELLOW_EX + "\n The round is a tie." + Fore.RESET)
            time.sleep(.1)
            print_with_delay_faster(
                "\n\n Your score: " + str(len(ply_stash)) + "\n Com's score: " + str(len(com_stash)))

        elif (com_card[0] == 'A') or (com_card[0] == 'K' and ply_card[0] != 'A') or \
                (com_card[0] == 'Q' and ply_card[0] not in ['A', 'K']) or \
                (com_card[0] == 'J' and ply_card[0] not in ['A', 'K', 'Q']) or \
                (com_card[0] == '10' and ply_card[0] not in ['A', 'K', 'Q', 'J']) or \
                (com_card[0] > ply_card[0] and com_card[0] != 'A' and com_card[0] != 'K' and com_card[0] != 'Q' and
                 com_card[0] != 'J' and ply_card[0] != '10'):
            com_stash.extend([com_card] + [ply_card])
            print_with_delay(Fore.RED + "\n Computer wins." + Fore.RESET)
            time.sleep(.1)
            print_with_delay_faster(
                "\n\n Your score: " + str(len(ply_stash)) + "\n Com's score: " + str(len(com_stash)))

        else:
            ply_stash.extend([com_card] + [ply_card])
            print_with_delay(Fore.GREEN + "\n " + plyName + " wins." + Fore.RESET)
            time.sleep(.1)
            print_with_delay_faster(
                "\n\n Your score: " + str(len(ply_stash)) + "\n Com's score: " + str(len(com_stash)))

        time.sleep(.1)
        print_with_delay_faster("\n\n\t" + str(len(ply)) + " card left for each one\n")
        print("_" * 55)
        time.sleep(.001)

        round += 1
        if len(ply) != 0:
            input("\n>> Press enter for round " + str(round) + " :: ")

    if len(com_stash) > len(ply_stash):
        print_with_delay(Fore.LIGHTMAGENTA_EX + "\n\n\tHARD LUCK NEXT TIME ... com is the winner \n\n" + Fore.RESET)
        points -= 10
    elif len(com_stash) == len(ply_stash):
        print_with_delay(Fore.LIGHTRED_EX + "\n\n\tWOW IT'S DRAW ... GOOD GAME \n\n" + Fore.RESET)
        points += 5
    else:
        print_with_delay_V_faster(
            Fore.CYAN + pyfiglet.figlet_format("\nCONGRATS YOU ARE THE WINNER !\n\n", font="bubble",
                                               width=500) + Fore.RESET)
        points += 10
    print_with_delay_faster(Fore.LIGHTRED_EX + f" Your score is {points} \n\n Press enter to continue  : " + Fore.RESET)
    y = input()
    flag = True
    flag1 = True
