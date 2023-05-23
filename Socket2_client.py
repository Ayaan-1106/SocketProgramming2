#2-1 클라이언트에서 file_name 입력 => 서버에 자료 있을 시 반환
#2-2 클라이언트에서 사칙연산 입력 => 서버에서 계산 후 반환
import socket

# DNS 서버 정보
dns_host = '172.31.115.125'  #    DNS 서버 IP 주소
dns_port = 8080         # DNS 서버 포트 번호

# DNS 서버에 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((dns_host, dns_port))

print("사용 가능 기능")
print("1. file_name을 입력후 내용 읽어오기")
print("2. 계산기")
print("3. 프로그램 종료")

while True:
    # DNS 쿼리 요청 입력
    
    user_input = input("사용할 기능을 고르시오: ")
    
    if user_input == '3':
        print("프로그램 종료")
        break

    elif user_input == '1':
        file_name = input("file_name: ")
        data = f"{user_input},{file_name}"
        client_socket.send(data.encode())

    elif user_input == '2':
        expression = input("사칙연산을 입력하세요: ")
        data = f"{user_input},{expression}"
        client_socket.send(data.encode())

    else:
        print("잘못된 입력입니다. 다시 시도하세요.")
        continue

    # DNS 응답 수신
    response = client_socket.recv(1024).decode()

    # 응답 출력
    print(response)

# 연결 종료
client_socket.close()