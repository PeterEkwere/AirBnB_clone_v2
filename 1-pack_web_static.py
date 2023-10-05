#!/usr/bin/python3
"""
    This script generates a .tgz archive from the web_static folder
    Author: Peter Ekwere
"""
from datetime import datetime
from fabric.api import local
import os


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
    local("mkdir versions")
    result = local(f"tar -czvf versions/{PATH} web_static")
    if result.succeeded:
        return PATH
    else:
        return None
