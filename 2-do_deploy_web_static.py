#!/usr/bin/python3
"""This is a script that distributes an archive to your web servers."""
from fabric.api import run, put, env
from os import path

env.hosts = ['52.91.126.140', '54.160.83.162']


def do_deploy(archive_path):
    """This is the main function that does the distribution."""
    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        archive_noext = archive_path[9:-4]
        ver = archive_path.split('/')
        name = ver[1]
        new_fold = "/data/web_static/releases/{}/".format(archive_noext)
        run("mkdir -p {}".format(new_fold))
        run("tar -xzf /tmp/{} -C {}".format(name, new_fold))
        run("rm /tmp/{}".format(name))
        run("mv {}/web_static/* {}".format(new_fold, new_fold))
        run("rm -rf {}/web_static".format(new_fold))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_fold))
    except Exception as e:
        return False

    return True
