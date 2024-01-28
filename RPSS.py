##########################################
#Aziza Alam, Jermaine Bell, Laurent Pierre
#MSIT 0660
#Project 4
#Professor Cobo
###########################################

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.statistics = Statistics()

    def choose_weapon(self):
        choice = input(f"{self.name}, choose your weapon (Rock, Paper, Scissors, Saw): ").capitalize()
        while choice not in ['Rock', 'Paper', 'Scissors', 'Saw']:
            print("Invalid choice. Please choose Rock, Paper, Scissors, or Saw.")
            choice = input(f"{self.name}, choose your weapon (Rock, Paper, Scissors, Saw): ").capitalize()
        return choice

    def update_statistics(self, result):
        self.statistics.update_stats(result)

    def __str__(self):
        return self.name

class Statistics:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def update_stats(self, result):
        if result == "win":
            self.wins += 1
        elif result == "loss":
            self.losses += 1
        elif result == "tie":
            self.ties += 1

    def display_stats(self):
        return f"Wins: {self.wins}, Losses: {self.losses}, Ties: {self.ties}"

class Game:
    def __init__(self):
        self.players = []
        self.win_conditions = {
            'Rock': ['Scissors', 'Saw'],
            'Paper': ['Rock'],
            'Scissors': ['Paper'],
            'Saw': ['Scissors', 'Paper']
        }

    def computer_choice(self):
        return random.choice(list(self.win_conditions.keys()))

    def play_round(self):
        comp_choice = self.computer_choice()
        for player in self.players:
            player_choice = player.choose_weapon()
            print(f"{player.name} chooses: {player_choice}")
            print(f"Computer chooses: {comp_choice}")
            result = self.determine_winner(player_choice, comp_choice)
            player.update_statistics(result)
            if result == "win":
                print(f"{player.name} wins the round.")
            elif result == "loss":
                print(f"{player.name} loses the round.")
            else:
                print("It's a tie.")

    def determine_winner(self, player_choice, comp_choice):
        if player_choice == comp_choice:
            return "tie"
        elif comp_choice in self.win_conditions[player_choice]:
            return "win"
        else:
            return "loss"

    def play_game(self):
        self.create_players()
        for _ in range(3):
            self.play_round()

    def create_players(self):
        self.players = []
        for i in range(1, 3):
            name = input(f"What is the name of Player {i}? (5-20 characters): ")
            while len(name) < 5 or len(name) > 20 or (self.players and name == self.players[0].name):
                print("Invalid input. Please ensure the name is 5-20 characters and unique.")
                name = input(f"What is the name of Player {i}? (5-20 characters): ")
            self.players.append(Player(name))

    def show_rules(self):
        rules = """
        Rock breaks Scissors and Saw, loses against Paper.
        Scissors cut Paper, lose against Rock and Saw.
        Paper covers Rock, loses against Scissors and Saw.
        Saw cuts Scissors and Paper, loses against Rock.
        Same selection results in a tie.
        """
        print(rules)

class GameDriver:
    def __init__(self):
        self.game = Game()

    def show_statistics(self):
        for player in self.game.players:
            print(f"{player.name}: {player.statistics.display_stats()}")

    def determine_overall_winner(self):
        player1_wins = self.game.players[0].statistics.wins
        player2_wins = self.game.players[1].statistics.wins

        if player1_wins > player2_wins:
            return self.game.players[0]
        elif player2_wins > player1_wins:
            return self.game.players[1]
        else:
            return None  # No overall winner

    def main_menu(self):
        while True:
            print("\n1. Play game\n2. Show game rules\n3. Show statistics\n4. Show overall winner\n5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.game.play_game()
            elif choice == '2':
                self.game.show_rules()
            elif choice == '3':
                self.show_statistics()
            elif choice == '4':
                overall_winner = self.determine_overall_winner()
                if overall_winner:
                    print(f"\nOverall Winner: {overall_winner.name}")
                else:
                    print("\nNo overall winner yet.")
            elif choice == '5':
                print("Goodbye")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    game_driver = GameDriver()
    game_driver.main_menu()


