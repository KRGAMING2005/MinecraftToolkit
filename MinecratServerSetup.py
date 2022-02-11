import os
import json
import requests as req
from subprocess import STDOUT, Popen
import fileinput

def BungeeCordSetup():
    fileURL = "https://raw.githubusercontent.com/KRGAMING2005/MinecraftToolkit/main/serverFiles/"
    fileDownloader(fileURL + "server.properties")
    fileDownloader(fileURL + "spigot.yml")

def fileDownloader(url):
    local_filename = url.split('/')[-1]
    r = req.get(url)
    f = open(local_filename, 'wb')

    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk:
            f.write(chunk)
    f.close()
    return

def getLatesBuild(project, version):
    url = f"https://papermc.io/api/v2/projects/{project}/versions/{version}"
    resp = req.get(url)
    data = resp.json()
    return max(data["builds"])


def getPaperDownloadURL(project, version, build):
    url = f"https://papermc.io/api/v2/projects/{project}/versions/{version}/builds/{build}/downloads/{project}-{version}-{build}.jar"
    return url


def downloadManager(server):
    if server == "Velocity":
        version = input("What version of Velocity do you want to download? ")
        print(f"Downloading velocity-{version}-{getLatesBuild('velocity', version)}.jar")
        fileDownloader(getPaperDownloadURL("velocity", version, getLatesBuild("velocity", version)))
    elif server == "Paper":
        version = input("What version of Paper do you want to download? ")
        print(f"Downloading paper-{version}-{getLatesBuild('paper', version)}.jar")
        fileDownloader(getPaperDownloadURL("paper", version, getLatesBuild("paper", version)))
        bungee = input("Do you want this server to be setup as a bungeecord subserver? (y,n)")
        if bungee == "y":
            BungeeCordSetup()
    elif server == "Craftbukkit":
        version = input("What version of Craftbukkit do you want to download")
        print(f"Downloading craftbukkit-{version}.jar")
        fileDownloader(f"https://download.getbukkit.org/craftbukkit/craftbukkit-{version}.jar")
    elif server == "Spigot":
        version = input("What version of Spigot do you want to download")
        print(f"Downloading spigot-{version}.jar")
        fileDownloader(f"https://download.getbukkit.org/spigot/spigot-{version}.jar")
        bungee = input("Do you want this server to be setup as a bungeecord subserver? (y,n)")
        if bungee == "y":
            BungeeCordSetup()
    elif server == "BungeeCord":
        print(f"Downloading BungeeCord.jar")
        fileDownloader(f"https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar")
    elif server == "Purpur":
        version = input("What version of Purpur do you want to download?")
        print(f"Downloading purpur.jar")
        fileDownloader(f"https://api.purpurmc.org/v2/purpur/{version}/latest/download")
        os.rename("download", "purpur.jar")
        bungee = input("Do you want this server to be setup as a bungeecord subserver? (y,n)")
        if bungee == "y":
            BungeeCordSetup()


code_to_soft = {"1":"Purpur","2":"Paper","3":"Spigot","4":"Craftbukkit","5":"Velocity","6":"BungeeCord"}
def translateDownload(software):
    if software in code_to_soft.keys():
        return code_to_soft[software]
    else:
        return None


def menu():
    option = input("What software do you want to install?\n[6] BungeeCord\n[5] Velocity\n[4] Craftbukkit\n[3] Spigot\n[2] Paper\n[1] Purpur\n$ ")
    downloadManager(translateDownload(option))


def main():
    print("This script will convert this directory into a minecraft server or proxy")
    keep = input("Press ENTER to continue!")
    menu()


main()
