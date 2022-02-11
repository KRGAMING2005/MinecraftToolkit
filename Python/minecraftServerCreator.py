import os
import requests as req
from subprocess import check_call, STDOUT, Popen

def notWindows():
    if os.name == 'nt':
        print("Sorry! This script currently only runs under linux!")
    else:
        isRanUnderRoot()

def isRanUnderRoot():
    if os.geteuid() == 0:
        print("Installing correct java version...")
        proc = Popen('sudo apt-get install -y openjdk-17-jre', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash")
        proc.wait()
        print('Successfully installed java 17')
        menu()
    else:
        print("Hey! This script needs to be ran as root!")

def getLatestBuild(project, version):
    url = f"https://papermc.io/api/v2/projects/{project}/versions/{version}"
    resp = req.get(url)
    data = resp.json()
    return max(data["builds"])

def downloadFile(project, version, build):
    url = f"https://papermc.io/api/v2/projects/{project}/versions/{version}/builds/{build}/downloads/{project}-{version}-{build}.jar"
    print(url)
    proc = Popen(f'wget {url}', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT)
    proc.wait()
    print(f"Downloaded file {project}-{version}-{build}.jar")
def menu():
    info = input("This script will install a Minecraft server or Proxy into the current directory \n Press enter to continue")
    option = input("MC Server creation script by TheDeQ\nServer software:\n[6] Bungeecord \n[5] Velocity \n[4] Craftbukkit\n[3] Spigot\n[2] Paper \n[1] Purpur\n$ ")
    if option == '6':
        print('Downloading latest version of Bungeecord...')
        proc = Popen('wget https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT)
        proc.wait()
        print('Downloaded \'BungeeCord.jar\'')
    elif option == '5':
        print('Downloading stable version of Velocity...')
        proc = Popen('wget https://papermc.io/api/v2/projects/velocity/versions/3.1.1/builds/98/downloads/velocity-3.1.1-98.jar', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT)
        proc.wait()
        print('Downloaded \'Velocity.java\'')
    elif option == '4':
        version = input("What version of Craftbukkit should i download? ")
        print('Downloading Craftbukkit ' + version + "...")
        proc = Popen('wget https://download.getbukkit.org/craftbukkit/craftbukkit-'+version+'.jar', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT)
        proc.wait()
        print('Donwloaded \'craftbukkit-'+version+'.jar\'')
    elif option == '3':
        version = input("What version of Spigot should i download? ")
        print('Downloading Spigot ' + version + "...")
        proc = Popen('wget https://download.getbukkit.org/spigot/spigot-'+version+'.jar', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT)
        proc.wait()
        print('Donwloaded \'spigot-'+version+'.jar\'')
    elif option == '2':
        print("")


notWindows()