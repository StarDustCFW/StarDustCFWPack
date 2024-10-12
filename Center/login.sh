#!/bin/sh
cd "$(dirname "$(readlink -f "$0")")"
t=$(cat token.vbs)
echo $t
git config --global credential.helper store
echo git config --global url."https://api:$t@github.com/".insteadOf "https://github.com/"
git config --global url."https://api:$t@github.com/".insteadOf "https://github.com/"
git config --global user.email "Kronos2308@gmail.com"
git config --global user.name "Kronos2308"

sleep 06

exit