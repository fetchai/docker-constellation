# Supported Tags & Dockerfiles

Current Versions:

* [0.9.1, 0.9, latest](https://github.com/fetchai/docker-constellation/blob/master/ubuntu/Dockerfile)

Previous Releases:

* [0.8.1, 0.8](https://github.com/fetchai/docker-constellation/blob/master/ubuntu/Dockerfile)
* [0.7.1, 0.7](https://github.com/fetchai/docker-constellation/blob/master/ubuntu/Dockerfile)
* [0.6.1, 0.6](https://github.com/fetchai/docker-constellation/blob/master/ubuntu/Dockerfile)
* [0.6.1-alpine, 0.6-alpine](https://github.com/fetchai/docker-constellation/blob/master/alpine/Dockerfile)
* [0.5.1, 0.5](https://github.com/fetchai/docker-constellation/blob/master/ubuntu/Dockerfile)
* [0.5.1-alpine, 0.5-alpine](https://github.com/fetchai/docker-constellation/blob/master/alpine/Dockerfile)
* [0.4.1-rc5](https://github.com/fetchai/docker-constellation/blob/master/ubuntu/Dockerfile)
* [0.3.1, 0.3](https://github.com/fetchai/docker-constellation/blob/master/ubuntu/Dockerfile)
* [0.3.1-alpine, 0.3-alpine](https://github.com/fetchai/docker-constellation/blob/master/alpine/Dockerfile)

## Quick Reference

* Support documentation available at the [Community Website](https://community.fetch.ai/)

* Where to file issues: [https://github.com/fetchai/docker-constellation](https://github.com/fetchai/docker-constellation)

* Maintained by: [The Fetch.AI Ledger Team](https://github.com/fetchai/ledger)

* Supported architectures: amd64

## What is Constellation?

Constellation is the single executable version of the Fetch.AI smart ledger. This version of the ledger is idea for test deployments and evaluation of the ledger technology.

## How to use this image

To run a single instance for testing, users can use the default options in the command line

    $ docker run fetchai/constellation

To specify the command line arguments like controlling the block interval:

    $ docker run fetchai/constellation -standalone -block-interval 5000

# License

View [license information](https://github.com/fetchai/ledger/blob/master/LICENSE) for the software contained in this image.

As with all Docker images, these likely also contain other software which may be under other licenses (such as Bash, etc from the base distribution, along with any direct or indirect dependencies of the primary software being contained).

As for any pre-built image usage, it is the image user's responsibility to ensure that any use of this image complies with any relevant licenses for all software contained within.
