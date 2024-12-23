import socket
import threading

def cliente(conn, addr):
    print("Nuevo [CLIENTE] Conectado al servidor.")

    while True:
        # Recibir datos del cliente
        msg = conn.recv(1024)
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
        conn.sendall(respuesta)

    # Cerrar conexión
    conn.close()

def servidor_tcp():
    # Crear socket TCP IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 5002))
    s.listen(1)  # Aceptar una conexión
    print(f"[ESCUCHANDO] Servidor iniciado")

    while True:
        # Aceptar nueva conexión
        conn, addr = s.accept()
        print(f"[CONEXIÓN ESTABLECIDA] Cliente conectado")

        # Crear un hilo para manejar al cliente
        hilo_cliente = threading.Thread(target=cliente, args=(conn, addr))
        hilo_cliente.start()
        print(f"[ACTIVO] Número de conexiones activas: {threading.active_count() - 1}")


if __name__ == "__main__":
    servidor_tcp()