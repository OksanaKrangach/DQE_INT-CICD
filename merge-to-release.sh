#!/bin/bash

git config --global user.email "oksana_krangach@epam.com"
git config --global user.name "Oksana Krangach"

git checkout develop
git pull
git checkout release
git pull
git merge develop
git commit -m "Release update"
echo "====================================================================="
git status
echo "====================================================================="
git push

git checkout feature1