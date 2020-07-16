#-*- coding:utf-8 -*-
"""
    将脚本放置项目根目录下
"""

from git import Repo
import os
import time

dirfile =  os.path.abspath('')
repo = Repo(dirfile)

for i in range(1000):
    time.sleep(1)
    g = repo.git
    try:
        g.add("--all")
        g.commit('-m auto update')
        g.push()
    except:
        try:
            g.pull('https://github.com/99kies/autoupdate')
            g.push()
        except:
            print('Already Update')
    print('Successful push!')
