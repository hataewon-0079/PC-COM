# Description: endoflife.date 사이트에서 제품별 지원 종료일을 가져와서 파일로 저장하는 소스
# 회사의 EOS(End of Support)를 관리하기 위해 사용


import http.client
import json

conn = http.client.HTTPSConnection("endoflife.date")

headers = { 'Accept': "application/json" }

# 제품명
products = [
    "rhel",
    "oracle-solaris",
    "oracle-database",
    "mysql",
    "postgresql",
    "mariadb",
    "mssqlserver",
    "log4j",
    "windows-server",
    "windows",
    "apache",
    "redhat-jboss-eap",
    "tomcat"
]


for product in products:
    conn.request("GET", f"/api/{product}.json", headers=headers)
    res = conn.getresponse()
    data = res.read()
    # print(f"Product: {product}")
    # print(data.decode("utf-8"))
    decoded_data = data.decode("utf-8")
    parsed_data = json.loads(decoded_data)

    if isinstance(parsed_data, list):
        for item in parsed_data:
            for key, value in item.items():
                print(f"{key}: {value}")
            print("---------------------")
    elif isinstance(parsed_data, dict):
        for key, value in parsed_data.items():
            print(f"{key}: {value}")
        print("---------------------")


#  조회한 결과를 하나의 파일로 저장
with open("d:\\result.txt", "a") as file:
    for product in products:
        conn.request("GET", f"/api/{product}.json", headers=headers)
        res = conn.getresponse()
        data = res.read()
        decoded_data = data.decode("utf-8")
        parsed_data = json.loads(decoded_data)
        file.write("\n\n")
        file.write("□□□□□□□□□□□□□□□□□□□□□\n")
        file.write(f"Product: {product}\n")
        file.write("□□□□□□□□□□□□□□□□□□□□□\n")
        if isinstance(parsed_data, list):
            for item in parsed_data:
                for key, value in item.items():
                    file.write(f"# {key}: {value},")
                file.write("\n")
        elif isinstance(parsed_data, dict):
            for key, value in parsed_data.items():
                file.write(f"# {key}: {value},")
            file.write("\n")




conn.close()