#!/usr/bin/python3
"""
The fabric script to delete outdated archives.
"""

import os
from fabric.api import env, local, run, cd

env.hosts = ['100.24.206.10', '54.167.152.64']


def do_clean(number=0):
    """
    To delete outdated archives.

    Args:
        number (int): Number of archives to keep.
                      If number is 0 or 1, keeps only the most recent archive.
                      If number is 2, keeps the most and second-most recent archives, etc.
    """
    number = max(1, int(number))

    #To delete local outdated archives
    local_archives = sorted(os.listdir("versions"), reverse=True)
    for archive in local_archives[number:]:
        local("rm -f versions/{}".format(archive))

    #To delete remote outdated archives
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr | grep 'web_static_'").split()
        for archive in remote_archives[number:]:
            run("rm -rf {}".format(archive))


if __name__ == "__main__":
    do_clean()
