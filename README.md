# My Blog Site

To Run the app

**Milestones for parity with Omni v1.0**

-   User can sign in
-   Omni can list user's clients
-   User can select a client (update route)
-   Omni can list user's tools
-   User can select a tool (update route)
-   Omni can render tool contents (iframe, sso)

## Getting Started

* C:\code\MyBlog>set FLASK_APP=flaskblog.py

* flask run

* http://127.0.0.1:5000/ 

* set FLASK_DEBUG=1

### Prerequisites

* pip install flask

**Permissions**

Tickets to file with Support include:

-   READ/WRITE access to annalect-annalect-omni s3 bucket
-   READ access to AWS SSM parameters /dev/omni/images/secrets/save and /dev/portal/cache/profile/timeout
-   READ access to the /dev/omni2/api-key-jwt-private and /dev/omni2/api-key-jwt-public in AWS Secrets Manager
-   READ access to annalect_jwt, omni_campaign, omni-ui, and pylect-infra bitbucket repositories

**Machine Setup**

-   [Python 3.7.x](https://www.python.org/downloads/)
-   [pip 19.3.1](https://pip.pypa.io/en/stable/installing/) (or latest version for Python 3.7)
-   [Node.js + npm](https://nodejs.org/en/download/)
-   [OpenVPN](https://annalect.atlassian.net/wiki/spaces/ADEV/pages/695468041/Onboarding+Guide?preview=/695468041/699170859/OpenVPN-HowTO.pdf) (for AWS VPC access)
-   [ODC Driver 17 for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-2017)

**Clone Repository**

```sh
git clone git@bitbucket.org:annalect/omni_portal.git
cd omni_portal
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

-   Start OpenVPN client, connect to ovpn.annalect.com
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

Generate a new OmniElement component connected to Redux store.

```
npm run generate

# Answer prompts
# ? Your element tag name, please: <portal-my-tag-name>
# ? Your element class name, please: <PortalMyClassNameElement>
```

**Running tests**

See [TESTING.md](TESTING.md)

## Application Details

**Handling unpermissioned Omni Object content**

The application has three user scenarios around Omni Objects:

1. Permissoned to all Omni Object applications

-   Has My Workspace nav link
-   Has Audiences nav link
-   Has Campaigns nav link
-   Has Create button
-   Has Recents tile
-   Has all tabs in Omni Objects table

2. Permissioned to at least one but not all Omni Object applications

-   Has My Workspace nav link
-   Has Audiences nav link if permissioned to AE
-   Has Campaigns nav link
-   Has Create button functionality for Campaigns and any other permissioned applications
-   Has Recents tile
-   Has tabs in table if permissioned to application

3. Lacking permission to any Omni Object applications

-   Has My Workspace nav link
-   Does not have Audiences nav link
-   Does not have Campaigns nav link
-   Does not have Create button
-   Does not have Recents tile
-   Does not have Omni Objects table

One outstanding question: Can you have a Campaign if you cannot consume/create Omni Objects?

**Rules for Omni Object table state**

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

[Good First Issues](https://annalect.atlassian.net/browse/OMN-1016?jql=project%20%3D%20OMN%20AND%20resolution%20%3D%20Unresolved%20AND%20labels%20%3D%20good-first-issue%20ORDER%20BY%20priority%20DESC%2C%20updated%20DESC)

