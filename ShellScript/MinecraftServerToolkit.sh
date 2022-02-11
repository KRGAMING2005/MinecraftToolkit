#! /bin/bash
# TheDeQ Minecraft Server Toolkit 2022

isPresent() { command -v "$1" &> /dev/null && echo 1; }

CURL_IS_PRESENT=$(isPresent curl)
BUILD="NULL"

splashScreen() {
    BoldText=$(tput bold 2> /dev/null)
    NormalText=$(tput sgr0 2> /dev/null)
    UnderlineText=$(tput smul 2> /dev/null)

    echo 'Minecraft Server Toolkit'
    echo 'This script will convert the current directory into a Minecraft server or proxy.'
    echo ''
    read -p "Press enter to contine!" option
    if [[ $option == "" ]]; then
        menu
    fi
}

menu() {
    echo "What software do you want to install?"
    echo '[6] BungeeCord'
    echo '[5] Velocity'
    echo '[4] Craftbukkit'
    echo '[3] Spigot'
    echo '[2] Paper'
    echo '[1] Purpur'
    read -p '$ ' option
    minecraftVersion $option
}

minecraftVersion() {
    read -p "What minecraft version do you want ot install? " option
    if [[ $1 == 2 ]]; then
        getLatestBuild 'paper' $option
    elif [[ $1 == 5 ]]; then
        if [[ $option == '1.18.1' ]]; then
            getLatestBuild 'velocity' '3.1.1'
        else
            getLatestBuild 'velocity' '3.1.1'
        fi
    fi

}

getLatestBuild() {
    request=$(curl https://papermc.io/api/v2/projects/$1/versions/$2 | jq '.builds | length')
    arrayID=$(($request - 1))
    build=$(curl https://papermc.io/api/v2/projects/$1/versions/$2 | jq ".builds[$arrayID]")
    downloadFile $1 $2 $build
}

downloadFile() {
    echo "\n\n\nDownloading $1-$2-$3.jar ..."
    download=$(wget -O $1-$2-$3.jar https://papermc.io/api/v2/projects/$1/versions/$2/builds/$3/downloads/$1-$2-$3.jar > $1-$2-$3.jar)
    echo "$download"
    echo "\n\n\nDownloaded $1-$2-$3.jar"
}

splashScreen