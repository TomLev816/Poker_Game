import random


def deal():
    cards = ['As','Ac','Ah','Ad','2s','2c','2h','2d',
            '3s','3c','3h','3d','4s','4c','4h','4d',
            '5s','5c','5h','5d','6s','6c','6h','6d',
            '7s','7c','7h','7d','8s','8c','8h','8d',
            '9s','9c','9h','9d','10s','10c','10h','10d',
            'Js','Jc','Jh','Jd','Qs','Qc','Qh','Qd',
            'Ks','Kc','Kh','Kd']


    myHand = []
    seat1 = []
    seat2 = []
    seat3 = []
    seat4 = []
    seat5 = []
    seat6 = []
    seat7 = []
    seat8 = []


    def hand():
        delt = []
        for i in range(2):
            card = random.randint(0,len(cards)-1)
            print (card)
            delt.append(cards[card])
            cards.pop(card)
        return delt



    seat1 = hand()
    seat2 = hand()
    seat3 = hand()
    seat4 = hand()
    seat5 = hand()
    seat6 = hand()
    seat7 = hand()
    seat8 = hand()

    print (seat1)
    print (seat2)
    print (seat3)
    print (seat4)
    print (seat5)
    print (seat6)
    print (seat7)
    print (seat8)

    def theFlop():
        flop = [ ]
        for i in range(3):
            card = random.randint(1,len(cards))
            print (card)
            flop.append(cards[card])
            cards.pop(card)
        return flop


    print (theFlop())


    def turn_river():
        turn = []
        card = random.randint(1,len(cards))
        print (card)
        turn.append(cards[card])
        cards.pop(card)
        return turn

    print (turn_river()) #prints turn
    print (turn_river()) #prints river

deal()