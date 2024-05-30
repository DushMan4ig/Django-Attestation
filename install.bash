pip install django-debug-toolbar
python manage.py startapp random_generator
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev nginx curl
sudo apt install postgresql postgresql-contrib
sudo su - postgres
psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
exit
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
mkdir ~/myproject
cd ~/myproject
virtualenv myprojectenv
source myprojectenv/bin/activate
pip install django gunicorn psycopg2-binary
sudo nano /etc/systemd/system/gunicorn.service
sudo nano /etc/nginx/sites-available/my