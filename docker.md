## Docker Up and Running 

On Mac or Windows docker is accessed via a virtual machine so it may be a bit slower relative to running natively on linux

Anything that involves a file system will be slow

Stacked file system layer so if you change a few lines of code in Dockerfile you don't need to rebuild the entire image

Java has Web Application Archive (that's probably where the name comes from for mar files)

Coding against a specific version of a docker container is helpful because you don't need to be an expert at how that specific service is deployed

Put torchserve on dockerhub?

One cool idea is atomic hosts that let you rollback to previous images if things break - e.g: Redhat CoreOS

`docker-machine env local` -> sets up a local VM using Virtual box - practical for debugging

`docker build --no-cache` to avoid unexpected build issues

Can run a container interactively from step in build that was broken (page 63)

Share private registries for debugging

alpine linux is a lightweight distribution with a different standard library that's popular for Docker

tagging images is a great way to compare multiple versions

Docker images can't get smaller - layers are additive by nature (similar to git)

using `time` utility to measure deployment times

Put stuff that changes often in one of the later layers so cache isn't invalidated

Origin of containers is the `chroot` unix function

Can change docker container constraints with `docker container update` 

At startup time containers gets DNS, volume and mac address - can configure all of these (I think there are defaults)

Look into `nsenter` command

Linux has `/bin/true` and `/bin/false`