Run Folowing Commands : 

1. pip install django
    
Setting up Virtual env, Optional if not asked in question : 
a. python -m venv myenv
b. myenv\Scripts\activate

2. django-admin startproject project_name
3. cd project_name
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py startapp app_name
7. Add app_name in project_name > settings.py > INSTALLED_APPS list
8. Make urls.py in app_name directory
9. Open urls.py of project_name and add your url in urlpatterns list, example
    path('?', include("app_name.urls"))  
    (Add any prefix you want in place of '?', Example: "api/" or "")
10. python manage.py runserver 
