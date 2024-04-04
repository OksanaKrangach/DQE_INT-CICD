#!/bin/bash

git checkout develop
git pull
git checkout release
git pull
git merge develop
git commit -m "Release update"
git push origin