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


# Recebendo a mensagem do usuário final pelo teclado
mensagem = input()
 
# Enviando a mensagem para o Servidor TCP através da conexão
while mensagem != '':
    conn.send(str(mensagem).encode())
    print("Resposta: {}".format(
        conn.recv(1024)
    ))
    mensagem = input()
    



