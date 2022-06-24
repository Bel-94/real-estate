<h1>Acuteleaf~Homes</h1>

<h2>By Belinda Ntinyari<h2>

<p>This is an app that helps people to search for properties/listings to buy. They can also contact the realtor and make inquiries.</p>

## Screenshots 
###### Home page
<img src="static/img/Screenshot from 2022-06-24 15-30-00.png">

###### single listing and inquiry form
<img src="static/img/Screenshot from 2022-06-24 15-30-00.png">

###### User Dashboard
<img src="static/img/Screenshot from 2022-06-24 15-32-53.png">


<h3>User Story</h3>
<p>The user is able to</p>

<ul>
    <li>Register and login.</li>
    <li>View all  the houses listed.</li>
    <li>Search for a listing. </li>
    <li>Make an inquiry about a specific listing. </li>
    <li>See more information on the listing and the realtor.</li>
    <li>Manage their account from the dashboard</li>
</ul>

<h3>Technologies Used</h3>
<ul>
    <li>Python3.8 & Django</li>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
    <li>Heroku</li>
</ul>

<h3>Requirements for Installation</h3>
<ul>
    <li>
    Either a computer,phone,tablet or an Ipad or any other tech-gudget. </li>
    <li>An access to the Internet.</li>
</ul>

<h3>Installation/Setup instructions</h3>
<p>The application requires the following installations to operate</p>
<ul>
    <li>pip</li>
    <li>gunicorn</li>
    <li>django</li>
    <li>Postgresql</li>

</ul>

## Setup and Installation  
To get the project follow these steps:

##### Cloning the repository:  
 ```bash 
https://github.com/ThiraTheNerd/neighbourhood.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd neighbourhood 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
``` 
 ##### Setup Database
 Create a .env file and fill in the configurations for your database and application.
 python manage.py makemigrations hoodapp
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

<h3>Known Bugs</h3>
<p>There are no known bugs currently but pull requests are allowed incase you spot a bug.</p>

<h3>License</h3>
<p>Copyright (c) Belinda Ntinyari - MIT License</p>

<h3>Authors Info</h3>
<ul>
    <li>LinkedIn: <a href="https://www.linkedin.com/in/belinda-ntinyari-3843a81b5/">Belinda Ntinyari</a>
    <li>Email address: <a href="ntinyaribelinda@gmail.com">Belinda Ntinyari</a>
</ul>
