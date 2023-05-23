#2-1 클라이언트에서 file_name 입력 => 서버에 자료 있을 시 반환
#2-2 클라이언트에서 사칙연산 입력 => 서버에서 계산 후 반환
import socket

# 서버 IP 주소와 포트 번호
SERVER_IP = '172.31.115.125'
SERVER_PORT = 8080

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 소켓을 주소에 바인딩
server_socket.bind((SERVER_IP, SERVER_PORT))

# 클라이언트의 연결을 기다림
server_socket.listen(1)
print('서버가 시작되었습니다. 클라이언트의 연결을 기다립니다...')

# 클라이언트와의 연결 수락
client_socket, client_address = server_socket.accept()
print('클라이언트가 연결되었습니다:', client_address)

# 파일 이름과 내용을 저장할 딕셔너리 선언
file_data = {}
# 파일 이름과 내용 추가
file_data["이름"] = "조성현" 
file_data["학번"] = "32194319"
file_data["학과"] = "소프트웨어학과"


while True:
    # 클라이언트로부터 데이터 수신
    client_data = client_socket.recv(1024).decode()
    if not client_data:
        # 클라이언트가 연결을 종료한 경우
        print('클라이언트가 연결을 종료했습니다.')
        break

    user_input, userInput_data = client_data.split(',')          
   
    if user_input == '1': #user가 file_name 찾는 기능 실행시.
        if userInput_data in file_data:
            content = file_data[userInput_data]
            client_socket.send(content.encode())
        else:
            content = "파일을 찾을 수 없습니다."
            client_socket.send(content.encode())
    
    elif user_input == '2':
        result = str(eval(userInput_data))
        client_socket.send(result.encode())
 
# 연결 종료
client_socket.close()
server_socket.close()