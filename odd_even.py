import random
import statistics

class Player():

    def __init__(self):
        self.perls = 10

        
    
wins = []

for _ in range(0,50):
    count = 0
    for _ in range(0,100):
        player1 = Player()
        player2 = Player()
        while True:
            player1_bet = player1.perls
            player2_bet = random.randint(1,player2.perls)
            player1_guess = random.randint(1,2)
            # 1 = gískar even 2 = gískar odd
            if player1_guess == 1 and player2_bet%2 == 0 or player1_guess == 2 and player2_bet%2 != 0:
                player1.perls += player1_bet
                player2.perls -= player1_bet
            else:
                player1.perls -= player2_bet
                player2.perls += player2_bet
            if player1.perls <= 0 or player2.perls <= 0:
                break    

            player1_bet = player1.perls
            player2_bet = random.randint(1,player2.perls)
            player2_guess = random.randint(1,2)
            if player2_guess == 1 and player1_bet%2 == 0 or player2_guess == 2 and player1_bet%2 != 0:
                player2.perls += player2_bet
                player1.perls -= player2_bet
            else:
                player2.perls -= player1_bet
                player1.perls += player1_bet
            if player1.perls <= 0 or player2.perls <= 0:
                break
        if player1.perls >= 20:
            count += 1
        
        print(player1.perls)
        print(player2.perls) 
    wins.append(count)
    print(count)


print(wins)
stdev = statistics.stdev(wins)
mean = statistics.mean(wins)

print(stdev)
print(mean)