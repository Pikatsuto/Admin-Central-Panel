<img src="https://i.imgur.com/uhqu2tr.png " data-canonical-src="https://i.imgur.com/uhqu2tr.png " width="100%"/>

## Description EN
Admin Control Panel is a centralized admin panel for all your interfaces using iframe. It contains by default WebTerminal, Nginix Proxy Reverse, Portainer, Dozzle and 2 links to Freenom and CloudFlere

## Description FR
Admin Contrôle Panel est un panel administrateur de centralisation  pour toute vos interfaces à l'aide d'iframe. Il contient par defaut WebTerminal, Nginix Proxy Reverse, Portainer, Dozzle et 2 lien vers Freenom et CloudFlere

## Screen

<img src="https://i.imgur.com/juJLCv3.png " data-canonical-src="https://i.imgur.com/juJLCv3.png "  width=100%/>

<img src="https://i.imgur.com/2BZvrYf.png" data-canonical-src="https://i.imgur.com/2BZvrYf.png"  width="100%"/>

<img src="https://i.imgur.com/9wg8rZV.png " data-canonical-src="https://i.imgur.com/9wg8rZV.png"  width="100%"/>

<img src="https://i.imgur.com/vUQhmgG.png " data-canonical-src="https://i.imgur.com/vUQhmgG.png"  width="100%"/>

<img src="https://i.imgur.com/vE52iWr.png " data-canonical-src="https://i.imgur.com/vE52iWr.png "  width="100%"/>

## Docker Compose

Link of icon for portainer : `https://i.imgur.com/X4e5UHV.png`

```yml
################
version: '3.9' #
services:      #
################
#
#
#################################################################
# Afficher les logs des Conteneurs via une WebUI
  CN_AdminCentralPanel_Dozzle: 
    # --------------------------------------------------------- #
    image: 'amir20/dozzle'
    container_name: 'CN_AdminCentralPanel_Dozzle'
    # --------------------------------------------------------- #
    network_mode: 'bridge'
    # --------------------------------------------------------- #
    hostname: 'CN_AdminCentralPanel_Dozzle'
    # --------------------------------------------------------- #
    restart: 'always'
    # --------------------------------------------------------- #
    volumes:
      - '/var/run/docker.sock:/var/run/docker.sock'
    # --------------------------------------------------------- #
    ports:
      - 8003:8080
#################################################################
#
#
#################################################################
  CN_AdminCentralPanel_WebTerminal_GuaCd:
    # --------------------------------------------------------- #
    image: 'guacamole/guacd:0.9.14'
    # --------------------------------------------------------- #
    network_mode: 'bridge'
    # --------------------------------------------------------- #
    environment:
      GUACDHOST: 'CN_AdminCentralPanel_WebTerminal_GuaCd'
      REDISHOST: 'CN_AdminCentralPanel_WebTerminal_Redis'
      WEBTERMINALHOST: 'WebTerminal'
    # --------------------------------------------------------- #
    volumes:
      - 'WebTerminal_Recording:/opt/webterminal/media/'
#################################################################
#
#
#################################################################
  CN_AdminCentralPanel_WebTerminal_Redis:
    # --------------------------------------------------------- #
    image: 'redis:6.0-alpine'
    # --------------------------------------------------------- #
    network_mode: 'bridge'
#################################################################
#
#
#################################################################
  CN_AdminCentralPanel_WebTerminal_WebSite:
    # --------------------------------------------------------- #
    image: 'webterminal/webterminal:beta'
    # --------------------------------------------------------- #
    network_mode: 'bridge'
    # --------------------------------------------------------- #
    environment:
      GUACDHOST: 'CN_AdminCentralPanel_WebTerminal_GuaCd'
      REDISHOST: 'CN_AdminCentralPanel_WebTerminal_Redis'
    # --------------------------------------------------------- #
    volumes:
      - 'WebTerminal_Recording:/opt/webterminal/media/'
      - 'WebTerminal_DtatBase:/opt/webterminal/db/'
    # --------------------------------------------------------- #
    links:
      - 'CN_AdminCentralPanel_WebTerminal_Redis'
      - 'CN_AdminCentralPanel_WebTerminal_GuaCd'
    # --------------------------------------------------------- #
    ports:
      - 8002:80
#################################################################
#
#
#################################################################
# http://Your_IP:9443/ => https://portainer.exemple.fr/
  CN_AdminCentralPanel_Portainer:
    # --------------------------------------------------------- #
    image: 'portainer/portainer-ce'
    container_name: 'CN_AdminCentralPanel_Portainer'
    # --------------------------------------------------------- #
    network_mode: 'bridge'
    # --------------------------------------------------------- #
    restart: 'always'
    # --------------------------------------------------------- #
    volumes:
      - 'Portainer_Data:/data'
      - '/var/run/docker.sock:/var/run/docker.sock'
    # --------------------------------------------------------- #
    ports:
      - 9443:9443
#################################################################
#
#
#################################################################
  CN_AdminCentralPanel_WebPanel:
    # --------------------------------------------------------- #
    image: 'pikatsuto/admin-central-panel'
    container_name: 'CN_AdminCentralPanel_WebPanel'
    # --------------------------------------------------------- #
    network_mode: 'bridge'
    # --------------------------------------------------------- #
    restart: 'always'
    # --------------------------------------------------------- #
    volumes:
      - 'WebPanel_Data:/usr/local/apache2/htdocs'
    # --------------------------------------------------------- #
    ports:
      - 8001:80
    # --------------------------------------------------------- #
    environment:
      PortainerHttpOrHttps: 'https'
      WebSshHttpOrHttps: 'http'
      DozzleHttpOrHttps: 'http'
      ProxyHttpOrHttps: 'http'
      # ------------------------------------------------------- #
      PortainerIp: '0.0.0.0'
      WebSshIp: '0.0.0.0'
      DozzleIp: '0.0.0.0'
      ProxyIp: '0.0.0.0'
      # ------------------------------------------------------- #
      PortainerPort: '9443'
      WebSshPort: '8002'
      DozzlePort: '8003'
      ProxyPort: '81'
#################################################################
#
#
#################################################################
# Email: admin@example.com | pass: changeme
# http://Your_IP:81/ => https://proxy.exemple.fr/
  CN_AdminCentralPanel_NginxProxyManager:
    # --------------------------------------------------------- #
    image: 'jc21/nginx-proxy-manager:latest'
    container_name: 'CN_AdminCentralPanel_NginxProxyManager'
    # --------------------------------------------------------- #
    network_mode: 'host'
    # --------------------------------------------------------- #
    restart: 'unless-stopped'
    # --------------------------------------------------------- #
    volumes:
      - 'NginxProxyManager_Data:/data'
      - 'NginxProxyManager_SSL:/etc/letsencrypt'
#################################################################
#
#
###########################
# Déclaration des volumes #
###########################
volumes:
  # --------------------- #
  WebTerminal_DtatBase:
    external: false
  # --------------------- #
  WebTerminal_Recording:
    driver: 'local'
  # --------------------- #
  Portainer_Data:
    external: false
  # --------------------- #
  WebPanel_Data:
    external: false
  # --------------------- #
  NginxProxyManager_Data:
    external: false
  # --------------------- #
  NginxProxyManager_SSL:
    external: false
  # --------------------- #
  PiHole_PiHole:
    external: false
  # --------------------- #
  PiHole_DnsMasq:
    external: false
  # --------------------- #
```

Commande de lancement
```bash
docker compose up -d
```