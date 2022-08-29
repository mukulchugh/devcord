# Devcord Web Application
A Web App buIlt using Django for developers to connect and collaborate

![alt text](https://github.com/mukulchugh/devcord/blob/master/screenshot.png?raw=true)


## DEMO 
http://mukulchugh.pythoneverywhere.com

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/mukulchugh/devcord.git
$ cd devcord
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.
