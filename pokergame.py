import random

class seat_hand(object):
  def __init__(self, card1, card2, handrank, money, style):
    self.card1 = card1
    self.card2 = card2
    self.handrank = handrank
    self.money = money
    self.style = style
    self.hand = card1 + card2
    
    
seat1 = seat_hand('','',0,1000,8)
seat2 = seat_hand('','',0,1000,11)
seat3 = seat_hand('','',0,1000,7)
seat4 = seat_hand('','',0,1000,7)
seat5 = seat_hand('','',0,1000,5)
seat6 = seat_hand('','',0,1000,8)
seat7 = seat_hand('','',0,1000,8)
playerHand = seat_hand('','',0,1000,20)

players = [seat1, seat2, seat3, seat4, seat5, seat6,seat7]

deck = ['As','Ac','Ah','Ad','2s','2c','2h','2d','3s','3c','3h','3d',
        '4s','4c','4h','4d','5s','5c','5h','5d','6s','6c','6h','6d',
        '7s','7c','7h','7d','8s','8c','8h','8d','9s','9c','9h','9d',
        'Ts','Tc','Th','Td','Js','Jc','Jh','Jd',
        'Qs','Qc','Qh','Qd','Ks','Kc','Kh','Kd']


def card_delt():
    turn = []
    card = random.randint(0,len(deck) - 1)
    #print (card)
    turn.append(deck[card])
    deck.pop(card)
    return turn


#Computer players hand
for each in players:
    each.card1 = card_delt()
    each.card2 = card_delt()
    each.hand = each.card1 + each.card2

#Players hand
playerHand.card1 = card_delt()
playerHand.card2 = card_delt()
playerHand.hand = playerHand.card1 + playerHand.card2


#ranking the computers hand
def hand_rank(seat,player_hand):
    card1 = player_hand[0][0]
    card2 = player_hand[1][0]
    suit1 = player_hand[0][1]
    suit2 = player_hand[1][1]  

    def check_pairs(seat,player_hand):
        if card1 == card2:
            if card1 == "4" or card1 == "3" or card1 == "2":
                #print ("Low Pocket pair")
                return 7
            elif card1 == "5" or card1 == "6":
                #print ("Low-mid Pocket pair")
                return 6        
            elif card1 == "8" or card1 == "7":
                #print ("mid Pocket pair")
                return 5        
            elif card1 == "9" or card1 == "T":
                #print ("mid-hig Pocket pair")
                return 2
            else:
                #print ("high Pocket pair")
                return 1
        else:
            return 0
    def has_ace(seat,player_hand):
        if card1 == "A" or card2 == "A":
            if suit1 == suit2:
                if card1 == "K" or card2 == "K":
                    #print ("has suited AK")
                    return 1
                elif card1 == "Q" or card2 == "Q" or card1 == "J" or card2 == "J":
                    #print ("has suited AQ or AJ")
                    return 2
                elif card1 == "T" or card2 == "T":
                    #print ("has suited AT")
                    return 3
                else:
                    #print ("has low suited Ace")
                    return 5
            else:
                if card1 == "K" or card2 == "K":
                    #print ("has unsuited AK")
                    return 2
                elif card1 == "Q" or card2 == "Q":
                    #print ("has unsuited AQ")
                    return 3
                elif card1 == "J" or card2 == "J":
                    #print ("has unsuited AJ")
                    return 4
                elif card1 == "T" or card2 == "T" or card1 == "9" or card2 == "9":
                    #print ("has mid-high unsuited Ace")
                    return 7
                elif card1 == "7" or card2 == "7" or card1 == "8" or card2 == "8":
                    #print ("has mid-low unsuited Ace")
                    return 9
                else:
                    #print ("has low unsuited Ace")
                    return 10
        else:
            return 0

    def has_king(seat,player_hand):
        if card1 == "K" or card2 == "K":
            if suit1 == suit2:
                if card1 == "Q" or card2 == "Q":
                    #print ("has suited KQ")
                    return 2
                elif card1 == "T" or card2 == "T" or card1 == "J" or card2 == "J":
                    #print ("has suited KJ or KT")
                    return 3
                elif card1 == "9" or card2 == "9":
                    #print ("has suited K9")
                    return 6
                else:
                    #print ("has low suited King")
                    return 7
            else:
                if card1 == "Q" or card2 == "Q":
                    #print ("has unsuited KQ")
                    return 4
                elif card1 == "J" or card2 == "J":
                    #print ("has unsuited KJ")
                    return 5
                elif card1 == "T" or card2 == "T" or card1 == "9" or card2 == "9":
                    #print ("has mid-high unsuited Kings")
                    return 7
                elif card1 == "7" or card2 == "7" or card1 == "8" or card2 == "8":
                    #print ("has mid-low unsuited Kings")
                    return 9
                else:
                    #print ("has low unsuited king")
                    return 11
        else: 
            return 0

    def has_queen(seat,player_hand):
        if card1 == "Q" or card2 == "Q":
            if suit1 == suit2:
                if card1 == "J" or card2 == "J":
                    #print ("has suited QJ")
                    return 3
                elif card1 == "T" or card2 == "T":
                    #print ("has suited KJ or KT")
                    return 4
                elif card1 == "9" or card2 == "9":
                    #print ("has suited Q9")
                    return 6
                elif card1 == "8" or card2 == "8":
                    #print ("has suited Q8")
                    return 7
                else:
                    #print ("has low suited Queen")
                    return 10
            else:
                if card1 == "J" or card2 == "J":
                    #print ("has unsuited QJ")
                    return 5
                elif card1 == "T" or card2 == "T" or card1 == "9" or card2 == "9":
                    #print ("has mid-high unsuited Queen")
                    return 7
                elif card1 == "7" or card2 == "7" or card1 == "8" or card2 == "8":
                    #print ("has mid-low unsuited Queen")
                    return 9
                else:
                    #print ("has low unsuited Queen")
                    return 11
        else: 
            return 0
    
    def has_jack(seat,player_hand):
        if card1 == "J" or card2 == "J":
            if suit1 == suit2:
                if card1 == "T" or card2 == "T":
                    #print ("has suited JT")
                    return 3
                elif card1 == "9" or card2 == "9":
                    #print ("has suited J9")
                    return 4
                elif card1 == "8" or card2 == "8":
                    #print ("has suited J8")
                    return 6
                elif card1 == "7" or card2 == "7":
                    #print ("has suited J7")
                    return 8
                else:
                    #print ("has low suited Jack")
                    return 11
            else:
                if card1 == "T" or card2 == "T":
                    #print ("has unsuited JT or JT")
                    return 5
                elif card1 == "9" or card2 == "9":
                    #print ("has unsuited J9")
                    return 7
                elif card1 == "8" or card2 == "8":
                    #print ("has unsuited J8")
                    return 8
                else:
                    #print ("has low unsuited Jack")
                    return 12
        else: 
            return 0
    
    def has_ten(seat,player_hand):
        if card1 == "T" or card2 == "T":
            if suit1 == suit2:
                if card1 == "9" or card2 == "9":
                    #print ("has suited T-9")
                    return 4
                elif card1 == "8" or card2 == "8":
                    #print ("has suited T-8")
                    return 5
                elif card1 == "7" or card2 == "7":
                    #print ("has suited T-7")
                    return 7
                else:
                    #print ("has low suited Jack")
                    return 11
            else:
                if card1 == "9" or card2 == "9":
                    #print ("has unsuited T-9")
                    return 7
                elif card1 == "8" or card2 == "8":
                    #print ("has unsuited T-8")
                    return 8
                else:
                    #print ("has low unsuited T")
                    return 12
        else: 
            return 0

    def has_nine(seat,player_hand):
        if card1 == "9" or card2 == "9":
            if suit1 == suit2:
                if card1 == "6" or card2 == "6":
                    #print ("has suited 9-6")
                    return 8
                elif card1 == "8" or card2 == "8":
                    #print ("has suited 9-8")
                    return 4
                elif card1 == "7" or card2 == "7":
                    #print ("has suited 9-7")
                    return 5
                else:
                    #print ("has low suited nine")
                    return 11
            else:
                if card1 == "8" or card2 == "8":
                    #print ("has unsuited 9-8")
                    return 7
                else:
                    #print ("has low unsuited 9")
                    return 12
        else: 
            return 0            
    
    def has_eight(seat,player_hand):
        if card1 == "8" or card2 == "8":
            if suit1 == suit2:
                if card1 == "6" or card2 == "6":
                    #print ("has suited 8-6")
                    return 6
                elif card1 == "5" or card2 == "5":
                    #print ("has suited 8-5")
                    return 8
                elif card1 == "7" or card2 == "7":
                    #print ("has suited 8-7")
                    return 5
                else:
                    #print ("has low suited eight")
                    return 11
            else:
                if card1 == "7" or card2 == "7":
                    #print ("has unsuited 9-8")
                    return 8
                else:
                    #print ("has low unsuited 8")
                    return 12
        else: 
            return 0     

    def has_seven(seat,player_hand):
        if card1 == "7" or card2 == "7":
            if suit1 == suit2:
                if card1 == "6" or card2 == "6":
                    #print ("has suited 7-6")
                    return 5
                elif card1 == "5" or card2 == "5":
                    #print ("has suited 7-5")
                    return 6
                elif card1 == "4" or card2 == "4":
                    #print ("has suited 7-4")
                    return 8
                else:
                    #print ("has low suited seven")
                    return 11
            else:
                if card1 == "6" or card2 == "6":
                    #print ("has unsuited 7-6")
                    return 8
                else:
                    #print ("has low unsuited 7")
                    return 12
        else: 
            return 0    

    def has_six(seat,player_hand):
        if card1 == "6" or card2 == "6":
            if suit1 == suit2:
                if card1 == "5" or card2 == "5":
                    #print ("has suited 6-5")
                    return 7
                elif card1 == "4" or card2 == "4":
                    #print ("has suited 6-4")
                    return 7
                else:
                    #print ("has low suited six")
                    return 11
            else:
                if card1 == "5" or card2 == "5":
                    #print ("has unsuited 6-5")
                    return 8
                else:
                    #print ("has low unsuited 6")
                    return 12
        else: 
            return 0 

    def has_five(seat,player_hand):
        if card1 == "5" or card2 == "5":
            if suit1 == suit2:
                if card1 == "4" or card2 == "4":
                    #print ("has suited 5-4")
                    return 6
                elif card1 == "3" or card2 == "3":
                    #print ("has suited 5-4")
                    return 7
                else:
                    #print ("has low suited five")
                    return 11
            else:
                if card1 == "4" or card2 == "4":
                    #print ("has unsuited 5-4")
                    return 8
                else:
                    #print ("has low unsuited 5")
                    return 12
        else: 
            return 0     

    def has_four(seat,player_hand):
        if card1 == "4" or card2 == "4":
            if suit1 == suit2:
                if card1 == "3" or card2 == "3":
                    #print ("has suited 4-3")
                    return 7
                else:
                    #print ("has suited 4-2")
                    return 8
            else:
                #print ("has low unsuited 4")
                return 12
        else: 
            return 0              
    
    def has_three(seat,player_hand):
        if card1 == "3" or card2 == "3":
            if suit1 == suit2:
                #print ("has suited 3-2")
                return 8
            else:
                #print ("has low unsuited 3")
                return 12
        else: 
            return 0              
    
    #the system that runs thru the if statments
    seat.handrank = check_pairs(seat,player_hand)
    if seat.handrank == 0:
        seat.handrank = has_ace(seat,player_hand)
        if seat.handrank == 0:
            seat.handrank = has_king(seat,player_hand)
            if seat.handrank == 0:
                seat.handrank = has_queen(seat,player_hand)
                if seat.handrank == 0:
                    seat.handrank = has_jack(seat,player_hand)
                    if seat.handrank == 0:
                        seat.handrank = has_ten(seat,player_hand)
                        if seat.handrank == 0:
                            seat.handrank = has_nine(seat,player_hand)
                            if seat.handrank == 0:
                                seat.handrank = has_eight(seat,player_hand)
                                if seat.handrank == 0:
                                    seat.handrank = has_seven(seat,player_hand)
                                    if seat.handrank == 0:
                                        seat.handrank = has_six(seat,player_hand)
                                        if seat.handrank == 0:
                                            seat.handrank = has_five(seat,player_hand)
                                            if seat.handrank == 0:
                                                seat.handrank = has_four(seat,player_hand)
                                                if seat.handrank == 0:
                                                    seat.handrank = has_three(seat,player_hand)
                                                    if seat.handrank == 0:
                                                        print ("somthings wrong")


#eventualy put a for loop in to run thru all the players at the table

for each in players:
    hand_rank(each,each.hand)



for each in players:
    if each.style < each.handrank:
        each.hand = "Fold"
        print ("Fold")
    else:
        print ("Call")

print (playerHand.hand)


# prints the 3 cards that are on the flop
userAns = input("Fold or Call: ").upper()
print (" ")
print (card_delt()) #prints flop1
print (card_delt()) #prints flop2
print (card_delt()) #prints flop3
print (" ")
#userAns = input("Are you ready to see the turn: ").upper()
print (card_delt()) #prints turn
print (" ")

#userAns = input("Are you ready to see the river: ").upper()
print (card_delt()) #prints river
print (" ")
print (" ")

for each in players:
    print(each.hand)
#print (deck)

print ("Your hand was" , playerHand.hand)