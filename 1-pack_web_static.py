#!/usr/bin/python3
"""
    This script generates a .tgz archive from the web_static folder
    Author: Peter Ekwere
"""
from datetime import datetime
from fabric.api import local, task
import os


@task
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
    tarFileName = f"web_static_{y}{m:02}{d:02}{h:02}{m:02}{s:02}.tgz"
    local('mkdir versions')
    local(f'tar -cvf versions/{tarFileName} web_static')
    PATH = os.path.abspath(f'versions/{tarFileName}')
    if os.path.exists(PATH):
        return PATH
    else:
        return None


if __name__ == "__main__":
    """ Trigger if called directly
    """
    do_pack()
