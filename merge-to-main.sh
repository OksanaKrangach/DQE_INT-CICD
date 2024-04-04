#!/bin/bash

#git config --global user.email "oksana_krangach@epam.com"
#git config --global user.name "Oksana Krangach"

echo "====================================================================="
echo "START"
pwd
echo "====================================================================="
git status
echo "====================================================================="
git checkout release
git pull
git checkout main
git pull
git merge release
git commit -m "New release"
echo "====================================================================="
git status
echo "====================================================================="
#git push

git checkout feature1