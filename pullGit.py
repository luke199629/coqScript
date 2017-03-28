# -*- coding: utf-8 -*-
# @Author: Luke
# @Date:   2017-03-09 00:57:03
# @Last Modified by:   luke199629
# @Last Modified time: 2017-03-27 15:12:40
import git, os, shutil
import subprocess
import time
# DIR_NAME = "temp"
# REMOTE_URL = "https://github.com/luke199629/cs241"
 
# if os.path.isdir(DIR_NAME):
#     shutil.rmtree(DIR_NAME)
 
# os.mkdir(DIR_NAME)
 
# repo = git.Repo.init(DIR_NAME)
# origin = repo.create_remote('origin',REMOTE_URL)
# origin.fetch()
# origin.pull(origin.refs[0].remote_head)
 
# print("---- DONE ----")

path = "https://github.com/UniMath/UniMath.git"
fileName = "76d062d.txt"
setup = "cd .. && cd UniMath && git remote set-url upstream "+path+" && git remote set-url origin https://github.com/luke199629/UniMath.git"
print(subprocess.call([setup], shell=True))
curtime = time.time()
command = "cd .. && cd UniMath && git checkout 76d062d && ./build.sh | tee "+fileName
# command = "cd .. && cd UniMath && git checkout 76d062d && ./build.sh | tee "+fileName+" && make clean"
print(subprocess.call([command], shell=True))
message = "Merge pull request #287 from benediktahrens/yoneda\nthe isomorphism given by yoneda lemma is natural"
updateGit = "cd .. && cd UniMath && git add -A && git commit -m \""+message+"\" && git push origin master"
print(subprocess.call([updateGit], shell =True))
print(time.time() - curtime)