# Submission

## Design choices

 - Lightweight database (**sqlite3**) is used since the task primarily requires the insertion and update of only the company name.
 - The backend of the application uses **Django** and **Django Rest Framework** as it allows efficient application scaling, the ability to work with ORMs & REST APIs and also contains a readily available admin dashboard.
  - **VueJS** is used as frontend framework as it has rapid web-application development capability.
 - **Bulma** is used the CSS framework as it provides more flexibility for customization and responsiveness.
 - **Nginx** is used as the deployment server.
 - The admin is allowed to either insert or update the company name through the admin dashboard page such that there is a version control on all the previous company names recorded with a `datetime` field.
 - The `CompanyName` model in the backend has `name`, `created_at` and `updated_at` fields, such that the **GET** request returns only the last updated record based on date/time.

GET API:
```
http://localhost:8000/api/companyname/
```

Sample Response:
```
{
  "id": 2,
  "name": "The Lab",
  "created_at": "2023-01-27T05:43:05.013602Z",
  "updated_at": "2023-01-28T00:33:46.731251Z"
}
```


## Docker
 - I prefer to use Docker for developing web applications due to its concept of containerization of applications which provides more flexiblity to scale up or down the number of containers based on the traffic load of a website.
 - Additionally, docker commands are easy-to-read and provides the ability to test different configurations and environments right away. 
 - I have used docker in cross-functional teams to package and share applications in a very organized manner. It allows running the application developed on my system to another developer's system with few docker commands and skips the numerous library installations and version conflicts.
 - Since, I have only worked on medium-scale projects with Docker, I personally cannot think of the things that I don't like about Docker.

## How To Run

 - Clone the project
    ```
    git clone https://gitlab.com/thelabnyc-hiring/backend-test-oyesh-singh.git
    ```

 - Install the [docker](https://docs.docker.com/engine/install/) if not available in your system.

### Development version

 - Build the project using docker compose
    ```
    cd backend-test-oyesh-singh/thelab
    sudo docker compose -f docker-compose.dev.yml up --build
    ```

The development server should be up and running at [http://localhost:8080/](http://localhost:8080/)

 - In order to access the admin dashboard, first you need to create a superuser. 
   - Run `sudo docker ps` in another terminal
   - Get the container ID of docker named **thelab_backend**
   - Run `sudo docker exec -it <container ID of thelab_backend> /bin/bash`
   - Run `python manage.py createsuperuser`
   - Follow the instructions from Django

 - Once the superuser is created, go to the admin dashboard at [http://localhost:8000/admin](http://localhost:8000/admin) and login with the newly created superuser.
 - Now, you can add or change the **Company Name**
 - Refresh/reload the web application that is running on development server and you should see the recently updated company name on the Home page.