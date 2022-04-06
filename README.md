# Flower Classifier 🍃
[![Test](https://github.com/omonimus1/plant_classification/actions/workflows/test.yml/badge.svg)](https://github.com/omonimus1/plant_classification/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/omonimus1/plant_classification/branch/dev/graph/badge.svg?token=MXVI6OEXK9)](https://codecov.io/gh/omonimus1/plant_classification)

The current repository contains Davide Pollicino' Honours Project. The project (still under evolution), is the result of three research questions:
* What are possible approaches to feature enginnering for the implementation of a classifier able to distinguish flower variants incredibly similar between them, even at differnt life stages and growth locations;
* Which CNN architecture would offer best performances 
* Is is possible to integrate a machine learning model within a django App, without that this model would first be deployed in a cloud service and exploses via endpoint? 

## Technologies
<img src="https://img.shields.io/badge/Tensorflow-F7DF1E?style=for-the-badge&logo=tensorflow&logoColor=black%22"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/Jquery-F7DF1E?style=for-the-badge&logo=jquery&logoColor=black%22"> <img src="https://img.shields.io/badge/Bootstrap-d24dff?style=for-the-badge&logo=bootstrap&logoColor=black%22"> 
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![CodeCov](https://img.shields.io/badge/codecov-%23ff0077.svg?style=for-the-badge&logo=codecov&logoColor=white)

## Web application functionalities
The machine learning model, is the the integrated and used in a Django Web APP, where user are able to:
* Classify a flower
* Leave a feedback related to the prediction
* Save a prediction as favourite
* Register, Login, and gets the user's favourite position. 







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
