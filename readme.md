# Cados

My Submission for October Hackathon 🎃 APIs Edition

[More Info](https://codebattles.dev/event/dce4b8cd-b48d-4511-b4d6-b0058c179944/)


## Run the server

Get the source code 💻

```
git clone https://github.com/foxy4096/Cados.git
```

Go the the dir 📁

```
cd Cados
```

Add the enviroment variables :gear:

In `Powershell` or `terminal` 💻 *(Not in cmd, it doesn't support touch command)*

```
touch Cados/.env
```

In `.env` add the following variables ➕

```py
DEBUG:bool # Default True
WEBHOST:str # Default "http://localhost:8000"
API_AUTH_KEY:str # Default "secret"
```



Make a virtualenv 📡

```
pip install virtualenv
virtuatenv venv
```

Install the dependencies 🔨

```
pip install -r req.txt
```

Make Migrations 💿

On Windows 📁:
```
python manage.py makemigrations
```

On Linux/Unix systemm 🐧:
```
python3 manage.py makemigrations