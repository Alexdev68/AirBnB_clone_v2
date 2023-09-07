#!/usr/bin/python3


from datetime import datetime
from fabric.api import task, local


@task
def do_pack():
    try:
        N_time = datetime.now().strftime("%Y%m%d%H%M%S")

        local("mkdir -p versions")

        local("tar -cvzf versions/web_static_{}.tgz web_static".format(
              N_time))

        return "verions/web_static_{}.tgz".format(N_time)
    except Exception as e:
        return None
