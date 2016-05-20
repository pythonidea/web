sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo gunicorn -b 0.0.0.0:8080 hello:wsgi_application
sudo /etc/init.d/gunicorn restart
