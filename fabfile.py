from fabric.api import *

def hello():
    run('echo "hello from `hostname`"')
