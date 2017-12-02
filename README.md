# Flask Chat
A simple chat in flask. More a message board that looks like
in the 80s than a full-featured chat with videos and unicorn.


## Why?
I wanted to have a simple chat with my friends and 
not use snapshot, hangouts or any other popular solutions
that requires to be logged on a system you do not control.

## What?
This is a simple application written in Python/Flask.
It handles a single chat window. Users have to authenticate.

## Requirements
* Single chat window
* Several users
* Admin functions to add/change users
* No plain password stored

### and for later ...
This could be integrated as well
* GIFs search
* Support to check HTML safety

## How to use it?
```bash
git clone https://github.com/juli1/flask-chat.git
cd flask-chat
# Replace the following line with virtualenv if necessary
python3.X -m venv flask # Replace X with your version of python
source flask/bin/activate
pip install -r requirements.txt
./run.py
```

And then, open your browser to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Start with the user *admin*, password *admin*.

## Resources
* [The Flask Website](http://flask.pocoo.org/)
* [The Amazing Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)