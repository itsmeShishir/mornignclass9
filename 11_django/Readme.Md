# Django

## Process to Create Django Application using Virtual Environment
    - pip install virtualenv
    - mkdir 11_django
    - cd 11_django
    - python -m venv env
    - source env/bin/activate -> mac
    -.\env\Scripts\activate -> windows
    - pip install django
    - pip freeze > requirements.txt
    - django-admin --version 
    - django-admin startproject core .

    - Blog Application
        - python manage.py startapp blog
        - python manage.py startapp auths
    
    - To run our application we need to use
        - python manage.py runserver
    
    - we need to add the app in settings.py 
        - INSTALLED_APPS = [
            'auths',
            'blog',
        ]
    - We need to do makemigrations and migrate
        - python manage.py makemigrations
        - python manage.py migrate

    - To create a Super user 
        - python manage.py createsuperuser
    
    
