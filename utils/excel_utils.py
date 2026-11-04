import openpyxl


def read_excel():
        # 打开excel文件
    workbook = openpyxl.load_workbook("./data/case.xlsx")
        # 选表
    worksheet = workbook["Sheet1"]
        # 读数据
        # zip函数可以把可迭代对象打包成一个个元组
    data = []
    keys = [cell.value for cell in worksheet[2]]
    for row in worksheet.iter_rows(min_row=3, values_only=True):

        dict_data = dict(zip(keys, row))
        if dict_data["is_true"]:
            data.append(dict_data)
        # 关闭excel文件
    workbook.close()

    return data
