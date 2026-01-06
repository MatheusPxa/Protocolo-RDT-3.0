from socket import *
import time
import random

# Função de checksum simples
def checksum(data):
    return sum(ord(c) for c in data) % 256

serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(3)  # timeout de 3 segundos

seq = 0  # número de sequência (0 ou 1)

print("=== MENU ===")
print("1 - Entrega normal")
print("2 - Corromper dados")
print("3 - Inserir atraso artificial")

opcao = input("Escolha: ")

data = input("Digite a mensagem: ")
cs = checksum(data)

# Simulação de corrupção
if opcao == "2":
    cs += 1  # altera checksum propositalmente
    print("Dados corrompidos intencionalmente")

packet = f"{seq}|{cs}|{data}"

while True:
    print("\nEnviando pacote:")
    print(f" SEQ={seq}, CHECKSUM={cs}, DADOS='{data}'")

    # Simulação de atraso artificial
    if opcao == "3":
        atraso = random.uniform(2, 5)  # atraso entre 2 e 5 segundos
        print(f"Inserindo atraso artificial de {atraso:.2f} segundos...")
        time.sleep(atraso)

    clientSocket.sendto(packet.encode(), (serverName, serverPort))

    try:
        ack, _ = clientSocket.recvfrom(2048)
        ack = ack.decode()

        print(f"ACK recebido: {ack}")

        if ack == f"ACK|{seq}":
            print("ACK correto, enviando próximo pacote")
            seq = 1 - seq  # alterna entre 0 e 1
            break
        else:
            print("ACK incorreto, retransmitindo")

    except timeout:
        print("TIMEOUT! Retransmitindo pacote")

clientSocket.close()
print("Conexão encerrada.")
