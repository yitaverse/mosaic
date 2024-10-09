## How to run in a terminal:

```
git clone https://github.com/yitaverse/mosaic.git
cd ./mosaic
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

With the second to last command you create a superuser to be able to access (after the last command, `python manage.py runserver`) `http://localhost:8000/admin/` to administer the site.

Visit `http://localhost:8000/` to log in with the credentials.

Press `CTRL+C`, in the terminal, to close Django server.

Run `pip freeze > requirements.txt` to export `requirements.txt`, if modified.

Run `deactivate`, in the terminal, to close the python virtual environment.
