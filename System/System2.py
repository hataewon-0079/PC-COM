import time

import paramiko

def ssh_command(name, host, keyword, commands):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host, username=name, password=keyword)
        print("> Connected <\n")

        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode('utf8')
            error = stderr.read().decode('utf8')

            if output:
                if command == "df -h | grep /dev/sda1 | awk '{print $2}'":
                    output = f"디스크 총 용량:{output}"

                if command == "last -n 10":
                    output = f"최근 10개 로그인 기록:\n{output}"
                    
                print(f"결과:\n {output}")

            if error:
                print(f"에러:\n {error}")


    except Exception as err:
        print("Error: 접속 실패\n", err)

    finally:
        ssh.close()
        print("> Disconnected <\n")
def main():

    u_name = 'root'
    host = '172.29.30.232'
    keyword='1q2w3e4rRR'

    commands = [
        "ls",
        "pwd",
        "whoami",
        "df -h",
        "free -m",
        "uname -a",
        "cat /etc/*release",
        "df -h | grep /dev/sda1 | awk '{print $2}'",  # 디스크 총 용량
        "tail -n 100 /var/log/secure | grep 'Failed password' | wc -l",
        "last -n 10",  # 최근 10개의 로그인 기록
        "tail -n 10 /var/log/secure | grep 'Fail'",  # 인증 실패 로그
        "tail -n 10 /var/log/secure | grep 'Accepted\|Failed'",  # 로그인 시도 및 성공한 로그인
    ]

    ssh_command(u_name, host, keyword, commands)


if __name__ == '__main__':
    main()
