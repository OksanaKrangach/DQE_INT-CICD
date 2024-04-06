#!/bin/bash

#git config --global user.email "oksana_krangach@epam.com"
#git config --global user.name "Oksana Krangach"

echo "#####################################################################"
echo "START merge_to_release"
echo "---------------------------------------------------------------------"

git checkout release
git pull
git checkout main
git pull
git merge release
git commit -m "New release"
git checkout feature1

echo "---------------------------------------------------------------------"
echo "FINISH  merge_to_release"
echo "#####################################################################"
