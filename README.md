# VDE Email Sending
Automate email sending using Django

# Requirements
- Python >= 3.6
- virtualenv
- Django >= 2.2
- Celery
```
git clone https://github.com/raquelpanapalen/tgk-vde-emails && cd tgk-vde-emails
virtualenv env --python=python3
source ./env/bin/activate
python manage.py migrate
python manage.py createsuperuser (which is the user who manages the app)
```
# Required variables
- ```EMAIL_HOST_USER``` (email account from where you want the emails to be sent)
- ```EMAIL_HOST_PASSWORD``` (password of EMAIL_HOST_USER email account)
