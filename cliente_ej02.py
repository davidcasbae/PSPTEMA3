import socket

def cliente_tcp():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("127.0.0.1", 5000))
    print("Nuevo [CLIENTE] Conectado al servidor.")

    while True:
        # Recibir datos del cliente
        msg = c.recv(1024)
        if not msg:
            break
        msg_decodificado = msg.decode()
        print(f"[RECIBIDO] {msg_decodificado}")

        # Verificar si el cliente quiere desconectarse
        if msg_decodificado.upper() == "QUIT":
            print(f"[DESCONECTAR] un cliente se ha desconectado.")
            break

        # Responder con el texto en mayúsculas
        respuesta = msg_decodificado.upper()
        c.sendall(respuesta)

    # Cerrar conexión
    c.close()

cliente_tcp()