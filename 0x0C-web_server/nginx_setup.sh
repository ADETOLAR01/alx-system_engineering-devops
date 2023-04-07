#!/bin/bash

# Install nginx
apt-get update
apt-get -y install nginx

# Configure nginx
echo "server {
    listen 80;
    root /var/www/html;
    index index.html;

    location / {
        echo 'Hello World!';
    }
}" > /etc/nginx/sites-available/default

# Restart nginx
service nginx restart
