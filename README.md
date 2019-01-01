# Training and Placement - NITC

## Local Setup
I would recommend creating a venv using conda
> git  clone https://github.com/gottacodeemall/tnp_nitc
> pip install -r requirements

### Setting up the Database
> python manage.py makemigrations
> python manage.py makemigrations aboutus
> python manage.py makemigrations contactus
> python manage.py makemigrations landing
>python manage.py makemigrations recruiters
>python manage.py makemigrations students
>python manage.py migrate

### Creating a superuser(admin)
> python manage.py  createsuperuser

### Run the server
> python manage.py runserver

## Handling the Data from Django Admin Console
**If the name on the django-admin console is Singleton. Do not create Multiple instances.**

Navigate to 127.0.0.1:8000/admin

**Update the content by looking at the default values.txt file.**

### Explanation about Recruiter Section

For past recuiters add each company individually to Visited companies
**Why us Section**
Html content of whyus

**Past Recruiters**
Each company is  a single entity

**Statistics section**
Consists of stats_table and chart_data and statistics file uploads.

In chart data when you are inputting data make sure to validate your data through json validator

**Policy and Procedure**
Consists of Policy html, Procedure Steps and Policy File Uploads

 ### Explanation about Contact Us Section
In contact us a few quick contacts will be displayed.
These can be selected by selecting display_in_contactus in People section.

### Info that cannot be changed
Information in the footer cannot be altered.

