import os
import sys
import json
import requests as req
from subprocess import STDOUT, Popen

def getLatesBuild(project, version):
    url = f"https://papermc.io/api/v2/projects/{project}/versions/{version}"
    resp = req.get(url)
    data = resp.json()
    return max(data["builds"])

def DownloadFile(url):
    local_filename = url.split('/')[-1]
    r = req.get(url)
    f = open(local_filename, 'wb')

    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return 

def DownloadFromPaperAPI(project, version, build):
    url = f"https://papermc.io/api/v2/projects/{project}/versions/{version}/builds/{build}/downloads/{project}-{version}-{build}.jar"
    DownloadFile(url)
# Te
def DownloadManager(option):
    if option == "6":
        print("Downloading BungeeCord...")
        url = "https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar"
        DownloadFile(url)
        print("Downloaded BungeeCord.jar")
    elif option == "5":
        mc = input("What Velocity version do you want to donwload? ")
        print("Downloading Velocity...")
        DownloadFromPaperAPI('velocity', mc, getLatesBuild('velocity', mc))
        print("Downloaded velocity-3.1.1.jar")
    elif option == "4":
        mc = input("What Craftbukkit version do you want to donwload? ")
        print("Downloading Craftbukkit...")
        url = f"https://download.getbukkit.org/craftbukkit/craftbukkit-{mc}.jar"
        DownloadFile(url)
        print("Downloaded Craftbukkit.jar")
    elif option == "3":
        mc = input("What Spigot version do you want to donwload? ")
        print("Downloading Spigot...")
        url = f"https://download.getbukkit.org/spigot/spigot-{mc}.jar"
        DownloadFile(url)
        print("Downloaded Spigot.jar")
    elif option == "2":
        mc = input("What Paper version do you want to donwload? ")
        print("Downloading Paper...")
        DownloadFromPaperAPI('paper', mc, getLatesBuild('paper', mc))
        print("Downloaded Paper.jar")
        BungeeCord = input("Is this going to be a bungeecord sub server [Y] [N] ? ")
        if BungeeCord == "Y" or BungeeCord == "y":
            proc = Popen(f'java -Xmx1G -jar paper-{mc}-'+ str(getLatesBuild('paper', mc)) + ".jar", shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash")
            proc.wait()
            eula = open("eula.txt", "a+")
            eula.write("eula=true")
            eula.close()
            with open('server.properties', 'r') as properties:
                propdata = properties.read()
            propdata = propdata.replace('online-mode=true', 'online-mode=false')
            with open('server.properties', 'w') as properties:
                properties.write(propdata)
        else:
            exit()
    elif option == "1":
        mc = input("What Purpur version do you want to donwload? ")
        print("Downloading Purpur...")
        url = f"https://api.purpurmc.org/v2/purpur/{mc}/latest/download"
        DownloadFile(url)
        os.rename("download", f"purpur-{mc}.jar")
        print("Downloaded Purpur.jar")
    elif option == "q":
        exit()
    else:
        menu()


#downloadFile('velocity', '3.1.1', getLatesBuild('velocity', '3.1.1'))

def menu():
    option = input("\n\nWhat software do you want to install?\n[6] BungeeCord\n[5] Velocity\n[4] Craftbukkit\n[3] Spigot\n[2] Paper\n[1] Purpur\n$ ")
    DownloadManager(option)


def main():
    print("Minecraft Server Toolkit V.1")
    print("This script will convert the current directory into a minecraft server or proxy")
    keep = input("Press any key to contine")
    menu()

main()
