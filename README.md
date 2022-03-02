# Flower Classifier 🍃

#### Status
[![PIPELINE status](https://github.com/omonimus1/plant_classification/actions/workflows/django.yml/badge.svg)](https://github.com/Potatoapp/backend-and-services-potato/actions/workflows/django.yml)
[![codecov develop](https://codecov.io/gh/omonimus1/plant_classification/branch/develop/graph/badge.svg?token=MXVI6OEXK9)](https://codecov.io/gh/omonimus1/plant_classification)


The current repository hosts Davide Pollicino Honours Project.
The project (still under implementation),
offers research documentation related the implementation of a **Flower Classifier**.

### CNN details
* The CNN implements has been build using the technologies listed below.
So far, it is possible to classify the following categories of flowers: Tulip, Sunflower, Rose, dandelion, daisy.

#### Project assets
* Jupiter Notebook
* [Web app](webAppClassifier/README.md)
* [Mobile Application](recognition_app/README.md)
#### Technologies

<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white">
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">

###  Coding style and quality check and dependencies for code checks
* Coding style: Black
* Python Lint: Flake8, flake8-todos
* mypy (for english type checking)
* trim (to trim files)
* autopep8 (to automatically reformat a python file in according to pep8 directive)
* black (For code quality check purposes)
```
# format folder
black folder_name
# Remote all white spaces from project files
trim .
# Format file to improve syntax in according to flake8 (yes -> 2 times --aggressive)
autopep8 --in-place --aggressive --aggressive filename.py
```
