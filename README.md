# Evoting

This is an online voting REST API written with django rest framework. You can use this API as the backend for an online voting app. There are endpoints for user registration and login with token based authentication.

## Usage
>If you don't have python installed download it from [here](https://www.python.org/downloads/)
1. Assuming you have [git](https://git-scm.com/downloads) installed run the command below. 
```bash
git clone https://github.com/shitemoticon/evoting.git
```
>Or download a zip copy of this repo from [here](https://github.com/shitemoticon/evoting/archive/refs/heads/main.zip)
  

2. Open the resulting folder with name `evoting` in your favourite code editor. If you downloaded a zip extract it and open `evoting` in your code editor.

3. Rename the file `my-settings.py` found in the folder `gctu` to `settings.py`

4. Run the command below to install the necessary requirements.
```bash 
pip install -r requirement.txt
``` 
5. Create folders (the name should be `migrations`) in the folders `account` and `elections` 
>These two folders are **required** because they store your database migration files. Create them before you continue.

6. In `settings.py` configure your database in the `DATABASES` dictionary like below.
```python
DATABASES = {
    # set this before making migrations
    'default': {
        # the ENGINE depends on the database you use. I use postgreSQL do some googling here in case you use a different database
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER': 'database_username',
        'PASSWORD': 'database_password',
        # HOST is where your database is hosted. Put the url
        'HOST': 'localhost'

    }
}
```
Next in settings add your CORS allowed urls if applicable. Find the list below and include your urls.

```python
#set this if your frontend (app using API) is hosted on the same machine as the API.
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080'
]
```

7. Run the command below it'll open a python shell (You're going to generate a secret key).
```bash
python manage.py shell
```
>Make sure you're in the `evoting` directory before running any commands

to generate a secret key run the following python code line by line in the python shell. Output should be similar to below.
```python
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
# your secret key will be different from the one below
'!zbc+#^q!nc&t(w1%0+6ip$+_5$r3$btx#_+p)@b=slk_hz2v)'
```
8. Copy the secret key you generated from step 7 and set to the `SECRET_KEY` constant in the `settings.py` like below.
```python
SECRET_KEY = '!zbc+#^q!nc&t(w1%0+6ip$+_5$r3$btx#_+p)@b=slk_hz2v)'
```

9. Run the command below to make your migrations.
```bash
python manage.py makemigrations
```
Then run the command below to migrate your models and create tables in your database.
```bash
python manage.py migrate
```
you can now check the availabe endpoints in `urls.py`, Good luck!


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU](https://choosealicense.com/licenses/gpl-3.0/)
