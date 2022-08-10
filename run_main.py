# -*- coding:utf-8 -*-
import os

import pytest

if __name__ == "__main__":
    pytest.main(["-s","./tests/test_case.py","--alluredir=report/result"])
    os.system("allure generate report/result -o ./report/report  --clean")
    print("abv")