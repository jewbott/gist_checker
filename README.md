## GitHub Gist Checking
This web app is based on following solutions:

- [Flask](https://github.com/pallets/flask)
- [APScheduler](https://pypi.org/project/APScheduler/)
- [PyGithub](https://pypi.org/project/PyGithub/)


More information about GitHub API:
https://docs.github.com/en/rest

## Requirements assumptions
Asume we have users/customers who share their bits of code/configurations files as gists using GitHub.

App should be able to fetch status of these gists periodicaly and provide results via web endpoint. 

Status of the gist should change based on the last time when gists were checked via endpoint. 

Result will be in json/text format and will include all gists based on following format:
```json
{GistID:
	{username,
	descriptionOfGist,
	gistID,
	creationDate,
	updateDate,
	Status}
}
```
## Files
There are 3 main files for the application

**main.py** - contains the code and basic congig

**requirements.txt** - contains required modules and packages that GCP will automaticaly install

**app.yaml** - settings for google app engine server

## App Configuration
Main.py has configuraiton variables that can be changed to suit needs:

**token** - can provide github access token for access to non public gists

**user** - provide github user for checking his/her gists

**period** - how often github should check for updates (in seconds)

**port** - port where app is running


## App Installation

Clone app from repository
```powershell
git clone https://github.com/jewbott/gist_checker.git
```
Apply any changes to main.py for cusom user/pariod of checking

## App Deployment to Google Cloud Platform
Sign up for free account https://console.cloud.google.com/ 

Install GCLOUD SDK https://cloud.google.com/sdk/docs/install

Navigate to the dashboard view, where you’ll see a toolbar.
https://console.cloud.google.com/home/dashboard

Find the NEW PROJECT button, click it and create a new project. 

Copy the project ID that you will see here that should look like "your-app-1221231"

In the end project url should look like http://your-application-name.appspot.com

After project was created, select it by clicking SELECT PROJECT button.

From here, you want to switch to the dashboard of Google App Engine. 

Click the menu button on the top left, scrol down to select App Engine in the first list, then selecting Dashboard on the top of the next pop-up list.

Click GETTING STARTED button and configure language of project (PYTHON)

Navigate to project folder and initialize Google Cloud SDK by running 
```powershell
$ gcloud auth login
```

Configure project using project ID that you copied during the creation of project in GCP console
```powershell
$ gcloud config set project PROJECT_ID
```
After that you can run the deployment:

```powershell
$ gcloud app deploy
```

After deployment, you can open your app in browser by running

```powershell
$ gcloud app browse
```
Or open the project URL http://your-application-name.appspot.com:YOUR PORT NUMBER

==============================================================

