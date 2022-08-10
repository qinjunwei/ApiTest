# -*- coding:utf-8 -*-
import os


def dirPath(dirName):
    basePath = os.path.dirname(os.path.dirname(__file__))
    dirPath = os.path.abspath(os.path.join(basePath, dirName))
    return dirPath

def filePath(dirName, fileName):
    filePath = os.path.abspath(os.path.join(dirPath(dirName= dirName), fileName))
    return filePath

if __name__ == "__main__":
    print(dirPath("tests"))
    print(filePath("config", "config.ini"))