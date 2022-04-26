import socket,ssl
import os
HOST = '127.0.0.1'      # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está
PATH = os.path.dirname(os.path.abspath(__file__)) #diretorio atual


context = ssl.create_default_context()

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(PATH+"/apache-selfsigned.crt")
context.check_hostname=False
conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=HOST)
conn.connect((HOST, PORT))

cert = conn.getpeercert()


conn.sendall(b"Teste de mensagem do cliente")

print("Resposta: {}".format(
    conn.recv(1024).split(b"\r\n")
))
