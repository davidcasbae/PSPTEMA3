import socket

def servidor_udp():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    servidor.bind(("", 5005))

    print(f"[SERVIDOR] Escuchando en el puerto...")

    while True:
        try:
            # Recibir mensaje
            mensaje, direccion = servidor.recvfrom(1024)
            print(f"[SERVIDOR] Mensaje recibido de {direccion}: {mensaje.decode('utf-8')}")

            # Responder al cliente
            respuesta = "Mensaje recibido"
            servidor.sendto(respuesta.encode('utf-8'), direccion)
        except KeyboardInterrupt:
            print("[SERVIDOR] Cerrando servidor.")
            break

    servidor.close()

servidor_udp()