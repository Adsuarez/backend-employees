---
__Disclaimer:__ the project is almost complete, right now is work CRUD for employees. Is pending create a docker for server and integrate to take a microservice.

# DOCKER configuration for PostgreSQL:

## commands for windows

    C:\Users\Usuario>docker pull postgres

    C:\Users\Usuario>docker run --name some-postgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=password -e POSTGRES_DB=cobrando_db -p 5432:5432 -d postgres
 
    C:\Users\Usuario>docker exec -it some-postgres bash

    root@eff69ea6b67c:/# psql -U admin --db cobrando_db --password

    cobrando_db=#

# Get sarted:
    1. Open a terminal in backend-empleados folder
    2. Create a virtual environment with the next command: python -m venv virt
    3. Activate virtual environment with the next command: source virt/Scripts/activate
    4. Install all dependences needed for the project with the next command: pip install -r requirements.txt
    5. Access folder crud with the next command: cd crud
    5. Run server on port 1234 with the next command: python manage.py runserver 1234

# make CRUD with Rest Client
    Note: Rest Client is like a Postman, but is a plugging embedded for Visual Studio Code, and you can download here: https://marketplace.visualstudio.com/items?itemName=humao.rest-client 

    ## How i can make CRUD?
    It's very simply, you can open "requests" folder in the project, and there are some files with ".rest" extension. open each one and click on the link "Send Request" that is above the first line. That's all, look the response of each request.
