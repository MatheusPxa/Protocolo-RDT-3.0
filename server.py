from socket import *
import time

def checksum(data):
    return sum(ord(c) for c in data) % 256

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

expected_seq = 0

print("Servidor RDT 3.0 aguardando mensagens...")

while True:
    packet, clientAddress = serverSocket.recvfrom(2048)
    packet = packet.decode()

    seq, recv_checksum, data = packet.split("|")
    seq = int(seq)
    recv_checksum = int(recv_checksum)

    calc_checksum = checksum(data)

    print("\n[SERVIDOR] Pacote recebido:")
    print(f"  SEQ={seq}, CHECKSUM recebido={recv_checksum}, CHECKSUM calculado={calc_checksum}")
    print(f"  DADOS='{data}'")

    if recv_checksum != calc_checksum:
        print("[SERVIDOR] Pacote CORROMPIDO! Ignorando...")
        continue

    if seq == expected_seq:
        print("[SERVIDOR] Pacote correto!")
        ack = f"ACK|{seq}"
        serverSocket.sendto(ack.encode(), clientAddress)
        expected_seq = 1 - expected_seq
    else:
        print("[SERVIDOR] Pacote duplicado, reenviando ACK anterior")
        ack = f"ACK|{1 - expected_seq}"
        serverSocket.sendto(ack.encode(), clientAddress)