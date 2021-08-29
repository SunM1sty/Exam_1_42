class Player:
    def __init__(self,nickname):
        self.nickname = nickname

class Game:

    __items = {1: 'Rock', 2: 'Scissors', 3:'Paper'}

    def __init__(self,player_1_name, player_2_name):
        self.player_1 = Player(player_1_name)
        self.player_2 = Player(player_2_name)
        self.__player_1_choice = 0
        self.__player_2_choice = 0

    def set_player_1_choice(self,player_1_choice):
        if player_1_choice in range(1,4):
            self.__player_1_choice = player_1_choice
        else:
            print("Wrong choice")

    def set_player_2_choice(self,player_2_choice):
        if player_2_choice in range(1,4):
            self.__player_2_choice = player_2_choice
        else:
            print("Wrong choice")
        
    def winner(self):
        if self.__player_1_choice - self.__player_2_choice == -1 or self.__player_1_choice - self.__player_2_choice == 2:
            print(f'{self.player_1.nickname} chose {self.__items[self.__player_1_choice]} VS {self.player_2.nickname}: {self.__items[self.__player_2_choice]} \n{self.player_1.nickname} wins')
        elif self.__player_1_choice == self.__player_2_choice:
            print(f'Draw, because both players chose {self.__items[self.__player_1_choice]}')
        else:
            print(f'{self.player_1.nickname}: {self.__items[self.__player_1_choice]} VS {self.player_2.nickname}: {self.__items[self.__player_2_choice]} \n{self.player_2.nickname} wins')
            
try:
    k = 1 / 0
except ArithmeticError:
    k = 0
print(k) # 0
