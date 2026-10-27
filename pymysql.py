import pymysql

# 1.建立连接
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="123456",
    database="litemall",
    charset="utf8mb4"
)

# 2.获取游标
cur = conn.cursor()

# 3.执行sql（查询示例）
sql = "select * from litemall_user;"
cur.execute(sql)

# 4.取出查询结果
res = cur.fetchone()
print(res)

cur.close()
conn.close()
