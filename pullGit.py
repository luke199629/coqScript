# -*- coding: utf-8 -*-
# @Author: Luke
# @Date:   2017-03-09 00:57:03
# @Last Modified by:   luke199629
# @Last Modified time: 2017-03-16 01:32:32
import git, os, shutil
import subprocess
import time
DIR_NAME = "temp"
REMOTE_URL = "https://github.com/luke199629/cs241"
 
if os.path.isdir(DIR_NAME):
    shutil.rmtree(DIR_NAME)
 
os.mkdir(DIR_NAME)
 
repo = git.Repo.init(DIR_NAME)
origin = repo.create_remote('origin',REMOTE_URL)
origin.fetch()
origin.pull(origin.refs[0].remote_head)
 
print("---- DONE ----")
fileName = "76d062d.txt"

curtime = time.time()
command = "cd .. && cd UniMath && git checkout 76d062d && ./build.sh | tee "+fileName
print(subprocess.call([command], shell=True))
print(time.time() - curtime)