# pyramid-react-template
A starting off point for a web application that uses Pyramid in the back-end and React in the frontend

- [Setting up your environment](#setting-up-your-environment)
- [Using the demo application](#using-the-demo-application)

# Setting up your environment
## With Docker
Install the Docker Engine https://docs.docker.com/install/

Create the docker network
```
docker network create webapp
```

In the project root, start the docker containers:
```
docker-compose up
```

### Database
Using your MySQL client tool of choice, run the sequel statements in `backend/SCHEMA.sql` against the MySQL instance running in the database container.

Example using the mysql cli client:
```
mysql -h 0.0.0.0 -u root -p < backend/SCHEMA.sql
Enter password: 
```
The password is `example` and is configured in the `backend/docker-compose.yml` file.

### Troubleshooting
#### "exec: \"./startup.sh\": permission denied"
Add execute permissions to the startup.sh file
```
chmod +x backend/startup.sh
chmod +x frontend/startup.sh
```

## Without Docker
### Backend
#### Requirements
Install python 3.7 https://www.python.org/downloads/

Install virtualenv:
- On Mac/Ubuntu
```
pip3 install virtualenv
```
- On Windows
```
pip install virtualenv
```
#### Setup a virtual environment
In the project root, create a python virtual environment:
```bash
virtualenv -p python3.7 pyenv
```

Activate the virtual environment:
- On Mac/Ubuntu
```
source pyenv/bin/activate
```
- On Windows
```
pyenv\Scripts\activate
```

Install python dependencies:
```
cd backend
pip install -e .
cd ..
```

#### Run the server
```
pserve backend/development.ini --reload
```

#### Database
Update the connection values in `backend/development.ini` to point to your external MySQL instance.

Run the sequel statements in `backend/SCHEMA.sql` against the MySQL instance.

### Frontend
#### Requirements
Install Node.js https://nodejs.org/en/download/

#### Install dependencies
```
cd frontend
npm install
```

#### Run the app
```
cd frontend # If you're not already in /frontend
npm start
```

# Using the demo Application
## MySQL (Database)
Network:
```
External
host: localhost
port: 3306
username: root
password: example

Docker Network
host: database
port: 3306
username: root
password: example
```

## Pyramid (Backend API)
Network:
```
External
host: localhost
port: 7777

Docker Network
host: pyramid
port: 7777
```

Endpoints:
```
GET    /api/v1/songs  # Returns a list of song objects
POST   /api/v1/songs  # Creates a song object
GET    /api/v1/songs/:id  # Returns a song object
PUT    /api/v1/songs/:id  # Replaces a song object
DELETE /api/v1/songs/:id  # Deletes a song object
```

Song Model:
```
{
    "id": integer,
    "name": string,
    "artist": string,
    "genre": string,
    "date_created": string
}
```

## Node (Frontend Application)
Network:
```
External
host: localhost
port: 3000

Docker Network
host: node
port: 3000
```

Endpoints:
```
/          # List of songs
/edit      # Add a song
/edit/:id  # Update a song
```
