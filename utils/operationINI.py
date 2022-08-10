
import configparser

from utils.logUtil import MyLog

userINI = r"E:\InterTest\config\config.ini"

def __getConfigparser(file):
    conf = configparser.ConfigParser()
    conf.read(file, encoding= "utf-8")
    return conf

def getData(option, section= "user", filePath= userINI):
    con = __getConfigparser(filePath)
    if con.has_option(section, option):
        userData = con.get(section= section, option= option)
    else:
        userData = "文件中无对应key---{}".format(option)
    return userData

def setData(value, option, section= "user", filePath= userINI):
    con = __getConfigparser(filePath)
    try:
        con.set(section=section,option=option,value=value)
        con.write(open(filePath,"r+",encoding="utf-8"))
    except Exception as e:
        MyLog.error("setData --- {}".format(e))

if __name__ == "__main__":
    file = r"E:\InterTest\config\email.ini"
    print(getData("id"))
    print(getData(option= "phone", section= "user"))
    print(getData("token"))
    print(getData(option= "host", section= "email", filePath= file))