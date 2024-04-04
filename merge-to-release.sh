#!/bin/bash

git pull --all
git checkout release
git pull
git pull
git merge develop
git commit -m "Release update"
echo "====================================================================="
git status
echo "====================================================================="
git push > /tmp/out 2>&1

git checkout feature1