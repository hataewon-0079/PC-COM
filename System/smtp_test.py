# 메일 전송 테스트
import smtplib
from email.mime.text import MIMEText

# SMTP 서버 정보
smtp_server = "outbound.daouoffice.com"
# smtp_port = 587 # TLS
# smtp_port = 25 # SMTP
smtp_port = 465 # SSL
smtp_user = "twha@signgate.com.com"
smtp_password = ""

# 메일 내용 설정
sender = "twha@signgate.com"
receiver = "twha@signgate.com"
subject = "Test Email"
body = "This is a test TLS."

# MIMEText 객체 생성
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

# SMTP 서버 연결 TLS 일대는 다음의 소스를 사용한다.
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()  # TLS 암호화 활성화
# server.login(smtp_user, smtp_password)

# SMTP 서버 연결 SSL 일대는 다음의 소스를 사용한다.
server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.login(smtp_user, smtp_password)

# SMTP port 25 연결시에는 다음의 소스를 사용한다.
# server = smtplib.SMTP(smtp_server)
# server.login(smtp_user, smtp_password)

# 메일 전송
server.send_message(msg)

# SMTP 서버 연결 종료
server.quit()

print("메일이 성공적으로 전송되었습니다.")
