#!/bin/bash

#git config --global user.email "oksana_krangach@epam.com"
#git config --global user.name "Oksana Krangach"

echo "#####################################################################"
echo "START merge_to_main"
echo "---------------------------------------------------------------------"

git checkout release
git pull
git checkout main
git pull
git merge release
git commit -m "New release"

echo "---------------------------------------------------------------------"
echo "FINISH  merge_to_main"
echo "#####################################################################"
