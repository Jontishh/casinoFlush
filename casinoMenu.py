import json

# clear the screen
def clear():
    from os import system, name
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Read users from json text file
def loadUsers():
    global users
    try:
        with open('users.txt','r') as f:
            users = json.loads(f.read())
    except:
        with open('users.txt','w') as f:
            pass

# user example structure
#{
#    "ken": {
#        "password": "doll",
#        "credit": 2000
#    }
#}
# Write users to json text file
def saveUsers():
    with open('users.txt','w') as f:
            f.write(json.dumps(users, indent = 4))

def loginInput ():
    username = input ('Username: ')
    password = input ('Password: ')
    return username, password


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

def loginMenu ():
    clear()
    print ('\n[Login]\n')
    username, password = loginInput ()
    while (username in users) == False or (password == users[username]['password']) == False:
        clear()
        print ('\nInvalid username or password')
        if menu(failedLoginOptions) == '1':
            print ('\n[Login]\n')
            username, password = loginInput ()
        else:
            return -1
    return username

def registerMenu():
    clear()
    print ('\n[Register]\n')
    username, password = loginInput()
    credits = 1500
    while username in users:
        clear()
        print(f'Username [{username}] already in use')
        if menu(failedLoginOptions) == '1':
            print ('\n[Register]\n')
            username, password = loginInput()
        else:
            return -1
    users[username] = {
        'password': password,
        'credit': credits
    }
    saveUsers()
    print(f'\nUser created, you have {credits}$')
    return username

def gameMenu(opt):
    clear()
    if opt == '1':
        clear()
        print (f"\n{user}'s information:\n")
        print (f'Username: {user}, Password: *****, Credits: {users[user]["credit"]}$')
        opt = menu(loginOptions)
    if opt == '2':
        clear()
        print ('\nStarting blackjack...\n')
        from blackjack import blackjackGame
        users[user]['credit'] += blackjackGame(users[user]["credit"])
        saveUsers()
    elif opt == '3':
        clear()
        print ('\nStarting Slotmachines...\n')
        from slotmachine import slotmachineGame
        users[user]['credit'] += slotmachineGame(users[user]["credit"])
        saveUsers()
    elif opt == 'q':
        print ('\nYou chose to exit. See you soon!')
        exit()

users = {}
startupMenu = {'1':'Login', '2':'Register', 'q':'Quit'}
loginOptions = {'1':'User Information', '2':'Blackjack', '3': 'Slotmachines', 'q':'Exit'}
failedLoginOptions = {'1':'Try again', '2':'Return'}
user = None
loadUsers()

while True:
    option = menu(startupMenu)
    if option == '1':
        user = loginMenu()
    elif option == '2':
        user = registerMenu()
    elif option == 'q':
        break

    while user != -1:
        clear()
        print ('\n[Main menu]')
        option = menu(loginOptions)
        gameMenu(option)

