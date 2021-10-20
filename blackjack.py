import random, itertools

#deck of cards
deck = list(itertools.product(list(range(2,11)) + ['J','Q','K','A'] ,['♠','♥','♦','♣']))

random.shuffle(deck)

# clear the screen
def clear():
    from os import system, name
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#deal a card
def dealCard (hand):
    if deck[0][0] == 'A':
        hand.append(deck.pop(0))
    else:
        hand.insert(0, deck.pop(0))


#calculate the total of a certain hand
def total (hand):
    total = 0
    for card in hand:
        if card[0] in range(1, 11):
            total += card[0]
        elif card[0] in ['J', 'Q', 'K']:
            total += 10
        else:
            if total >= 11:
                total += 1
            else:
                total += 11
    return total

def total2 (hand):
    total = 0
    
    for card in hand:
        if card[0] in range(1, 11):
            total += card[0]
        elif card[0] in ['J', 'Q', 'K']:
            total += 10
        else:
            r = ''
            while r is not None:
                inp = input('Is A 1 or 11?\n')
                if inp == '1':
                    total += 1
                    r = None
                elif inp == '11':
                    total += 11
                    r = None
                else:
                    print('Invalid choice')
                
    return total

def view_card(card):
    value = card[0]
    suit = card[1]

    t = '''┌───────┐
| {0:<2}    |
|       |
|   {1}   |
|       |
|     {0:<2}|
└───────┘'''

    return(t.format(value, suit), f"{value} of {suit} ")

# $$

# Print hand with suits
def view_hand(hand):
    string = ""
    i = 0
    for card in hand:
        string += (view_card(card)[1])
        if len(hand) != i+1:
            string += "and "
        i += 1

    h = [[None]*len(hand) for i in range(7)]
    for i in range(len(hand)):
        s = view_card(hand[i])[0].split('\n')
        # print(s)
        for j in range(len(s)):
            # print(s[j], i, j)
            h[j][i] = s[j]

    # print(h)
    o = ''
    for r in h:
        o += '    '.join(r) + '\n'
    print(o)
    return(string)

# print card with suit and values
def view_card2(card):
    value = card[0]
    suit = card[1]
    print('┌───────┐')
    print(f'| {value:<2}    |')
    print('|       |')
    print(f'|   {suit}   |')
    print('|       |')
    print(f'|     {value:<2}|')
    print('└───────┘')
    return(f"{value} of {suit} ")

# Print hand with suits   
# def view_hand2(hand):
#     string = ""
#     i = 0
#     for card in hand:
#         string += (view_card(card))
#         if len(hand) != i+1:
#             string += "and "
#         i += 1
#     return(string)

def menu (opt):
    for i in opt:
        print (f'\n{i}) {opt[i]}')
    i = input ('\nOption: ')
    if (i in opt) == True:
        return i
    while (i in opt) == False:
        print ('\nInvalid option. Please enter a valid option')
        i = input ('\nOption: ')
        if (i in opt) == True:
            return i

#game loop
def blackjackGame(credit):
    earning = 0
    keepPlayingOptions = {'1':'Play again', '2':'Go back to menu'}
    playOptions = {'1':'Stay', '2':'Hit', '3':'Double Down', '4':'Split'}
    keepPlaying = True
    while keepPlaying == True:
        playerHand = []
        dealerHand = []
        
        #Add a bet
        print (f"You have {credit + earning} credits.")
        bet = int(input ('How much do you want to bet?: '))
        while bet > credit + earning or bet < 0:
                print (f'Invalid bet amount [{bet}], your wallet: {credit + earning}')
                bet = (int(input('How much do you want to bet?: ')))

        for _ in range(2):
            dealCard (dealerHand)
            dealCard (playerHand)
            
        while True:
            clear()
            print (f'Dealer has {view_card2(dealerHand[0])}and X')
            print (f'You have {view_hand(playerHand)}for a total of {total(playerHand)}')
            playOption = menu(playOptions)
            if playOption == '1':
                break
            elif playOption == '2':
                dealCard(playerHand)
            elif playOption == '3':
                dealCard(playerHand)
                bet *= 2
                break
            elif playOption == '4':
                if playerHand(0) == playerHand(1) and len(playerHand) == 2:
                    playerHand2 = [playerHand.pop(0)]
                
            if total(playerHand) >= 21:
                break
        
        while True:
            if total(dealerHand) < 17 and total(playerHand) <= 21:
                dealCard(dealerHand)
            else:
                break
        clear()
        print (f'\nYou have {view_hand(playerHand)}for a total of {total(playerHand)}')
        print (f'and the dealer has {view_hand(dealerHand)}for a total of {total(dealerHand)}')

        if total(playerHand) == 21 and len(playerHand) == 2:
            print ('Blackjack! You win!')
            earning += bet
        elif total(dealerHand) == 21 and len(dealerHand) == 2:
            print ('Blackjack! Dealer wins!')
            earning += -bet
        elif total(playerHand) == 21:
            print('You got 21! You win!')
            earning += bet
        elif total(dealerHand) == 21:
            print('Dealer got 21! Dealer wins!')
            earning += -bet
        elif total(playerHand) > 21:
            print ('You bust! Dealer wins!')
            earning += -bet
        elif total(dealerHand) > 21:
            print ('Dealer busts! You win!')
            earning += bet
        elif total(playerHand) == total(dealerHand):
            print ('Draw!')
        elif 21 - total(dealerHand) < 21 - total(playerHand):
            print ('Dealer wins!')
            earning += -bet
        elif 21 - total(playerHand) < 21 - total (dealerHand):
            print ('You win!')
            earning += bet
        
        option = menu(keepPlayingOptions)
        
        if option == '2':
            keepPlaying = False
    return earning