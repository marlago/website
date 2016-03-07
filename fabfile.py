from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
# in Python 2.x this is SocketServer
import socketserver

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
env.theme_path = 'themes'
DEPLOY_PATH = env.deploy_path
THEME_PATH = env.theme_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
GH_USER_PAGE_REPO = "https://github.com/sollago/sollago.github.io.git"

# Port for `serve`
PORT = 8000


def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)


def build(config="pelicanconf"):
    """Build local version of site"""
    local('pelican -s {0}.py'.format(config))
    collectstatic()


def rebuild(config="pelicanconf"):
    """`clean` then `build`"""
    clean()
    build(config)


def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')
    collectstatic()


def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()


def reserve():
    """`build`, then `serve`"""
    build()
    serve()


def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')


def cf_upload():
    """Publish to Rackspace Cloud Files"""
    rebuild()
    with lcd(DEPLOY_PATH):
        local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
              '-U {cloudfiles_username} '
              '-K {cloudfiles_api_key} '
              'upload -c {cloudfiles_container} .'.format(**env))


@hosts(production)
def publish():
    """Publish to production via rsync"""
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )


def ghpages():
    """Publish to GitHub Pages"""
    rebuild(config="publishconf")
    local("ghp-import {0}".format(DEPLOY_PATH))
    local("git push {0} gh-pages:master".format(GH_USER_PAGE_REPO))

# Added to work with twenty html5up theme


def collectstatic():
    if os.path.isdir(DEPLOY_PATH):
        local('mkdir -p {deploy_path}/css/ {deploy_path}/js/ {deploy_path}/fonts/ {deploy_path}/images/'.format(**env))
        local('cp -rf {theme_path}/twenty/static/css/* {deploy_path}/css/'.format(**env))
        local('cp -rf {theme_path}/twenty/static/js/* {deploy_path}/js/'.format(**env))
        local('cp -rf {theme_path}/twenty/static/fonts/* {deploy_path}/fonts/'.format(**env))
        local('cp -rf {theme_path}/twenty/static/images/* {deploy_path}/images/'.format(**env))
