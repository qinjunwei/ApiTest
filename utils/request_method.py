# -*- coding:utf-8 -*-
import json
from time import sleep

import requests

from utils.logUtil import MyLog


class ApiRequest:

    def __to_dict(s: str):
        '''
        将json字符串转字典
        :param s:字符串
        :return: 字典
        '''
        return json.loads(s)

    def __to_str(self,dict: dict):
        '''
        字典转json字符串
        :param dict:
        :return: json字符串
        '''
        return json.dumps(dict)

    def __get(self,url,data=None,headers=None):
        if headers is not None:
            res = requests.get(url=url,data=data,headers=headers, verify= False).text
        else:
            res = requests.get(url=url,data=data, verify= False).text
        return res

    def __post(self,url,data=None,headers=None):
        if headers is not None:
            res = requests.post(url=url,data=data,headers=headers, verify= False).text
        else:
            res = requests.post(url=url,data=data, verify= False).text
        return res

    def __put(self, url, data= None, headers= None):
        if headers is not None:
            res = requests.put(url=url,data=data,headers=headers, verify= False).text
        else:
            res = requests.put(url=url,data=data, verify= False).text
        return res

    def request_main(self,method: str,url=None,data=None,headers=None):
        # 将字典转为json
        data = self.__to_str(data)
        res = ""
        if method.lower() == 'get':
            res = self.__get(url=url,data=data,headers=headers)
        elif method.lower() == 'post':
            res = self.__post(url=url,data=data,headers=headers)
        elif method.lower() == 'put':
            res = self.__put(url=url,data=data,headers=headers)
        else:
            MyLog.info("【暂无{}请求方法】".format(method))

        try:
            resDict = json.loads(res)
            return resDict
        except Exception as e:
            return res


if __name__ == "__main__":
    api = ApiRequest()

    d = {"data":{"records"}}