import os

class Game:
    def __init__(self, first_user_name, second_user_name):
        self.__fisrt_user_name = first_user_name
        self.__second_user_name = second_user_name
        self.__first_user_choice = 0
        self.__second_user_choice = 0
        self.__first_user_item = "nothing"
        self.__second_user_item = "nothing"

    def set_first_user_choice(self,first_user_choice):
        if first_user_choice in range(1,4):
            self.__first_user_choice = first_user_choice
        else:
            print("Wrong choice")

    def set_second_user_choice(self,second_user_choice):
        if second_user_choice in range(1,4):
            self.__second_user_choice = second_user_choice
        else:
            print("Wrong choice")
    
    def set_first_user_item(self):
        if self.__first_user_choice is 1:
            self.__first_user_item = "Rock"
        elif self.__first_user_choice is 2:
            self.__first_user_item = "Scissors"
        elif self.__first_user_choice is 3:
            self.__first_user_item = "Paper"

    def set_second_user_item(self):
        if self.__second_user_choice is 1:
            self.__second_user_item = "Rock"
        elif self.__second_user_choice is 2:
            self.__second_user_item = "Scissors"
        elif self.__second_user_choice is 3:
            self.__second_user_item = "Paper"

    def get_fist_user_name(self):
        return self.__fisrt_user_name

    def get_second_user_name(self):
        return self.__second_user_name
        
    def winner(self):
        if self.__first_user_choice - self.__second_user_choice == -1 or self.__first_user_choice - self.__second_user_choice == 2:
            print(f'{self.__fisrt_user_name} chose {self.__first_user_item} against {self.__second_user_name} chose {self.__second_user_item} => {self.__fisrt_user_name} wins')
        elif self.__first_user_choice == self.__second_user_choice:
            print(f'Draw, because both players chose {self.__first_user_choice}')
        else:
            print(f'{self.__fisrt_user_name} chose {self.__first_user_item} against {self.__second_user_name} chose {self.__second_user_item} => {self.__second_user_name} wins')


first_user_name = input()
second_user_name = input()
print("Player 1 choose your item (1 - Rock, 2 - Scissors, 3 - Paper): ", end='')
first_user_choice = int(input())
os.system("cls")
print("Player 2 choose your item (1 - Rock, 2 - Scissors, 3 - Paper): ", end='')
second_user_choice = int(input())
os.system("cls")

first = Game(first_user_name, second_user_name)
first.set_first_user_choice(first_user_choice)
first.set_first_user_item()
first.set_second_user_choice(second_user_choice)
first.set_second_user_item()
first.winner()