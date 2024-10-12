#!/bin/bash

# Update package list and install Git LFS
apt-get update && apt-get install -y git-lfs

# Initialize Git LFS and pull files
git lfs install
git lfs pull
