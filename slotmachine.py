import random
credit = 100
keepPlayingOptions = {"1": "Try again", "2": "Go back to main menu"}

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

def createRow (symbols, row):
    for i in range (3):
        row.append(random.choice(symbols))
    return row

def showRow (row):
    i = " | "
    for j in row:
        i += str(j) + " | "
    return i

def slotmachineGame (credit):
    earning = 0
    symbols = ["✨", "❌", "⭐"]
    keepPlaying = True
    while keepPlaying == True:
        print (f"You have {credit + earning} credits.")
        bet = (int(input('How much do you want to bet?: ')))
        while bet > credit + earning or bet < 0:
            print (f'Invalid bet amount [{bet}], your wallet: {credit + earning}')
            bet = (int(input('How much do you want to bet?: ')))
                
        credit -= bet
        rowOne = [] 
        rowTwo = []
        rowThree = []
        createRow (symbols, rowOne)
        createRow (symbols, rowTwo)
        createRow (symbols, rowThree)
        
        print ()
        print (showRow (rowOne))
        print (" -----------------")
        print (showRow (rowTwo))
        print (" -----------------")
        print (showRow (rowThree))
        print ()
        
        if rowTwo[0] == rowTwo[1] and rowTwo[1] == rowTwo[2]:
            earning = 2*bet
            print (f"You won {bet*2} credits!")
        elif rowThree[0] == rowTwo[1] and rowTwo[1] == rowOne[2]:
            earning = 2*bet
            print (f"You won {bet*2} credits!")
        elif rowOne[0] == rowTwo[1] and rowTwo[1] == rowThree[2]:
            earning = 2*bet
            print (f"You won {earning} credits!")
        else:
            print ("You lost this time.")
            
        option = menu(keepPlayingOptions)
        
        if option == "2":
            keepPlaying = False
    return earning
                