#!usr/bin/python3

"""demo on the NASA APOD api and devv keys"""

import requests
import pprint

MYAPI = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key="

def keyharvester():
    with open("/home/student/nasa.key","r") as keyfile:
        mykey = keyfile.read()
    return mykey.rstrip('\n')

def main():
    #harvest our key from nasa.key /home/student
    nasakey = keyharvester()
    nasakey = nasakey.rstrip('\n')

    # append our key to MYAPI
    # called API (request.get() and pull off json (.json())
    asteroids =requests.get(MYAPI + nasakey).json()


    # decode json - loop across "near earth objects" to reveal asteroids
   # pprint.pprint(asteroids["near_earth_objects"])
    for bigrock in asteroids["near_earth_objects"]:
        if bigrock["is_potentially_hazardous_asteroid"]:
            print("Name -",bigrock["name"])
            print("PROXIMITY -",bigrock["close_approach_data"])
            print("Size - ",bigrock["estimated_diameter"], end = "\n*************************\n")
        else:
            print("This asteroid is not one to concern")
                    

   # only display those that may pose a danger



if __name__ == "__main__":
    main()

