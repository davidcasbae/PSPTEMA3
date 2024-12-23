import socket

def servidor_tcp():
    global s
    try:
        # Crear socket TCP IPv4
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", 5000))
        s.listen(1)  # Aceptar una conexión
        print("[SERVIDOR] Esperando conexiones...")

        conn, addr = s.accept()
        print("[SERVIDOR] Conexión establecida con", addr)

        try:
            # Enviar un mensaje al cliente
            mensaje = "Bienvenido al servidor. Envíame algo!"
            conn.send(mensaje.encode())

            # Recibir respuesta del cliente
            datos = conn.recv(1024)
            print("[SERVIDOR] Datos recibidos:", datos.decode())

            # Enviar datos de vuelta en mayúsculas
            conn.send(datos.upper())
        except Exception as e:
            print(f"[SERVIDOR] Error durante la comunicación con el cliente: {e}")
        finally:
            conn.close()
            print("[SERVIDOR] Conexión cerrada con el cliente.")
    except Exception as e:
        print(f"[SERVIDOR] Error en el servidor: {e}")
    finally:
            s.close()
            print("[SERVIDOR] Servidor cerrado.")

# Ejecuta esta celda para iniciar el servidor.
# Luego, en otra terminal o en otro notebook, puedes conectar con un cliente.
servidor_tcp()