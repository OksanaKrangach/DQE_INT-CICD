#!/bin/bash

#git config --global user.email "oksana_krangach@epam.com"
#git config --global user.name "Oksana Krangach"

echo "#####################################################################"
echo "START merge_to_release"
echo "---------------------------------------------------------------------"

git checkout develop
git pull
git checkout release
git pull
git pull
git merge develop
git commit -m "Release update"

echo "---------------------------------------------------------------------"
echo "FINISH  merge_to_release"
echo "#####################################################################"
