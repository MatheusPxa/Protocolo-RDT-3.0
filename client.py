from socket import *
import time
import random

def checksum(data):
    return sum(ord(c) for c in data) % 256

serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(3)  

seq = 0  

print("=== Cliente RDT 3.0 ===")

while True:
    print("\n=== MENU CANAL ===")
    print("1 - Entrega normal")
    print("2 - Corrupção de dados")
    print("3 - Atraso artificial")
    print("4 - Perda de pacotes")
    print("0 - Sair")
    opcao = input("Escolha a opção do canal: ")

opcao = input("Escolha: ")

data = input("Digite a mensagem: ")
cs = checksum(data)

 if opcao == "0":
        print("Encerrando cliente...")
        break

    data = input("Digite a mensagem: ")
    cs = checksum(data)

    if opcao == "2":
        cs += 1
        print(">>> Dados corrompidos intencionalmente")

    packet = f"{seq}|{cs}|{data}"

    while True:
        print("\nEnviando pacote:")
        print(f"  SEQ={seq}, CHECKSUM={cs}, DADOS='{data}'")

        if opcao == "3":
            atraso = random.uniform(2, 5)
            print(f">>> Inserindo atraso artificial de {atraso:.2f} segundos...")
            time.sleep(atraso)

        if opcao == "4":
            if random.random() < 0.3:  
                print(">>> Pacote perdido intencionalmente! Retransmitindo...")
                time.sleep(1)
                continue

        clientSocket.sendto(packet.encode(), (serverName, serverPort))

        try:
            ack, _ = clientSocket.recvfrom(2048)
            ack = ack.decode()
            print(f"ACK recebido: {ack}")

            if ack == f"ACK|{seq}":
                print("ACK correto! Enviando próximo pacote...")
                seq = 1 - seq
                break
            else:
                print("ACK incorreto! Retransmitindo pacote...")

        except timeout:
            print("TIMEOUT! Retransmitindo pacote...")

clientSocket.close()
print("Cliente encerrado.")
