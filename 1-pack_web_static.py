#!/usr/bin/env python3
"""module: 1-pack_web_static
"""
# Write a Fabric script that generates a .tgz archive from contents of
# the web_static folder of your AirBnB Clone repo, using the function do_pack.
#   Prototype: def do_pack():
#   All files in the folder web_static must be added to the final archive
#   All archives must be stored in the folder versions (your function should
#   create this folder if it doesn’t exist)
#   The name of the archive created must be
#       web_static_<year><month><day><hour><minute><second>.tgz
#   The function do_pack must return the archive path if the archive has been
#   correctly generated. Otherwise, it should return None
from fabric.api import local
from datetime import datetime
import os

def do_pack(c):
    """Generate a tar.gz file from the web_static folder.

    Returns:
        Archive path if archive is correctly generated, otherwise None.
    """
    time = datetime.now()
    archive_name = f"web_static_{time.strftime('%Y%m%d%H%M%S')}.tgz"
    local("mkdir -p versions")
    result = local("tar -czvf versions/{} web_static".format(archive_name), capture=True)
    if result.failed:
        return None
    return os.path.abspath(f"versions/{archive_name}")
