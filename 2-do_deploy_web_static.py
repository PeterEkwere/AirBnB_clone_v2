#!/usr/bin/python3
"""
    This script generates a .tgz archive from the web_static folder
    Author: Peter Ekwere
"""
from datetime import datetime
from fabric.api import env, local, run, put
import os

env.hosts = ["35.175.130.11"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_pack():
    """ This function handle the .tgz archiving
    """
    now = datetime.now()
    y = now.year
    m = now.month
    d = now.day
    h = now.hour
    m = now.minute
    s = now.second
    PATH = f"web_static_{y}{m:02}{d:02}{h:02}{m:02}{s:02}.tgz"
    local("mkdir -p versions")
    result = local(f"tar -czvf versions/{PATH} web_static")
    if result.succeeded:
        return PATH
    else:
        return None


def do_deploy(archive_path):
    """ This function distributes an archive to your webserver
    """
    if not os.path.exists(archive_path):
        print("Not Found")
        return False
    splits = archive_path.split("/")
    compressed_file = splits[1]
    uncompressed_file = compressed_file.split(".")[0]
    put(f"{archive_path}", "/tmp/")
    run(f"mkdir -p /data/web_static/releases/{uncompressed_file}/")
    tar_source = f"/tmp/{compressed_file}"
    tar_dest = f"/data/web_static/releases/{uncompressed_file}"
    run(f"sudo tar -xzf {tar_source} -C {tar_dest}")
    run(f"sudo mv -f {tar_dest}/web_static/* {tar_dest}/")
    run("sudo rm -rf /data/web_static/{uncompressed_file}/web_static")
    run(f"sudo rm /tmp/{compressed_file}")
    run("sudo rm -rf /data/web_static/current")
    run(f"sudo ln -s {tar_dest}  /data/web_static/current")
    return True
