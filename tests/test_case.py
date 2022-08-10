# -*- coding:utf-8 -*-
import json
from time import sleep

import pytest

from utils.request_method import ApiRequest
from utils import operationINI as oi,randomData as rd
from utils.logUtil import MyLog
from utils.operationExcel import OperationExcel,ExcelVarles

api = ApiRequest()

cases = OperationExcel().getExcelDatas("data","接口测试用例.xls")

@pytest.mark.parametrize('data',cases)
def test_api(data):

    parames_dict = {}
    headers_dict = {}
    # 重新设置请求头信息
    headers = data[ExcelVarles.case_headers]
    if len(headers) > 0:
        headers_dict: dict = json.loads(headers)
        if headers_dict.get("Authorization") == "${token}":
            headers_dict["Authorization"] = oi.getData("token")
        else:
            # TODO:检查用例中请求头
            pass

    # 拼接参数
    parames = data[ExcelVarles.case_data]
    if len(parames) > 0 and "{" in parames:
        parames_dict: dict = json.loads(parames)
        if parames_dict.get("id") == "${userId}":
            parames_dict["id"] = oi.getData("id")
        if parames_dict.get("token") == "${token}":
            parames_dict["token"] = oi.getData("token")
        if parames_dict.get("phone") == "${phone}":
            parames_dict["phone"] = oi.getData("phone")
        if parames_dict.get("userFullName") == "${randomName}":
            parames_dict["userFullName"] = rd.randomName()

    delay = data[ExcelVarles.case_delay]
    save_datas = data[ExcelVarles.case_saveData]
    apiName = data[ExcelVarles.case_apiName]
    request_method = data[ExcelVarles.case_method]
    isRun = data[ExcelVarles.case_isRun]
    check_points = data[ExcelVarles.case_checkPoint].split(":")
    host = data[ExcelVarles.case_host]
    url_path = data[ExcelVarles.case_url]
    url = host + url_path

    # MyLog.info("请求数据---url---{}\t---header---{}\t---method---{}\t---params---{}".format(url, headers_dict, request_method, parames_dict))

    if isRun == "yes":
        resDict = api.request_main(method=request_method,url=url,data=parames_dict,headers=headers_dict)
        MyLog.info("\n---接口名称-{}\n---响应数据---{}".format(apiName,resDict))

        if delay == "yes":
            sleep(1)

        if len(save_datas) > 1:
            section = data[ExcelVarles.case_section]
            try:
                saves(datas=save_datas,resDict=resDict,section=section)
            except Exception as e:
                MyLog.error("数据保存报错，比对用例表中‘保存数据’内容与响应结果的差别。\n保存报错信息--{}\n请求响应数据内容--{}".format(e, resDict))
        assert check_points[1] in resDict[check_points[0]]
    else:
        pass

def saves(datas, resDict,section="message"):
    """
    保存响应数据，后续接口使用
    :param datas: 需要保存的字段信息
    :param resDict: 响应数据
    :param section: 段
    :return:
    """
    datas: dict = json.loads(datas)
    keys = datas.keys()
    for key in keys:
        dataValues = datas[key]
        if type(dataValues[0]) is list:
            for i in range(len(dataValues[0])):
                values = resDict[key].get(dataValues[0][i])
                if len(values) > 0:
                    for j in range(len(dataValues[1])):
                        option_k = dataValues[1][j]
                        option_v = values[0].get(dataValues[1][j])
                        oi.setData(value=str(option_v),option=option_k,section=section)
                else:
                    MyLog.info("该字段响应数据为空--{}".format(dataValues[0][i]))
        else:
            for value in datas[key]:
                oi.setData(value=str(resDict[key][value]),option=value,section=section)