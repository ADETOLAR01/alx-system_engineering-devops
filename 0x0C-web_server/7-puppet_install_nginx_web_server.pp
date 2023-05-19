# Install and config the nginx
package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'apt-get update ; apt-get -y install nginx',
  provider => shell,
}

exec {'Hello World!':
  command  => 'echo "Hello World!" | dd status=none of=/var/www/html/index.html',
  provider => shell,
}

exec {'sed -i 's/listen\s*80;/listen 80 default_server;/g' /etc/nginx/sites-available/default,
}

echo 'location /redirect_me { return 301 http://example.com/new_page}' >> /etc/nginx/sites-available/default

echo '<html>
<head><title>404 Not Found</title></head>
<body>
    <h1>404 Not Found</h1>
    <p>Ceci n&apos;est pas une page.</p>
</body>
</html>' > /var/www/html/404.html

sed -i 's|#error_page 404 /404.html;|error_page 404 /404.html;|' /etc/nginx/sites-available/default

service nginx restart4 page.
