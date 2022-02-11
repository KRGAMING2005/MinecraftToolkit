import os
import json
import requests as req
from subprocess import STDOUT, Popen
import fileinput

def BungeeCordSetup():
    fileURL = "https://raw.githubusercontent.com/KRGAMING2005/MinecraftToolkit/main/serverFiles/"
    fileDownloader(fileURL + "server.properties")
    fileDownloader(fileURL + "spigot.yml")
    for line in fileinput.input("spigot.yml", inplace=True):
        print('{} {}'.format(fileinput.filelineno(), line), end='')

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
        version = input("What version of Velocity do you want to donwload? ")
        print(f"Downloading velocity-{version}-{getLatesBuild('velocity', version)}.jar")
        fileDownloader(getPaperDownloadURL("velocity", version, getLatesBuild("velocity", version)))

    elif server == "Paper":
        version = input("What version of Paper do you want to donwload? ")
        print(f"Downloading paper-{version}-{getLatesBuild('paper', version)}.jar")
        fileDownloader(getPaperDownloadURL("paper", version, getLatesBuild("paper", version)))


def translateDownload(software):
    if software == "6":
        return "BungeeCord"
    elif software == "5":
        return "Velocity"
    elif software == "4":
        return "Craftbukkit"
    elif software == "3":
        return "Spigot"
    elif software == "2":
        return "Paper"
    elif software == "1":
        return "Purpur"


def menu():
    option = input("What software do you want to install?\n[6] BungeeCord\n[5] Velocity\n[4] Craftbukkit\n[3] Spigot\n[2] Paper\n[1] Purpur\n$ ")
    downloadManager(translateDownload(option))


def main():
    print("This script will convert this directory into a minecraft server or proxy")
    keep = input("Press ENTER to continue!")
    menu()


main()
