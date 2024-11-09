#!/bin/bash

docker kill fterm 2>/dev/null

docker build -f Dockerfile . -t fterm

docker run --rm -p 8082:80 --name fterm fterm