#!/bin/bash

sudo docker build -t pikatsuto/admin-central-panel .
sudo docker compose up -d

sudo cat /var/lib/docker/volumes/proadmin_full_WebPanel_Data/_data/index.html