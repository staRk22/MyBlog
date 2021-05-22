# My Blog Site

To Run the app

## Getting Started

* C:\code\MyBlog>set FLASK_APP=flaskblog.py

* flask run

* http://127.0.0.1:5000/ 

* set FLASK_DEBUG=1

### Prerequisites

* pip install flask

**Permissions**

Tickets to file with Support include:

**Machine Setup**

-   [Python 3.7.x](https://www.python.org/downloads/)
-   [pip 19.3.1](https://pip.pypa.io/en/stable/installing/) (or latest version for Python 3.7)
-   [Node.js + npm](https://nodejs.org/en/download/)
-   [ODC Driver 17 for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-2017)

**Clone Repository**

```sh
```

**Checkout Develop Branch**

This is the main development integration branch. Master is unused.

```sh
git checkout develop
```

**Install Packages**

```sh
pip install -r requirements.txt --user
npm ci
```

**Update Local Config Overrides**

Copy `serveroverride-example.cfg` into a new file called `serveroverride.cfg` and update any values with `override-me`.
This will override configuration settings in `serverbase.cfg` when running locally.
Ask a fellow developer for any tips on what this file should include.
NOTE: This file is specified in `.gitignore` and should NEVER be committed.

### Local Development

**Start Server**

```sh
# Windows
run_server
# macOS/Linux
./run_server.sh
```

**Run App**

-   Browse to http://localhost:9002/
-   Press CTRL+C to quit

**Building Local Docker Container**

To run docker container locally:

-   build docker container from Dockerfile `docker build --rm -t <user>/portal .`
-   to install database credentials uncomment `COPY serveroverride.cfg serveroverride.cfg` line in Dockerfile
-   run docker container on local machine `docker run --name portal -p 9003:9000 <user>/portal`

You may also create a shell script to launch your docker container for local testing. DO NOT commit this to the repo since you will need to pass your AWS keys as environment variables. An example for Mac is below:

`launch_container.sh`

```
#!/bin/bash
docker run --entrypoint "" -p9003:9000 -e AWS_ACCESS_KEY_ID='YOUR AWS KEY' -e AWS_SECRET_ACCESS_KEY='YOUR AWS SECRET KEY' -e DB_PORT=5432 -e DB_HOST=docker.for.mac.host.internal -it <user>/portal uwsgi $1
```

Remember to stop and clean up your local containers when you are finished.

To see if you have any containers running `docker ps -a`.

If containers are running:

-   `docker stop $(docker ps -a -q)`
-   `docker rm $(docker ps -a -q)`
-   `docker rmi $(docker images -a)`

**Generate Code**


```
npm run generate

# Answer prompts
# ? Your element tag name, please: <portal-my-tag-name>
# ? Your element class name, please: <PortalMyClassNameElement>
```

**Running tests**

See [TESTING.md](TESTING.md)

## Application Details

**Rules for Object table state**

-   Initially each table tab is sorted by 'Modified Date' descending.
-   Each table tab saves it's own changes to sort column and sort direction.
-   Changes are preserved when entering or exiting table tabs and when views within a client change.
-   Table tab state is preserved during and after search.
-   Table state is reset for all tabs when the client is changed.

**data_points Flexibility**

The `data_points` column provides teams quite a bit of flexibility. To support differences in data representation choices across apps and between bulk uploads and single object creation we are reducing the `data_points` array into a single object which also favors key access.

```javascript
const points = data_points.reduce((acc, curr) => {
    return { ...acc, ...curr };
}, {});
```

## Resources


