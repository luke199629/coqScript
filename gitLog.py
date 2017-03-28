# -*- coding: utf-8 -*-
# @Author: Luke
# @Date:   2017-03-09 00:57:03
# @Last Modified by:   luke199629
# @Last Modified time: 2017-03-27 22:10:46
import git, os, shutil
import subprocess
import time

fileName = "newestLog.txt"
curtime = time.time()
command = "cd .. && cd UniMath && git log | tee "+fileName
print(subprocess.call([command], shell=True))
print(time.time() - curtime)

file = open("newestLog.txt")

commits = []
commitHist = open("commitHist.txt", "w")
for line in file:
    if line[:6] == "commit":
        commits.append(line[7:-1])
        commitHist.write(line[7:-1]+"\n")
file.close()
commitHist.close()
# print(commits)