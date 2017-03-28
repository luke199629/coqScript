# -*- coding: utf-8 -*-
# @Author: luke199629
# @Date:   2017-03-27 22:18:49
# @Last Modified by:   luke199629
# @Last Modified time: 2017-03-27 23:20:38
class commitObject:

    def __init__(self, commitId, mergeId, author, date, commitMessage):
        self.commitId = commitId
        self.mergeId = mergeId
        self.author = author
        self.date = date
        self.commitMessage = commitMessage

def constructFromFile(inputFile):
    startLineNumbers = []
    logs = []
    result = []
    file = open(inputFile)
    ctr = 0
    for line in file:
        if line[:6] == "commit":
            startLineNumbers.append(ctr)
        logs.append(line)
        ctr += 1
    file.close()
    for i in range(len(startLineNumbers) - 1):
        block = []
        if i + 1 == len(startLineNumbers) - 1:
            block = logs[startLineNumbers[i]:]
        else:
            block = logs[startLineNumbers[i]:startLineNumbers[i+1]]
        commitId = ""
        mergeId = ""
        author = ""
        date = ""
        commitMessage = ""
        for line in block:
            if line[:6] == "commit":
                commitId = line[7:-1]
            elif line[:5] == "Merge":
                mergeId = line[7:-1]
            elif line[:6] == "Author":
                author = line[8:-1]
            elif line[:4] == "Date":
                date = line[8:-1]
            else:
                commitMessage += line
        commitMessage = commitMessage[:-1]
        commitObj = commitObject(commitId, mergeId, author, date, commitMessage)
        result.append(commitObj)
        result.reverse()
    return result


            
