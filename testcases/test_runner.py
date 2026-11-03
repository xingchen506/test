import jsonpath
import requests
import pytest
from utils.excel_utils import read_excel
import pymysql

class TestRunner:

    data = read_excel()
    #提取后的数据需要初始化一个全局的属性保存，使用空字典
    all = {}

    @pytest.mark.parametrize("case",data)
    def test_case(self,case):

        #引入全局变量all
        all = self.all
        method = case["method"]
        url = "http://localhost:9527/admin/auth" + case["path"]
        headers = eval(case["headers"]) if isinstance(case["headers"],str) else None
        params = eval(case["params"]) if isinstance(case["params"], str) else None
        data = eval(case["data"]) if isinstance(case["data"], str) else None
        json = eval(case["json"]) if isinstance(case["json"], str) else None
        files = eval(case["files"]) if isinstance(case["files"], str) else None

        request_data = {
            "method":method,
            "url":url,
            "headers":headers,
            "params":params,
            "data":data,
            "json":json,
            "files":files
        }
        res = requests.request(**request_data)
        #http响应断言
        if case["check"]:
            assert jsonpath.jsonpath(res.json(),"$.errmsg")[0]== case["expected"]
        else:
            assert case["expected"] in res.text
        #数据库断言
        if case["sql_check"] and case["sql_expected"]:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                database="litemall",
                user="root",
                password="123456",
                charset="utf8"
            )
            cur =conn.cursor()
            cur.execute(case["sql_check"])
            result = cur.fetchone()
            cur.close()
            conn.close()
            assert result[0] == case["sql_expected"]

        #提取
        #json提取
        if case["jsonExData"]:
            #首先把josnExData拆开
            for key,value in eval(case["jsonExData"]).items():
                value = jsonpath.jsonpath(res.json(),value)[0]
                all[key] = value
                # print(type(value))
        #数据库提取
        if case["sqlExData"]:
            for key,value in eval(case["sqlExData"]).items():
                conn = pymysql.connect(
                    host="localhost",
                    port=3306,
                    database="litemall",
                    user="root",
                    password="123456",
                    charset="utf8"
                )
                cur = conn.cursor()
                cur.execute(value)
                result = cur.fetchone()
                cur.close()
                conn.close()
                value = result[0]
                all[key] = value
                print(all)