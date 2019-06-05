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
-- INSERT --                                                    i#!/usr/bin/python3

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
                                                                                                -- INSERT --                                                    
