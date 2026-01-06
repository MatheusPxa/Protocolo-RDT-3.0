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
