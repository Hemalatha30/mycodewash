
#!/usr/bin/python3

''' Author Hemasnet@yhaoo.com +Learning GITjson.py'''

# Pull in json so that we can parse json

import json

def main():

    # open thejonsnow.json file in read mode
    with open("jonsnow.json", "r") as gotdata:
        jonsnow = gotdata.read() # create a string of all the json 
        GOTpy = json.loads(jonsnow) # covert string to pythonic lISTS AND DICTS 
    print(GOTpy)
    print(GOTpy["url"])
    print(GOTpy["aliases"])
    print(GOTpy["titles"])


#create a loop to move across aliases
    with open("aliases.txt","w") as jsaliases:
       for gotalias in GOTpy["aliases"]:
          print(gotalias, file=jsaliases)
    print(GOTpy["aliases"])
       # print(jonsnow)
       # print(jonsnow["url"])

          # parse file for ..


    # display character name

    # display charater aliases



   # display api for 



if __name__ == "__main__":
    main()
