# **AnimePedia**

## Overview

Basic Website created using django which shows all Animes and user can upvote an Anime. 
Also new Animes can be added.Anime can be edited/deleted easily.

## Features

#### Admin 
* Admin has the ability to create,edit and delete any Animes.
* 

## Screenshots


## Pending

- [x] Login/Sign Up
- [x] Exception Handling 
- [x] Sort Animes By Name
- [ ] Upvote
- [x] Superuser/Admin can edit/delete/add new animes
- [ ] Forgot Password

## Running this Project


To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

---
