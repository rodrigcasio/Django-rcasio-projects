# Django Online Courses project

## The purpose of adding this project:

Learn `admin site` provided by Django to manage models.
  - Customize admin site for specific models like `Course` and `Instructor`.
  - Create Inline classes for adding related objects on the same page
    - (`StackedInline`) to manage `Lesson` objects directly within the `Course` management page.
  - Implement a custom registration process for different user roles (`Instructors` and `Learners`).

In this project it is necesary to create a `Superuser` account to manage the app
This project is linked to a created `PostgreSQL` database within my local machine to visualize and manage the registrations of the Course and Instructor sections within the `ADMINSITE` section when running the app.

## Dockerizaton & Portability

This poject is containerized for easy deployment across any enviroment.
- Image: `rodrigocasio/online-course-admin:v1`
it has dynamic config which uses the `DOCKER_RUNNING` enviroment variable to toggle between `localhost` and the Docker host IP (`172.17.0.1`) for database connectivity

# How to run

1. Ensure PostgreSQL is running on your host machine
2. Run the container:   (currently no working but succesfully created image and pushed in my Docker Hub)
  (`docker run -p 8000:8000 rodrigocasio/online-course-admin:v1`)
3. Access the admin panel at `http://localhost:8000/admin`

# HOW TO RUN localhost with database 
install all the packages within a virtual enviroment:
(local PostgreSQL db need to be active)
`python manage.py runserver`

@rodrigcasio

