import socket
import threading

import cliente_ej02


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
        hilo_cliente = threading.Thread(target=cliente_ej02.cliente_tcp)
        hilo_cliente.start()
        print(f"[ACTIVO] Número de conexiones activas: {threading.active_count() - 1}")
        conn.close()
        s.close()

servidor_tcp()