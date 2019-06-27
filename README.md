# Constellation Docker Image

The following repository contains the docker images used in order to build and particular version of
the Fetch.AI ledger (constellation). Currently the following flavours of docker images are available:

* Ubuntu
* Alpine

## Build

Enclosed in this project is a utility script for building the docker images. To build a image simply
run the shell script with a given tag name (or branch name) and distribution:

    ./build-img.py v0.5.1 ubuntu

