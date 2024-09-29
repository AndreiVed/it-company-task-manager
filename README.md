# IT Company Task Manager Project

Django project for managing tasks, workers, worker`s teams and projects in IT company

## Check it out!

[Task manager deployed to Render]("https://it-company-task-manager-dlqd.onrender.com")

## installation

Python3 must be already installed 

``` shel
git clone https://github.com/AndreiVed/it-company-task-manager/
cd it_company_task_manager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver #starts Django server
```
To enter the site first time use:
* login: user
* password: user12345

## Features

* Authentication functionality for Worker/User
* Worker can create, edit and delete tasks, mark tasks as completed (for this, there is a "mark as DONE" button on the task page).
* Each worker has his own position and can edit, create and delete positions.
* Workers can create new, edit and delete teams, also can add themselves to team.
* Teams can have several projects in the works.
* Tasks have types of tasks. Workers can create new, edit and delete task types.
* Tasks can be combined into projects. on the page with the list of tasks, all tasks are sorted by priority, 
and completed and failed tasks (whose deadline is less than the current time) are highlighted separately.
* Pagination is implemented for each list, except for the task list
* Powerful admin panel for advanced managing.

![DB_diagram](pictures%2FScreenshot%202024-09-27%20at%2014.38.19.png)
![login page](pictures%2FScreenshot%202024-09-26%20at%2012.05.02.png)
![index page](pictures%2FScreenshot%202024-09-26%20at%2012.05.13.png)
![worker detail page](pictures%2FScreenshot%202024-09-26%20at%2012.05.26.png)
![teams list page](pictures%2FScreenshot%202024-09-26%20at%2012.05.51.png)
![workers list page 1](pictures%2FScreenshot%202024-09-26%20at%2012.06.22.png)
![workers list page 2](pictures%2FScreenshot%202024-09-26%20at%2012.06.33.png)
![worker update page](pictures%2FScreenshot%202024-09-26%20at%2012.06.56.png)
![worker delete page](pictures%2FScreenshot%202024-09-26%20at%2012.07.04.png)
![positions list page](pictures%2FScreenshot%202024-09-26%20at%2012.06.45.png)
![projects list page](pictures%2FScreenshot%202024-09-26%20at%2012.08.28.png)
![projects create page](pictures%2FScreenshot%202024-09-26%20at%2012.07.51.png)
![project detail page](pictures%2FScreenshot%202024-09-26%20at%2012.08.06.png)
![task list page 1](pictures%2FScreenshot%202024-09-26%20at%2012.08.28.png)
![task list page 2](pictures%2FScreenshot%202024-09-26%20at%2012.08.37.png)
![task create page 1](pictures%2FScreenshot%202024-09-26%20at%2012.08.51.png)
![task create page 2](pictures%2FScreenshot%202024-09-26%20at%2012.08.59.png)
![task type list](pictures%2FScreenshot%202024-09-26%20at%2012.09.18.png)
