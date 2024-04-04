#!/bin/bash

git checkout release
git merge develop
git commit -m "Release update"
git push origin