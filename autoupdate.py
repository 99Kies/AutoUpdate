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
    time.sleep(2)
    g = repo.git
    g.add("--all")
    g.commit('-m auto update')
    try:
        g.push()
    except:
        g.pull()
        g.push()
    print('Successful push!')
