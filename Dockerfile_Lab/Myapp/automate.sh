#!/bin/bash
podman build -t quay.io/rkssgupta/myimage ./myapp
podman push quay.io/rkssgupta/myimage
