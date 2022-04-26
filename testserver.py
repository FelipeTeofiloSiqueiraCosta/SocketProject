import socket, ssl
import os
HOST = '127.0.0.1'      # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está
PATH = os.path.dirname(os.path.abspath(__file__)) #diretorio atual


context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile= PATH+"/apache-selfsigned.crt", keyfile= PATH+"/apache-selfsigned.key")

bindsocket = socket.socket()
bindsocket.bind((HOST, PORT))
bindsocket.listen(5)

def deal_with_client(connstream):
    data = connstream.recv(1024)
    # empty data means the client is finished with us
    print(data)
    connstream.sendall(b"Teste mensagem do servidor")
    
    while data:
       # if not do_something(connstream, data):
            # we'll assume do_something returns False
            # when we're finished with client
            #break
        data = connstream.recv(1024)
        print(data)
    # finished with client

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()