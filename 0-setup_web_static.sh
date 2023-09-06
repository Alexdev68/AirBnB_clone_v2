#!/usr/bin/env bash
# This script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/test/ && touch /data/web_static/releases/test/index.html
mkdir -p /data/web_static/shared/

cat <<EOF > /data/web_static/releases/test/index.html
<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>
EOF

if [ -L /data/web_static/current ]; then
	rm /data/web_static/current
fi

ln -s /data/web_static/releases/test/* /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

echo "\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}" >> /etc/nginx/sites-available/default
sudo service nginx restart
