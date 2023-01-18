import random

def play():
    user = input("what's you choice?r 'r' for rock 'p' for paper and 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'it\' a tie'

    if is_win(user, computer):
         return 'you won!'
    return 'you lost!'
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
    (player == 'p' and opponent == 'r'):
        return True

print(play())