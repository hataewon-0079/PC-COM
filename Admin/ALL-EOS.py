import http.client

conn = http.client.HTTPSConnection("endoflife.date")

headers = { 'Accept': "application/json" }

conn.request("GET", "/api/all.json", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


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
    "apache",
    "mssqlserver",
    "log4j",
    "tomcat",
    "windows-server",
    "windows"
]

# target_keys = ["cycle", "releaseLabel", "support", "eol", "latest"]
#
# for product in products:
#     conn.request("GET", f"/api/{product}.json", headers=headers)
#     res = conn.getresponse()
#     data = res.read()
#     decoded_data = data.decode("utf-8")
#     parsed_data = json.loads(decoded_data)
#
#     print(f"Product: {product}")
#
#     if isinstance(parsed_data, list):
#         for item in parsed_data:
#             for key, value in item.items():
#                 if key in target_keys:
#                     print(f"{key}: {value}")
#             print("---------------------")
#     elif isinstance(parsed_data, dict):
#         for key, value in parsed_data.items():
#             if key in target_keys:
#                 print(f"{key}: {value}")
#         print("---------------------")
#
#     # 파일로 결과 저장
#     with open(f"d:\\{product}_result.txt", "w") as file:
#         if isinstance(parsed_data, list):
#             for item in parsed_data:
#                 for key, value in item.items():
#                     if key in target_keys:
#                         file.write(f"{key}: {value}/")
#                 file.write("\n")
#         elif isinstance(parsed_data, dict):
#             for key, value in parsed_data.items():
#                 if key in target_keys:
#                     file.write(f"{key}: {value}/")
#             file.write("\n")

# for product in products:
#     conn.request("GET", f"/api/{product}.json", headers=headers)
#     res = conn.getresponse()
#     data = res.read()
#     # print(f"Product: {product}")
#     # print(data.decode("utf-8"))
#     decoded_data = data.decode("utf-8")
#     parsed_data = json.loads(decoded_data)
#
#     if isinstance(parsed_data, list):
#         for item in parsed_data:
#             for key, value in item.items():
#                 print(f"{key}: {value}")
#             print("---------------------")
#     elif isinstance(parsed_data, dict):
#         for key, value in parsed_data.items():
#             print(f"{key}: {value}")
#         print("---------------------")
#
#     # 파일로 결과 저장
#     with open(f"d:\\{product}_result.txt", "w") as file:
#         if isinstance(parsed_data, list):
#             for item in parsed_data:
#                 for key, value in item.items():
#                     file.write(f"{key}: {value}\n")
#                 file.write("---------------------\n")
#         elif isinstance(parsed_data, dict):
#             for key, value in parsed_data.items():
#                 file.write(f"{key}: {value}\n")
#             file.write("---------------------\n")

conn.close()