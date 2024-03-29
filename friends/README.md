FRIENDS
=============================================

> A blog for friends to share problems

* Live at heroku : [friendzbook.herokuapp.com](https://friendzbook.herokuapp.com/)

## Features
* Blog
* Upload image to Google Drive
* Login/Registration
* Like/Comment
* Search
* Send E-mail

## Used Technologies
* Python
* Django
* SQLite3
* PostgreSQL
* HTML
* CSS
* JavaScript
* jQuery
* Ajax
* Bootstrap
* Google Drive API


## Installation

### Create virtual environment and goto friends directory
```bash
virtualenv friends
cd .\friends\
```
* copy the project and paste in friends directory

### Activate virtualenv and install reequirements.txt
```bash
.\Scripts\activate
python -m pip install -r .\requirements.txt
```
### goto src directory and make db ready
```bash
cd .\src\
.\manage.py migrate
```
### Run dev server
```bash
.\manage.py runserver 8888
```
* now goto http://127.0.0.1:8888/

## Screenshots

### Homepage
![image](./screenshots/header.png)

![image](./screenshots/index%20page.png)


### Login - Registration

![image](./screenshots/login.png)

![image](./screenshots/registration.png)

### Posts

![image](./screenshots/blog.png)

![image](./screenshots/posts.png)

![image](./screenshots/post%20detail.png)

### Profile

![image](./screenshots/profile.png)

![image](./screenshots/public%20profile.png)

