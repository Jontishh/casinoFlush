import random

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

def createRow (sym, row):
    for i in range (3):
        row.append(random.choice(sym))
    return row

def showRow (row):
    i = " | "
    for j in row:
        i += str(j) + " | "
    return i

def slotmachineGame (credit):
    earning = 0
    keepPlayingOptions = {"1": "Try again", "2": "Go back to main menu"}
    symbols = ["✨", "❌", "⭐"]
    keepPlaying = True
    while keepPlaying == True:
        print (f"You have {credit + earning} credits.")
        try:
            bet = (int(input('How much do you want to bet?: ')))
        except:
            print ("\nInvalid input\n")
            continue
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
            earning += 2*bet
            if rowThree[0] == rowTwo[1] and rowTwo[1] == rowOne[2]:
                earning += 2*bet
                if rowOne[0] == rowTwo[1] and rowTwo[1] == rowThree[2]:
                    earning += 2*bet
                    #Three wins both diagonals and row
                    print (f"You won {6*(bet)}$!")
                else:
                    #Two wins first diagonal and row
                    print (f"You won {4*(bet)}$!")
            elif rowOne[0] == rowTwo[1] and rowTwo[1] == rowThree[2]:
                earning += 2*bet
                #Two wins "other" diagonal and row
                print (f"You won {4*(bet)}$!")
            else:
                #One win
                print (f"You won {2*(bet)}$!")
        elif rowThree[0] == rowTwo[1] and rowTwo[1] == rowOne[2]:
            earning += 2*bet
            if rowOne[0] == rowTwo[1] and rowTwo[1] == rowThree[2]:
                earning += 2*bet
                #Two wins both diagonals
                print (f"You won {4*(bet)}$!")
            else:
                #One win first diagonal
                print (f"You won {2*(bet)}$!")
        elif rowOne[0] == rowTwo[1] and rowTwo[1] == rowThree[2]:
            earning += 2*bet
            if rowThree[0] == rowTwo[1] and rowTwo[1] == rowOne[2]:
                earning += 2*bet
                #Two wins both diagonals
                print (f"You won {4*(bet)}$!")
            else:
                #One win second diagonal
                print (f"You won {2*(bet)}$!")
        else:
            print ("You lost this time.")
            
        option = menu(keepPlayingOptions)
        
        if option == "2":
            keepPlaying = False
    return earning
                