#!/bin/bash

git pull --all
git checkout main
git merge release
git commit -m "New release"
git push origin