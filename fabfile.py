#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fabfile.py
import os, re
from datetime import datetime

# 导入Fabric API:
from fabric.api import *

# 服务器登录用户名:
env.user = 'root'
# sudo用户为root:
env.sudo_user = 'root'
# 服务器地址，可以有多个，依次部署:
env.hosts = ['115.28.189.125']

# 服务器MySQL用户名和口令:
db_user = 'root'
db_password = '******'

_TAR_FILE = 'dist-bookeq.tar.gz'

def build():
    includes = ['bookeq','*.*']
    excludes = ['test', '*.pyc', '*.pyo']
    local('rm -f dist/%s' % _TAR_FILE)
    #with lcd(os.path.join(os.path.abspath('.'), 'www')):
    cmd = ['tar', '--dereference', '-czvf', 'dist/%s' % _TAR_FILE]
    cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
    cmd.extend(includes)
    local(' '.join(cmd))

_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE
_REMOTE_BASE_DIR = '/data/wwwroot/book.chenxf.org'

def deploy():
    newdir = 'www-%s' % datetime.now().strftime('%y-%m-%d_%H.%M.%S')
    # 删除已有的tar文件:
    run('rm -f %s' % _REMOTE_TMP_TAR)
    # 上传新的tar文件:
    put('dist/%s' % _TAR_FILE, _REMOTE_TMP_TAR)
    # 创建新目录:
    with cd(_REMOTE_BASE_DIR):
        sudo('tar -xzvf %s' % _REMOTE_TMP_TAR)
    # 重启Python服务和nginx服务器:
    with settings(warn_only=True):
        run('supervisorctl stop bookeq')
        run('supervisorctl start bookeq')