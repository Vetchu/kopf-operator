#!/bin/bash -ex
docker build -t vetch/basic-kopf:tagname10 --build-arg ssh_prv_key="$(cat ~/.ssh/id_rsa_tmp)" .
docker push vetch/basic-kopf:tagname10
