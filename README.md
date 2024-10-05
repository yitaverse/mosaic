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
python manage.py runserver
```

Now visit:
http://localhost:8000/

Press `CTRL+C`, in the terminal, to close Django server.

Run `deactivate`, in the terminal, to close the python virtual environment.
