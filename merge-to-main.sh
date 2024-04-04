#!/bin/bash

git checkout release
git pull
git checkout main
git pull
git merge release
git commit -m "New release"
git push origin