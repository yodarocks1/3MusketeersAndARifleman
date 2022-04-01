# Hustle

### This web app will help connect workers with people that need yard work done. This could include, lawn mowing, leaf raking, or snowblowing. 

## Work Space Layout

The app will be stored in this repository along with the documentation of the design process and the documentation of the app. The documentation for both can be found in the folder called "docs".

The actal app will be in the folder called "hustle"

## Version-Control Procedures

Every person on the team has a personal branch that they will use to develope on. When a change is needed to be merged with the main branch, the person that made the change will have to create a pull request. Then the rest of the team will look it over discuss and approve it. 

## Tool Stack Description and Setup

Django will be used to create and manage the web apps database. Django uses python and it's somthing that everyone on the team has some experience in making it a great choice.

## Build Instructions

Clone the project in gitbash. ``` bash $ git clone https://github.com/yodarocks1/3MusketeersAndARifleman ```

The next steps are subject to change.

- run ``` pip install django-localflavor ```

- run ``` pip install django-crispy-forms ```

- run ``` python manage.py makemigrations ```

- run ``` python manage.py migrate ```

- run ``` bash $ python manage.py runserver ```

- Type localhost:8000\main in a browser to see the app running

## Unit Testing Instructions

To run the unit tests first follow all the build instructions expect for actally running the main server then:
run ``` python manage.py test ```

if all the tests pass you will see this:

```
Creating test database for alias 'default'...
....
----------------------------------------------------------------------
Ran 4 tests in 1.028s

OK
Destroying test database for alias 'default'...
System check identified no issues (0 silenced).
```

The unit tests test all the data base obejcts to make sure that everything is working with inserting things into the database and making sure the connectins all work

## System Testing Instructions

Once the app is implemented this is what you will use to start up the project to start testing it.

Start by running an instance of the web app by first entering the correct repository and then by entering the following bash $ python manage.py runserver  Now
that the app is running, open an internet browser and enter the address localhost:8000\main. The testing username and pasword will be described later but will allow the user to test every system in the app.

## Other Development Notes

### Naming Conventions
#### The naming conventions for variables, functions, classes, and everything else (subject to change)
- Variables: normal_variableName, CONSTANT_VARIABLE_NAME
- functions/methods: normal_functionName(), normal_MethodName()
- classes: NormalClassName


