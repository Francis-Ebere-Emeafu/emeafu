# Setting Up Remote Automation
from __future__ import with_statement

import os
from fabric.contrib.files import sed
from fabric.api import cd, env, local, run, sudo
from fabric.colors import green, red
from fabric import colors
from fabric.context_managers import prefix
from contextlib import contextmanager as _contextmanager


env.user = "freemandigit"
env.password = "pass.p1985"
env.hosts = ["freemandigit@162.243.173.228"]
env.directory = "/home/freemandigit/apps/adnews"
env.activate = "source /home/freemandigit/envs/adnews/bin/activate"

def local_uname():
    local('uname -a')


def commit(message='updates'):
    # Add comment using quotes to format them as strings
    # fab commit 
    try:
        local("git add .")
        print('----------')
        print(message)
        print('---------- \n')
        local("git commit -m '{}'".format(message))
        local("git push")
        print(colors.green('Changes committed and pushed to github remote server!', bold=False))
    except:
        local("git status")
        print(colors.yellow('No changes to commit on git local repo, all new changes already committed!', bold=False))
        

def push():
    # local function to push git changes to github remote server
    local("git add -p && git commit")
    local("git push")
    print(colors.blue('Done pushing changest to the server, no new changes to push!', bold=False))


@_contextmanager
def virtualenv():
    # local("ssh freemandigit@162.243.173.228")
    with cd(env.directory):
        with prefix(env.activate):
            yield

def restart_server():
    # run("sudo systemctl restart adnews --noinput")
    sudo("systemctl restart adnews")


def deploy():
    local("git push")
    remote_dir = "/home/freemandigit/apps/adnews"
    # with cd(remote_dir):
    with virtualenv():
        run("git pull")
        print("Hello we are here in the run folder")
        # run("python3.6 manage.py migrate")
        run("python manage.py collectstatic --noinput")
        restart_server()