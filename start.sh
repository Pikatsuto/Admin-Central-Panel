#!/bin/bash

sudo docker build -t pikatsuto/admin-central-panel .
sudo docker compose up -d

sudo rm /var/lib/docker/volumes/AdminCentralPanel_Data/_data/*

sudo cp ./site/* /var/lib/docker/volumes/AdminCentralPanel_Data/_data/