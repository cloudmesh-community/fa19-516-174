FROM python:3

WORKDIR /usr/src/app

#
# thsi sis wrong, it typically needs to be installed with pip install, while you
# use cloudmesh sys generayte to generate the framework, this is not just about
# creating a random python prg, thsi is about the integration into cloudmesh to
# eleverage 1000o of thausends of lines of clever python code.
#
COPY requirements.txt ./

#
# this is even more worng as you either mount this in volumes and do not do a
# copy or use git clone to create your own local copy so that on entry yo ucan
# do a git pull or even when execing it to get the nnewest code.
#

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#
# pull missning here
#
CMD [ "python", "server.py" ]