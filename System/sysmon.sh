# Linux 서버를 점검하는 배치 프로그램

# 1. CPU 정보
echo "1. CPU 정보"
echo "CPU 코어 수: `grep processor /proc/cpuinfo | wc -l`"
echo "CPU 사용량: `top -b -n 1 | grep Cpu | awk '{print $2+$4}'`%"
echo

# 2. 메모리 정보, 용량 정보를 MB 단위로 출력
echo "2. 메모리 정보"
echo "전체 메모리: `free | grep Mem | awk '{print $2/1024}'`MB"
echo "사용 중인 메모리: `free | grep Mem | awk '{print $3/1024}'`MB"
echo "사용 가능한 메모리: `free | grep Mem | awk '{print $4/1024}'`MB"
echo




echo "사용 중인 메모리: `free | grep Mem | awk '{print $3}'`"
echo "사용 가능한 메모리: `free | grep Mem | awk '{print $4}'`"
echo

# 3. 디스크 정보
echo "3. 디스크 정보"
echo "전체 디스크: `df -h | grep /dev/sda1 | awk '{print $2}'`"
echo "사용 중인 디스크: `df -h | grep /dev/sda1 | awk '{print $3}'`"
echo "사용 가능한 디스크: `df -h | grep /dev/sda1 | awk '{print $4}'`"
echo

echo "aa : 'lastlog | grep -v \"Never logged in\" | wc -l'

# 보안로그 점검
echo "4. 보안로그 점검"
echo "`tail -f /var/log/secure | grep 'Failed password' | wc -l`"


# 4. 파티션 사용정보
echo "4. 파티션 사용정보"
echo "`df -h`"
echo


# 시스템 버전 확인
echo "5. 시스템 버전 확인"
echo "`cat /etc/*release`"
echo
# 커널 버전 확인
echo "5. 커널 버전 확인"
echo "`uname -a`"
echo

# apache 서비스 확인
echo "6. apache 서비스 확인"
echo "`ps -ef | grep httpd | wc -l`"
# apache 버전 확인
echo "6. apache 버전 확인"
echo "`httpd -v`"
echo

# tomcat 서비스 확인 확인
echo "7. tomcat 서비스 확인"
echo "`ps -ef | grep tomcat | wc -l`"
# tomcat 버전 확인
echo "7. tomcat 버전 확인"
echo "`/usr/local/tomcat/bin/version.sh`"
echo

# mysql 서비스 확인 확인
echo "8. mysql 서비스 확인"
echo "`ps -ef | grep mysql | wc -l`"
echo
# mysql 버전 확인
echo "8. mysql 버전 확인"
echo "`mysql -V`"
echo

# orcale 서비스 확인 확인
echo "9. oracle 서비스 확인"
echo "`ps -ef | grep oracle | wc -l`"
echo
# oracle 버전 확인
echo "9. oracle 버전 확인"
echo "`oracle -v`"
echo


# 점검 결과를 파일로 저장
echo "점검이 완료되었습니다." > sysmon.log
echo "CPU 코어 수: `grep processor /proc/cpuinfo | wc -l`" >> sysmon.log
echo "CPU 사용량: `top -b -n 1 | grep Cpu | awk '{print $2+$4}'`%" >> sysmon.log
echo "전체 메모리: `free | grep Mem | awk '{print $2/1024}'`MB" >> sysmon.log
echo "사용 중인 메모리: `free | grep Mem | awk '{print $3/1024}'`MB" >> sysmon.log

echo "전체 디스크: `df -h | grep /dev/sda1 | awk '{print $2}'`" >> sysmon.log


# 결과를 메일로 발송
mail -s "서버 점검 결과" root < sysmon.log

