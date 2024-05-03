#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
# file existence check
if [ ! -d /data/web_static/releases/ ]; then
        sudo mkdir -p /data/web_static/releases/test/
fi

if [ ! -d /data/web_static/shared/ ]; then
        sudo mkdir -p /data/web_static/shared/
fi
# test file
echo "<!DOCTYPE>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null
target="/data/web_static/releases/test"
link="/data/web_static/current"
if [ -L "$link" ]; then
    sudo rm "$link"
fi
sudo ln -s "$target" "$link"

sudo chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served by $hostname;
    root /var/www/html;
    index index.html index.htm;

    location /hbh_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html{
        internal;
    }
}" | sudo tee /etc/nginx/sites-available/default >/dev/null

sudo service nginx restart
