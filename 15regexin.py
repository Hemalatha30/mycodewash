#usr/bin/python3

import re


def main():
    with open("textcap.txt","r") as textcap:
        for line in textcap: # first line in text cap ; looping 
            regmatch = re.search(r"^Contact:\ssip:\+(\d+)@\[(.*)\]:?(\d+)?", line)
            if regmatch:
                print(regmatch)         # display match object
                print(regmatch.group()) # display full match
                print(regmatch.group(1)) #display the digits of caller
                print(regmatch.group(2)) # display the IPv6
                print(regmatch.group(3)) # display the port


if __name__ == "__main__":
    main()









