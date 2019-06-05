#!usr/bin/python3


""" SSH Learning"""

import os

import paramiko

SRVRS =[{'ip':'10.10.2.3','un':'bender'},{'ip':'10.10.2.4', 'un':'fry'}]

CMDLIST = ['touch sshworked.txt', 'touch sshworked2.txt', 'uptime']

def cmdissue(sshsession, commandtoissue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(commandtoissue)
    return ssh_stdout.read()


def main():
    # harvest RSA key (ssh private key)
    # default path on home folder
    myprivkey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")


    for server in SRVRS:


        # It is like a putty terminal just opened without abny credentials
        # init connection to remote machine
        sshsession = paramiko.SSHClient()
        # dont prompt for the to add or not like in putty we want it as automated
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshsession.connect(hostname=server['ip'], username=server['un'], pkey=myprivkey)

        # Initiate connection to remote machine


        #touch two files


        # get uptime of server
        for commandtoissue in CMDLIST:
            with open("serverresults.log","a") as svrlog:
                #cmdissue(sshsession, commandtoissue)
                print(cmdissue(sshsession, commandtoissue), file=svrlog)



        # close the connection 
        sshsession.close()

if __name__ == "__main__":
    main()

