import random,art

def deal_cards():
    """Returns a random card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card= random.choice(cards)
    return card

def calculate_score(cards):
    """calculates the scores of the players"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_cards(u_score, c_score):
    """compares the scores of the players"""
    if u_score == c_score:
        return "it's a Draw. (for some reason i think that's good- equality? empath issues)"
    elif c_score == 0:
        return "You Lose, opponent has a Blackjack"
    elif u_score == 0:
        return "You Win with a Blackjack"
    elif u_score > 21:
        return "You Lose, you went over (sounded greedy ngl)"
    elif c_score > 21:
        return "You win, opponent went over"
    elif u_score > c_score:
        return "You win slayy!!"
    else:
        return "You Lost terribly, you can always try again tho<3"

def play():
    print(art.logo)
    user=[]
    computer=[]
    user_score= -1
    computer_score= -1
    game_over=False

    for i in range(2):
        user.append(deal_cards())
        computer.append(deal_cards())

    while not game_over:
        user_score= calculate_score(user)
        computer_score= calculate_score(computer)

        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Computers first card: [{computer[0]}]")

        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            deal_or_not=input("Type 'y' to deal another card, type 'n' to pass: ")
            if deal_or_not=="y":
                user.append(deal_cards())
            else:
                game_over=True

    while computer_score!=0 and computer_score<17:
        computer.append(deal_cards())
        computer_score= calculate_score(computer)

    print(f"Your final cards: {user}, final score: {user_score}")
    print(f"Computers final cards: {computer}, final score: {computer_score}")
    print(compare_cards(user_score, computer_score))

while input("Wanna play Blackjackk?? Type 'y' or 'n':) :") == "y":
    print("\n" * 20)
    play()