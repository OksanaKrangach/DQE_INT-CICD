#!/bin/bash

git pull --all
git checkout release
git merge develop
git commit -m "Release update"
git push origin