""" create a game that guess the number """

import random
import time
import pyfiglet
from colorama import init, Fore

init()
flag = True
flag1 = True
flag2 = True
flag3 = True
xp = 0


def print_with_delay(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.04)
    return ''


def print_with_delay_faster(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.01)
    return ''


def print_with_delay_V_faster(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.00000001)
    return ''


print_with_delay_V_faster(Fore.MAGENTA + pyfiglet.figlet_format(" WELCOME to - RANDNUM - GAME", width=200) + Fore.RESET)
time.sleep(.6)
while flag2:

    print_with_delay("\n\n>> what's your name ? ")
    name = input()
    print("\n")
    time.sleep(.3)
    if name.isalpha() and len(name) > 2:
        flag2 = False
    else:
        print(" XXXX  Name only contain alphabets and more than 2 XXXX ")
        print("\n")
        time.sleep(.1)

print_with_delay_faster(Fore.LIGHTBLUE_EX + f" Ok {name}, can you guess the NUM \n\n"
                                            f" Some hints : \n"
                                            f"    +++ or --- means increase or decrease by 10 or MO0RE  \n"
                                            f"    + or - is the same but less than 10 \n\n" + Fore.RESET)

time.sleep(.2)
while flag:
    while flag1:
        while flag3:
            print_with_delay_faster(
                " >> Choose the level :- ( 1 --> easy [-100:100] ), ( 2 --> medium [-200:200]), ( 3 --> hard [-400:400]) : ")
            level = input()
            if level == '1':
                n = 100
                print_with_delay_faster(Fore.LIGHTGREEN_EX + "\n\t--- 0h you take the easy one ---\n\n" + Fore.RESET)
                flag1 = False
                flag3 = False
            elif level == '2':
                n = 200
                flag1 = False
                flag3 = False
                print_with_delay_faster(Fore.LIGHTYELLOW_EX + "\n\t--- Great you choose number 2 ---\n\n" + Fore.RESET)
            elif level == '3':
                n = 400
                print_with_delay_faster(Fore.YELLOW + "\n\t--- Wow let's see what you got : ---\n\n" + Fore.RESET)
                flag1 = False
                flag3 = False
            else:
                flag1 = True
                flag3 = True
                print("\n It's not valid , just choose 1,2 or 3 !! \n\n\n")
                time.sleep(.2)

    time.sleep(.2)

    # highest range

    a = round(n * random.random())

    # lowest range
    b = round(-n * random.random())

    # the number you should guess
    x = round(random.uniform(a, b))

    print_with_delay_faster("\n* * * *  YOU HAVE 7 ATTEMPS ... G00D LUCK   * * * * \n\n\n")
    time.sleep(0.5)

    for i in range(7):

        print_with_delay_faster(" >> Guess the number : ")

        try:
            z = int(input())
        except ValueError:
            print()
            print_with_delay("\n This is not an int number you have lost an attempt \n\n")
            print("\n" + "-" * 60 + "\n")
            print_with_delay_faster(f"\n\t\t Now you have {6 - i} attemps left \n\n")
            print("\n")
            continue
        print("\n" + "-" * 60)
        if z == x:
            xp += 10
            print_with_delay_V_faster(Fore.GREEN + pyfiglet.figlet_format("\n CONGRATS - YOU WIN  \n\n", font="cosmic",
                                                                          width=600) + Fore.RESET)
            print_with_delay_faster(
                Fore.BLUE + " " + str(z) + " was correct \n your score now = \"" + str(xp) + "\"\n" + Fore.RESET)
            break
        else:
            if i < 3:
                print_with_delay_faster(f"\n\t\t  you have {6 - i} attemps left \n\n")

            elif i < 6:
                print_with_delay_faster(
                    Fore.MAGENTA + f"\n\t  BE CAREFUL you only have {6 - i} attempts \n\n" + Fore.RESET)

            else:
                print_with_delay(Fore.RED + "\n\t:::::::: GAME OVER YOU LOST ::::::::\n\n" + Fore.RESET)
                xp -= 10
                print_with_delay_faster(Fore.BLUE + f" the correct num was '{x}'\n your score now is {xp}" + Fore.RESET)
                break

            if z + 10 < x:
                print(Fore.YELLOW + "\n\t\t  (( guess higher +++ ))" + Fore.RESET)
            elif z < x:
                print(Fore.LIGHTYELLOW_EX + "\n\t\t(   little more + )" + Fore.RESET)
            elif z - 10 > x:
                print(Fore.RED + "\n\t\t (( guess more lower --- ))" + Fore.RESET)
            else:
                print(Fore.LIGHTRED_EX + "\n\t\t(   little fewer - )" + Fore.RESET)
            print("\n")

    print("\n")
    flag4 = True
    while flag4:
        print_with_delay_faster(">> Press ENTER to continue : ")
        c = input()
        flag4 = False
    flag = True
