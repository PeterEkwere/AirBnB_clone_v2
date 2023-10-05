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
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    tarFileName = f"web_static_{year}{month: 02}{day: 02}
    {hour: 02}{minute: 02}{second: 02}.tgz"
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
