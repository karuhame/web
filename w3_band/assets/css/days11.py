import random
def deal_card():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card = random.choice(cards)
    return card

def Ace(list):
    if(11 in list and sum(list) >21):
        list.remove(11)
        list.append(1)
def hit_dealer(player_list,dealer_list):
    while(sum(dealer_list)<sum(player_list)or(sum(dealer_list)<17)):
        dealer_list.append(deal_card())
        Ace(dealer_list)
        print(f"Dealer cards:{dealer_list}")
    if(sum(dealer_list)>sum(player_list) and sum(dealer_list)<=21):
        print("You lose.")
    elif(sum(dealer_list)==sum(player_list)):
        print("we call it a draw. LMAO")
    else: print("You won")

def hit_player(player_list,dealer_list):
    draw = input("Do you want to draw? Type 'y' or 'n'.").lower()
    if(draw == 'y'):
        player_list.append(deal_card())
        Ace(player_list)
        print(f"This is your cards {player_list}")
        if(sum(player_list)>21):
            print("BUSTED!!! You lose.")
        else:
            hit_player(player_list,dealer_list)
    else:
        print(f"Dealer cards:{dealer_list}")
        hit_dealer(player_list,dealer_list)

player = []
dealer = []
for i in range(2):
    player.append(deal_card())
    dealer.append(deal_card())
print(f"This is your cards {player}")
hit_player(player,dealer)
