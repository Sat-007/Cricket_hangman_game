import os
import random    # THIS HERE IS USED TO randomly select platyers from the list
import pandas as pd
import sqlite3
from chosen_player import player
               

sat007 = [r'''
/ ___|  / \|_   _/ _ \ / _ \___  |
\___ \ / _ \ | || | | | | | | / / 
 ___) / ___ \| || |_| | |_| |/ /  
|____/_/   \_\_| \___/ \___//_/   
            ''']


hangmanicons = [r'''
   +---+
       |
       |
       |
      ===''', r'''
   +---+
   O   |
       |
       |
      ===''', r'''
   +---+
   O   |
   |   |
       |
      ===''', r'''
   +---+
   O   |
  /|   |
       |
      ===''', r'''
   +---+
   O   |
  /|\  |
       |
      ===''', r'''
   +---+
   O   |
  /|\  |
  /    |
      ===''', r'''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

#First let us randmly select a player from our list
selected_player = player()             #player() is in chosen_player.py which we select a random player

os.system("clear")

answer = []
guessed = []
game_over = False
counter = 6
print(f"\n{' '.join(sat007)}\n\n ")

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for _ in range(len(selected_player)):
    answer += "_"
print( f"\t\t{' '.join(answer)}" )
print( hangmanicons[0] )

while not game_over:
    guessed_player  = input("\n Guess a Letter: ").lower()
    if guessed_player in guessed:
        print(f"\t\tYou already guessed '{guessed_player}'!")
    else:
        guessed.append(guessed_player)  # Add guess to list

    # Check if guess is in the word
    is_correct = False

    for point in range(len(selected_player)):
      letter_in_word = selected_player[point]
      if guessed_player == letter_in_word:
        answer[point] = guessed_player
        is_correct = True

    # Update counter based on guess
    if not is_correct:
      counter -= 1
    print(f"\n{' '.join(sat007)}\n\n")
    if counter <= 6:
       diff = abs(counter - 6)  #Just used to print the icons
       print(hangmanicons[diff])

    for position in range(len(alphabet)):
        letter_in_alphabet = alphabet[position]
        if guessed_player == letter_in_alphabet:
            alphabet[position] = "-"

    print(f"{' '.join(alphabet)}\n")
    print(f"\t\t{' '.join(answer)}")

    game_over = counter == 0 or "_" not in answer
    if game_over:
      if counter == 0:
        os.system("cls")
        print(hangmanicons[6])
        print(f"\n\n-------YOU LOST!--------\n")
        print(f"The Player was ---> {selected_player}\n")
      else:
        os.system("cls")
        print(f"\nThe Player was ---> {selected_player}\n")
        print(f"\n\n Congratulations! YOU WON THE GAME :)\n")
 

















'''
    if guessed_player in guessed:
        print(bcolors.FAIL + f"\t\t You already guessed '{guessed_player}'!" +  bcolors.ENDC)
    elif guessed_player not in guessed:
        if guessed_player not in selected_player:
            counter = counter - 1
        guessed += guessed_player



    for point in range(len(selected_player)):
        letter_in_word = selected_player[point]
        if guessed_player == letter_in_word:
            answer[point] = guessed_player

    for position in range(len(alphabet)):
        letter_in_alphabet = alphabet[position]
        if guessed_player == letter_in_alphabet:
            alphabet[position] = "-"

    guessed += guessed_player

    print(bcolors.GREEN + f"\n{' '.join(sat007)}\n\n" + bcolors.ENDC)
    print(bcolors.UNDERLINE + f"{' '.join(alphabet)}\n" + bcolors.ENDC)
    print(bcolors.BLUE + f"\t\t{' '.join(answer)}" + bcolors.ENDC)

    if counter ==6:
        print(bcolors.CYAN + hangmanicons[0] + bcolors.ENDC)
    if counter==5:
        print(bcolors.CYAN + hangmanicons[1] + bcolors.ENDC)
    if counter==4:
        print(bcolors.CYAN + hangmanicons[2] + bcolors.ENDC)
    if counter==3:
        print(bcolors.CYAN + hangmanicons[3] + bcolors.ENDC)
    if counter==2:
        print(bcolors.CYAN + hangmanicons[4] + bcolors.ENDC)
    if counter == 1:
        print(bcolors.CYAN + hangmanicons[5] + bcolors.ENDC)






    if counter == 0:
        print(bcolors.CYAN + hangmanicons[6] + bcolors.ENDC)
        game_over = True
        print(bcolors.FAIL + f"\n\n-------YOU LOST!--------\n" + bcolors.ENDC)
        print(bcolors.FAIL + f"The Player was --->  " + bcolors.ENDC + bcolors.GREEN + f"{selected_player}\n" + bcolors.ENDC)
    if "_" not in answer:
        game_over = True
        print(bcolors.HEADER+ "\n\n Congratulations!\n YOU WON THE GAME :)\n" + bcolors.ENDC)


'''