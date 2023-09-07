#!/usr/bin/python3


from datetime import datetime
from fabric.api import task, local


@task
def do_pack():
    try:
        N_time = datetime.now().strftime("%Y%m%d%H%M%S")

        local("mkdir -p versions")

        local(f"tar -cvzf versions/web_static_{N_time}.tgz /web_static")

        return f"verions/web_static_{N_time}.tgz"
    except Exception as e:
        return None
