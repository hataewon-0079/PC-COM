# Linux 서버 모니터링 스크립트
# 1. CPU 사용량
# 2. 메모리 사용량
# 3. 디스크 사용량
# 4. 네트워크 사용량
# 5. 프로세스 사용량
# 6. 사용자 접속 정보
# 7. 서비스 상태
# 8. 로그인 정보

import psutil
import os
import platform
import socket
import time
import datetime
import json
from collections import OrderedDict
import subprocess

# 시스템 정보
def get_system_info():
    system_info = OrderedDict()
    system_info['platform'] = platform.platform()
    system_info['cpu'] = platform.processor()
    system_info['memory'] = f"{psutil.virtual_memory().total / 1024 / 1024}MB"
    system_info['disk'] = f"{psutil.disk_usage('/').total / 1024 / 1024 / 1024}GB"
    system_info['network'] = socket.gethostbyname(socket.gethostname())
    system_info['boot_time'] = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return system_info

# CPU 사용량
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# 메모리 사용량
def get_memory_usage():
    return psutil.virtual_memory().percent

# 디스크 사용량
def get_disk_usage():
    return psutil.disk_usage('/').percent

# 네트워크 사용량
def get_network_usage():
    return psutil.net_io_counters()

# 프로세스 사용량
def get_process_usage():
    process_list = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['cpu_percent'] = proc.cpu_percent()
            pinfo['memory_percent'] = proc.memory_percent()
            process_list.append(pinfo)
        except psutil.NoSuchProcess:
            pass
    return process_list

# 사용자 접속 정보
def get_users():
    return psutil.users()

# 서비스 상태

def get_service_status():
    services = ['httpd', 'sshd', 'ntpd']
    service_list = []
    for service in services:
        service_info = OrderedDict()
        service_info['name'] = service
        service_info['status'] = 'active' if subprocess.call(['systemctl', 'is-active', service]) == 0 else 'inactive'
        service_list.append(service_info)
    return service_list

# 로그인 정보
def get_login_info():
    login_info = OrderedDict()
    login_info['users'] = get_users()
    login_info['service'] = get_service_status()
    return login_info

# 시스템 모니터링 정보
def get_system_mon():
    system_mon = OrderedDict()
    system_mon['system'] = get_system_info()
    system_mon['cpu'] = get_cpu_usage()
    system_mon['memory'] = get_memory_usage()
    system_mon['disk'] = get_disk_usage()
    system_mon['network'] = get_network_usage()
    system_mon['process'] = get_process_usage()
    system_mon['login'] = get_login_info()
    return system_mon

# 시스템 모니터링 정보를 JSON 파일로 저장
def save_system_mon():
    system_mon = get_system_mon()
    with open('d:\\system_mon.json', 'w') as file:
        json.dump(system_mon, file, indent=4)

if __name__ == '__main__':
    save_system_mon()
    print('시스템 모니터링 정보를 저장하였습니다.')
