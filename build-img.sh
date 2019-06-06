#!/bin/bash
set -e

# check the parameters
if [ "$#" -ne 2 ]; then
    echo "Usage: ./build-img.sh <tag> <distro>"
    exit 1
fi

# build the image
distro=$2
constellation_tag=$1
docker build \
	-t constellation:${constellation_tag} \
	--build-arg ledger_tag=${constellation_tag} \
	-f ${distro}/Dockerfile \
	.
