#!/bin/bash

git checkout main
git merge release
git commit -m "New release"
git push origin