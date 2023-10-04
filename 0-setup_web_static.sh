#!/usr/bin/env bash
# This script creates a new ubuntu machine with all confi ready for deployment to server
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/  /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo sh -c 'cat sed/file.html > /data/web_static/current/index.html'
sudo sh -c 'echo "Hello World!" > /var/www/html/index.nginx-debian.html'
sudo touch /etc/nginx/html/404.html
sudo sh -c 'echo "Ceci n'\''est pas une page" > /etc/nginx/html/404.html'
sudo sed -i -f sed/insert.sed /etc/nginx/sites-available/default
sudo sed -i -f sed/404.sed /etc/nginx/sites-available/default
sudo sed -i -f sed/alias.sed /etc/nginx/sites-available/default
sudo sed -i -f sed/head.sed /etc/nginx/sites-available/default
sudo service nginx restart
