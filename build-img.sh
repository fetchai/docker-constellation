#!/bin/bash
set -e

# check the parameters
if [ "$#" -ne 1 ]; then
    echo "Usage: ./build-img.sh <tag>"
    exit 1
fi

# build the image
constellation_tag=$1
docker build -t constellation:${constellation_tag} --build-arg ledger_tag=${constellation_tag} .
