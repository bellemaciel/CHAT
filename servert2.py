import socket, time, threading, os
semaforo = threading.BoundedSemaphore(1)

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(('192.168.207.19',12000))


lista_convo = []
listam = [('192.168.202.61',12000), ('192.168.207.38',12000)]

def escuta():
	while True:
		mensagem_bytes, ip_cliente = servidor.recvfrom(2048)#aguarda respota do cliente, recebe mensagem e ip
		#quebrar mensagem e time			
		mensagem_resposta = (mensagem_bytes.decode())#decodifica a mensagem que está em binário
		print("Mensagem Recebida do Cliente: ",mensagem_resposta)
		semaforo.acquire()
		lista_convo.append(mensagem_resposta)#adiciona na lista
		semaforo.release()
		
		imprime()
	
	
		
def envia():
	while True:
		imprime()
		mensagem_enviar = input()#mensagem que será enviada do servidor
		for m in listam:
			servidor.sendto(str(mensagem_enviar).encode(),m)#enviando para o cliente a nova mensagem, esse ip é de outra máquina
		semaforo.acquire()
		lista_convo.append(mensagem_enviar)#adiciona na lista
		semaforo.release()
		#calcular time
		

def imprime():
	os.system('clear')	
	print('Histórico conversa: ')#mostra na tela a conversa
	for msg in lista_convo:
		print(msg)
	print("Digite uma mensagem: ")
	
	
	
print("iniciou")
t1 = threading.Thread(target=escuta)
t2 = threading.Thread(target=envia)
t1.start()
t2.start()

	