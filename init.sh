sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3

sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==2.2.2
sudo python3 -m pip install mysqlclient


sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database stepic_web;"
sudo mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"


sudo rm -r /etc/nginx/sites-enabled/*
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart


#gunicorn hello:app --bind='0.0.0.0:8080' &
#sudo python3 manage.py runserver 0.0.0.0:8000

#sudo python3 /ask/manage.py migrate

sudo gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask ask.wsgi:application



