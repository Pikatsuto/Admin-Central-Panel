#!/bin/bash

sudo docker build -t pikatsuto/admin-central-panel .
sudo docker compose up -d

sudo nano /var/lib/docker/volumes/proadmin_full_WebPanel_Data/_data/data.json