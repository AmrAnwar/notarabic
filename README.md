# not arabic
Simple Dictionary Api Similar To Urban Dictionary

## About the Api:

**not arabic** is a simple dictionary API using Django restframework, user can (get, add) **words**, and **upvote** or **downvote** it and get data about the words popularity similar to **Urban Dictionary**

---

## Project Archetiecture [link](https://drive.google.com/file/d/14UaZKbFcpjQBvYtB40IUxxLHfnGgt24D/view?usp=sharing "link") or photos below:

### - Models:

[![Models](https://www7.0zz0.com/2019/06/10/20/502454527.jpeg)](https://www7.0zz0.com/2019/06/10/20/502454527.jpeg)

### - Requests and Permissions:

[![Permissions](https://www5.0zz0.com/2019/06/10/21/452319419.jpeg "Permissions")](https://www5.0zz0.com/2019/06/10/21/452319419.jpeg "Permissions")

### - Views: 

[![Views](https://www5.0zz0.com/2019/06/10/21/854204385.jpeg)](https://www5.0zz0.com/2019/06/10/21/854204385.jpeg)

## run the project: 
```
virtualenv -p python3 <path>/notarabic-env
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## requests examples 

### Words list: 

[![](https://www3.0zz0.com/2019/06/10/22/904453314.jpeg)](https://www3.0zz0.com/2019/06/10/22/904453314.jpeg)

### Retrieve user word instance:
[![](https://www3.0zz0.com/2019/06/10/22/494644414.jpeg)](https://www3.0zz0.com/2019/06/10/22/494644414.jpeg)

-----

## Technologies:
- Django
- Django GIS built-in library & geoip2.
- Django Rest Framework
- Docker
- Postgres
- Factories using Factory boy 

## in code you can useful learning exmaples to:
- convert the Archecture to real life code
- CBV using Django rest ( class based view).
- using routers in django urls.
- Paginations.
- simpple usage to Django GIS library to get the user request country.
- mange user permission for the APIs.
- Factories (using Factory boy) to create dummy data and using it in testing
- Create docker containers to the app
- TDD ( test driving development) using Unit testing **[TODO] **


