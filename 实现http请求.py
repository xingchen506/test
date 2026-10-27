import requests

#查询全部区域信息
response = requests.get("http://localhost:6255/wx/groupon/list",params={"page":1,"limit":10})
LOGIN = requests.post("http://localhost:9527/admin/auth/login",json={"code":"","password":"admin123","username":"admin123"})
response = requests.post("http://localhost:9527/admin/admin/create",data={"password":"123412","username":"qqqq1234"})

#print("状态码:",response.status_code)
#print("响应体:",response.text)

login_url = "http://localhost:9527/admin/auth/login"
login_body = {
    "username": "admin123",
    "password": "admin123"
}
login_resp = requests.post(login_url, json=login_body)
print("登录返回：", login_resp.json())
token = login_resp.json()["data"]["token"]

headers = {
    "Content-Type": "application/json",
    "X-Litemall-Admin-Token": token   # 关键！携带登录凭证
}

create_url = "http://localhost:9527/admin/admin/create"
create_body = {
    "username": "qqqq1234",
    "password": "123412"
}

#response = requests.post(create_url, json=create_body, headers=headers)
print("状态码:", login_resp.status_code)
print("响应体:", login_resp.json())
print("响应体:", login_resp.text)
print("响应体:", login_resp.content)



