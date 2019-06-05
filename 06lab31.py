#!usr/bin/python

""" List and Dict Modelling"""

def showinstructions():
    #print  a main menu and the commands
    print('''RPG GAME by Zach''')

def showstatus():
    #print Player's current status
    print('You are in the' + currentRoom)
    # print current inventory
    print('Inventory' + str(inventory))
    # print an item if thers is one
    if "item" in rooms[currentRoom]:
        print('You see a' + rooms[currentRoom]['item'])
    print("------------------------------------------------------------------")

#an inventory which is empty initially
inventory = []
# create a dictionary for rooms
rooms = { 'Hall':{'south':'Kitchen'},'Kitchen':{'north':'Hall'}}

#start the player in the Hall
currentRoom = 'Hall'

showinstructions()

#loop forever as it is game and not real world project
while True:
    showstatus()

    #get the player's next 'move'
    #.split() breaks it up into a list array
    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split()

    # if they tyoe 'go' first
    if move[0] == 'go':
        #check they are allowed to go wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door(link) to new room
    else:
        print('You cannot go that way!')

    #if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item and item is the one they want o get
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to the inventory
            inventory += [move[1]]
            #display the helpful message
            print(move[1] + 'got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise , if the item is not there to get
    else:
        #tell then they cannot get it 
        print("Can't get" + move[1] + "!")
