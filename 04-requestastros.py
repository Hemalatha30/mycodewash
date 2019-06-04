#!/usr/bin/python3


import requests
                   
MAJORTOM = "http://api.open-notify.org/astros.json"


def main():
    try:
        resp = requests.get(MAJORTOM)
         # pyj = requets.get(MAJORTOM).json()

        pyj = resp.json()

        astro = pyj.get("people")

        for space in astro:
            print(space["name"])
    except:
        print("API is unavailable at the moment")
        exit()

if __name__ == "__main__":
    main()


