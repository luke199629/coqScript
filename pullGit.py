# -*- coding: utf-8 -*-
# @Author: Luke
# @Date:   2017-03-09 00:57:03
# @Last Modified by:   luke199629
# @Last Modified time: 2017-03-28 00:36:44
import git, os, shutil
import subprocess
import time
import commitObject


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
commitObjList = commitObject.constructFromFile("newestLog.txt")

# print(commitObjList[0].commitId)
# exit() # for experiment use
path = "https://github.com/UniMath/UniMath.git"

setup = "cd .. && cd UniMath && git remote set-url upstream "+path+" && git remote set-url origin https://github.com/luke199629/UniMath.git"
# print(subprocess.call([setup], shell=True))
subprocess.call([setup], shell=True)
times = []
for ctr in range(len(commitObjList)):
# for ctr in range(0):
    curtime = time.time()
    curObj = commitObjList[ctr]
    fileName = str(ctr) + ".txt"
    command = "cd .. && cp UniMath-build/* UniMath && cd UniMath && git checkout " + curObj.commitId + " && ./build.sh | tee "+"./../"+fileName+" && make clean"
    # command = "cd .. && cd UniMath && git checkout 76d062d && ./build.sh | tee "+fileName+" && make clean"
    # print(subprocess.call([command], shell=True))
    subprocess.call([command], shell=True)
    updateGit = "cd .. && cd UniMath && git add -A && git commit -m \""+ curObj.commitMessage +"\" && git push origin master"
    # print(subprocess.call([updateGit], shell =True))
    subprocess.call([updateGit], shell =True)
    # time.sleep(2)
    elapsed = time.time() - curtime
    times.append(elapsed)
    print(elapsed)
print(times)





