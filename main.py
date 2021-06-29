from github import Github
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, make_response
import logging
import datetime



#config vars
today = str(datetime.date.today())
token = ''
user = 'jewbott'
period = 300
port = 8080

#default anonnymous github url connection
if token == '':
    git = Github()
# you can use github token or custom url
else:
    git = Github(token)

#systemvars
lastCheck = ''
gists = {}
returned = {}

#basic logger
logging.basicConfig(level=logging.INFO, filemode='a', format='%(asctime)s: %(levelname)s - %(message)s')

#function to check gists for specified user
def getGists():
        if lastCheck == '':
            logging.info('Gists were not checked yet')
        else:
            logging.info('Last time gists were checked:' + str(lastCheck))

        global gists
        for gist in git.get_user(user).get_gists():
                desc = gist.description
                id = gist.id
                datecreated = (gist.created_at)
                dateupdated = (gist.updated_at)
                gists[id] = [user, desc, id, datecreated, dateupdated]
        print(gists)

#function to compare gist update/create comparing to the last visit by user
def compareGist():
    currenttime = datetime.datetime.utcnow()
    global returned
    global lastCheck
    for key, value in gists.items():

        user = value[0]
        desc = value[1]
        id = value[2]
        created = value[3]
        updated = value[4]

        if lastCheck == '':
            status = "Initial Check"
            logging.info('Initial check for gist:' + str(id))
        elif created >= lastCheck:
            status = "New gist"
            logging.info('New gist was found for user:' + str(desc))
        elif updated >= lastCheck:
            status = "Gist Updated"
            logging.info('Gist was updated:' + str(desc))
        else:
            status = "Not modified"
            logging.info('Gist was not updated:' + str(desc))
        returned[key] = [{'user':user, 'description': desc, 'gistid':id, 'datecreated': created,'dateupdated': updated,'status': status}]

    lastCheck = currenttime

    return returned

#initial request to get gist details
getGists()
logging.info('first API call')
#background scheduler to run and update dictionary of gistis in specified intervals of time
sched = BackgroundScheduler(daemon=True)
sched.add_job(getGists, 'interval', seconds=period)
sched.start()

#basic flask framework
app = Flask(__name__)

#endpoint for plain/text result of json
@app.route("/")
def check():
    chk = compareGist()
    response = make_response(chk)
    response.mimetype = "text/plain"
    logging.info('Gist was checked at:' + str(lastCheck))
    return response


if __name__ == "__main__":
    app.run(port=port)
