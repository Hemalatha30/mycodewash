
#!/usr/bin/python3
'''Author:Hema | Email: Hemasnet@yahoo.com || json learning with Python'''

# with python, the json batteries are in box, but you need to plug them in 

import json

def main():
    # create a list of dictionaries
    videogames = [{"game1":"red", "game2":"whisker","game3":"hema","game4":"Sakthivel"}, {"game1":"paperboy", "game2":"donkey Knong"}]

# show the values of videogames

    print(videogames)

    # create a file in the local system

    with open('vidogames.json',"w") as vidfile: # "w" is write ; "r" - read, "a" = "append
        json.dump(videogames, vidfile)

# function will nee dto be called for it to work or return something 

if __name__ == "__main__":
    main()
