sudo /etc/init.d/mysql restart
python /home/box/web/ask/manage.py syncdb --noinput
sudo ln -fs /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo unlink /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -fs /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/ask_wsgi.conf   /etc/gunicorn.d/ask_wsgi.conf
sudo /etc/init.d/gunicorn restart
