import random

class AbstractGame:

    def start(self):
        while True:
            start = input("Would you like to play? ")
            if start.lower() == "yes" or start.lower() == "y":
                break
        self.play()    
            

    def end(self):
        print("The game has ended.")
        self.reset()
    
    def play(self):
        raise NotImplementedError("play() has not been implemented yet")
    
    def reset(self):
        raise NotImplementedError("reset() has not been implemented yet")
    
class AnotherGame(AbstractGame):

    pass

class RandomGuesser(AbstractGame):

    def __init__(self, rounds: int):
        self.rounds = rounds
        self.round = 0

    def reset(self):
        self.round = 0

    def play(self):
        while self.round < self.rounds:
            self.round += 1
            print(f"Welcome to round {self.round}. Let's Begin!")
            random_num = random.randint(1, 10)
            while True:
                guess = input("Enter a number between 1 - 10: ")
                if int(guess) == random_num:
                    print("You got it!")
                    break
        self.end()

#games = [AnotherGame(), RandomGuesser(1)]
games = [RandomGuesser(1), AnotherGame()]
for game in games:
    game.start()