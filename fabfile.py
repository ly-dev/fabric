from fabric.api import *

PACKAGE_MANAGER_INSTALL = "apt-get install %s"
PACKAGE_MANAGER_UPDATE = "apt-get update"

def hello():
    run('echo "hello from `hostname`"')

def installPackages(packages):
    sudo(PACKAGE_MANAGER_UPDATE)
    for package in packages:
        sudo(PACKAGE_MANAGER_INSTALL % package)

def installApache2():
    installPackages(["apache2"])
