#!/usr/bin/python3

"""LAb for List and DICT"""

def showInstructions():
    #print a main menu and the commands
	print('''RPG Game for fun learning''')

def showStatus():
    # PRINT PLAYers current status
	print('------------------------')
	print('You are in the' + currentRoom)
	#print in the current Inventory
	print('Inventory :'+ str(inventory))
	#print an item if there is one
	if "item" in rooms[currentRoom]:
	    print('You see a' + rooms[currentRoom]['item'])
	print("-------------------------------------------------------")


# an inventory which is initiall empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {'Hall' : {'south' : 'Kitchen', 'east' : 'Dining Room', 'item' : 'key'},'Kitchen' : {'north' : 'Hall', 'item' : 'monster'}, 'Dining Room': {'west' : 'Hall','south' : 'Garden', 'item' : 'potion'}, 'Garden' : {'north' : 'Dining Room'}}

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#Loop forever
    
while True:

    showStatus()
#get the player's next 'move'
#.split() breaks it up into a list array

    move = ''
    while move == '':
        move = input ('>')

    move = move.lower().split()

#if they type 'go' first
if move[0] == 'go':
    # check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
        #set the current room to new room
        currentRoom = rooms[currentRoom][move[1]]
	#there is no door (link) to new room
    else:
	    print('You can\'t go that way!')


#if they type 'get' first
if move[0] == 'get' :
    # if room contains an item, and the item is the one way want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #add the item to their inventory
        inventory += [move[1]]
	#display helpful message
        print (move[1]  + ' got!')
	#delete the items from the room
        del rooms[currentRoom]['item']
        #otherwise , if the item is not there to get
    else:
        #tell then they cannot get it
        print('Can\'t get'+ move[1] + '!')

## If a player enters a room with monster
if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you ... Game over!')
    break

if currentRoom == 'Garden' and 'Key' in inventory and 'potion' in inventory:
    print('You escaped the house with ultra rare key and magic potion .. You WIN!')
    break



