#!/usr/bin/python3
"""This is a script that generates a .tgz archive from the contents of the
   web_static folder.
"""
from datetime import datetime
from fabric.api import task, local


@task
def do_pack():
    """This is the function that does the main work."""
    try:
        N_time = datetime.now().strftime("%Y%m%d%H%M%S")

        local("mkdir -p versions")

        local("tar -cvzf versions/web_static_{}.tgz web_static".format(
              N_time))

        return "verions/web_static_{}.tgz".format(N_time)
    except Exception as e:
        return None
