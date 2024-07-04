import http.client
import json

conn = http.client.HTTPSConnection("endoflife.date")

headers = { 'Accept': "application/json" }

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
products2 = [
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

    # 파일로 결과 저장
    with open(f"d:\\{product}_result.txt", "w") as file:
        if isinstance(parsed_data, list):
            for item in parsed_data:
                for key, value in item.items():
                    file.write(f"{key}: {value}/")
                file.write("\n")
        elif isinstance(parsed_data, dict):
            for key, value in parsed_data.items():
                file.write(f"{key}: {value}/")
            file.write("\n")

conn.close()