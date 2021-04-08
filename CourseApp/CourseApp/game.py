import os
from classes import Player, Game

player_1_name = input()
player_2_name = input()
print("Player 1 choose your item (1 - Rock, 2 - Scissors, 3 - Paper): ", end='')
player_1_choice = int(input())
os.system("cls")
print("Player 2 choose your item (1 - Rock, 2 - Scissors, 3 - Paper): ", end='')
player_2_choice = int(input())
os.system("cls")

firstgame = Game(player_1_name, player_2_name)
firstgame.set_player_1_choice(player_1_choice)
firstgame.set_player_2_choice(player_2_choice)
firstgame.winner()