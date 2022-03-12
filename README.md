# Flower Classifier 🍃

[![Test](https://github.com/omonimus1/plant_classification/actions/workflows/test.yml/badge.svg)](https://github.com/omonimus1/plant_classification/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/omonimus1/plant_classification/branch/dev/graph/badge.svg?token=MXVI6OEXK9)](https://codecov.io/gh/omonimus1/plant_classification)

The current repository contains Davide Pollicino' Honours Project. The project (still under evolution), is the implementation of a CNN ables to classify a flower by receiving in input an image. 
The machine learning model, is the the integrated and used in a Django Web APP, where user are able to:
* Classify a flower
* Leave a feedback related to the prediction
* Save a prediction as favourite
* Register, Login, and gets the user's favourite position. 


#### Project assets
* Jupiter Notebook
* Web App

#### Technologies
<img src="https://img.shields.io/badge/Tensorflow-F7DF1E?style=for-the-badge&logo=tensorflow&logoColor=black%22"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/Jquery-F7DF1E?style=for-the-badge&logo=jquery&logoColor=black%22"> <img src="https://img.shields.io/badge/Bootstrap-d24dff?style=for-the-badge&logo=bootstrap&logoColor=black%22"> 
<!--<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"> -->
#### How to run the project
```
# create virtual environemnt
python3 -m venv venv

# install project requirements
source venv/bin/activate
pip3 install -r requirements.txt

# run migrations
python3 manage.py makemigrations
python3 manage.py migrate

# create superuser
python3 manage.py creatersuper

# run application
python3 manage.py runserver
```
(Note: manage.py may be located inside the webappClassifier folder :) )
#### Coding style checks adopted
* Coding style: Black
* Python Lint: Flake8, flake8-todos
* mypy (for english type checking)
```
# format folder
black folder_name
# Remote all white spaces from project files
trim .
# Format file to improve syntax in according to flake8 (yes -> 2 times --aggressive)
autopep8 --in-place --aggressive --aggressive filename.py
```
