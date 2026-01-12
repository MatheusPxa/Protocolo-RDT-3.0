# RDT 3.0 - Reliable Data Transfer (Python)

Implementação do protocolo RDT 3.0 usando UDP, simulando **Stop-and-Wait** com:

- Numeração de pacotes (0 e 1)
- Checksum para detecção de corrupção
- ACKs para confirmação
- Timeout e retransmissão automática
- Simulação de canal não confiável:
  - Entrega normal
  - Corrupção de dados
  - Atraso artificial
  - Perda de pacotes (30% de chance)

---

## Como usar

1. Baixar ou fazer Download do projeto
2. Abra dois terminais: terá opção de abrir na sua máquina coloando o seu ip ou em abrir em 2 máquinas

### Executar servidor e cliente:

Será feito execução dentro do terminal do vs code

- Servidor
python server.py
logo em seguida deve consta seguinte mensagem para confirma que deu certo
Aguardando pacotes na porta 12000...

- Cliente
python client.py
logo em seguida deve consta seguinte mensagem para confirma que deu certo

=== MENU CANAL ===
1 - Entrega normal
2 - Corrupção de dados
3 - Atraso artificial
4 - Perda de pacotes
0 - Sair
Escolha a opção do canal:

basta escolher opção desejada e coloca o servidor para rodar a opção selecionada




