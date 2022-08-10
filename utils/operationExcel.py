# -*- coding:utf-8 -*-
import xlrd
from utils import getPath as fp

class OperationExcel:

    def getSheet(self, dirName, fileName, index= 0):
        book = xlrd.open_workbook(fp.filePath(dirName= dirName, fileName= fileName))
        sheet = book.sheet_by_index(index)
        return sheet

    def getExcelDatas(self, dirName, fileName):
        data = []
        sheet = self.getSheet(dirName,fileName)
        # 表头
        title = sheet.row_values(0)
        rows = sheet.nrows
        cols = sheet.ncols
        for row in range(1, rows):
            row_value = sheet.row_values(row)
            data.append(dict(zip(title, row_value)))
        return data


class ExcelVarles:
    case_id="id"
    case_apiName="接口名称"
    case_host="域名"
    case_url="接口地址"
    case_method="请求方式"
    case_headers = "请求头"
    case_data="请求参数"
    case_checkPoint = "检查点"
    case_saveData = "保存数据"
    case_section = "section"
    case_isRun="是否执行"
    case_delay = "请求延迟"



if __name__ == "__main__":
    dirName = r"data"
    fileName = r"接口测试用例.xls"
    ob = OperationExcel()
    data = ob.getExcelDatas(dirName= dirName, fileName= fileName)
    print(data, sep= "\t")