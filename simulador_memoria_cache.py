# -*- coding: utf-8 -*-

'''
Construa um simulador de algoritmos de substituição de página de memória em cache. O simulador
deve receber como entrada a sequencia de referências às páginas de memória principal (endereços),
e simular as substituições realizadas em cache após a ocorrência de um miss, para os algoritmos
FIFO, LRU, LFU e RANDOM. O programa deve receber como parâmetro a capacidade total da
memória cache (ou seja, número total de páginas), o esquema de mapeamento (direto, associativo e
associativo por conjunto) que a cache vai operar, e o nome do arquivo de entrada a ser lido pelo
programa, contendo as sequências de referências aos acessos de páginas da memória. O formato do
arquivo de entrada consiste em um valor de endereço de memória (um número inteiro por linha) a
ser carregado no programa. A saída do simulador deve consistir de, para cada política de
substituição:

a. A cada nova referência de memoria do arquivo de entrada, imprimir a lista de todas as
páginas armazenadas na memória cache;

b. Ao final da execução, a fração de acertos às referências de memória para cada política.

'''
import numpy as np
import random

acertos = 0
erros = 0


# mapeamento direto
def mapeamento_direto(enderecos_solicitados):
	status_cache()
	global acertos, erros
	acertos = 0
	erros = 0
	for endereco in enderecos_solicitados:
		if (int(endereco) == dados_cache[int(endereco) % tamanho_paginas_cache]):
			print "CACHE-HIT - Os dados do endereço %d da memória já estavam na memória cache" % int(endereco)
			acertos += 1
		else:
			print "CACHE-MISS - Os dados do endereço %d da memória não estavam na memória cache" % int(endereco)
			dados_cache[int(endereco) % tamanho_paginas_cache] = int(endereco)
			erros += 1
		status_cache_operacoes()
	fracao_acertos()
	status_cache()
	print


# mapeamento associativo
def mapeamento_associativo(enderecos_solicitados, tipo):

	status_cache()
	global acertos, erros
	acertos = 0
	erros = 0
	contador = 0

	enderecos_solicitados = map(int, enderecos_solicitados)

	if (tipo == "FIFO"):

		while (contador < len(enderecos_solicitados)):
			if (enderecos_solicitados[contador] in dados_cache):
				print "CACHE-HIT - Os dados do endereço %d da memória já estavam na memória cache" % enderecos_solicitados[contador]
				acertos += 1
			else:
				print "CACHE-MISS - Os dados do endereço %d da memória não estavam na memória cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache):
					dados_cache[dados_cache.index(None)] = enderecos_solicitados[contador]
				else:
					dados_cache.pop(0)
					dados_cache.append(enderecos_solicitados[contador])
			contador += 1
			status_cache_operacoes()

	if (tipo == "LRU"):

		while (contador < len(enderecos_solicitados)):
			if (enderecos_solicitados[contador] in dados_cache):
				print "CACHE-HIT - Os dados do endereço %d da memória já estavam na memória cache" % enderecos_solicitados[contador]
				acertos += 1
				aux = dados_cache.pop(dados_cache.index(int(enderecos_solicitados[contador])))
				dados_cache.insert(0, aux)
			else:
				print "CACHE-MISS - Os dados do endereço %d da memória não estavam na memória cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache):
					dados_cache[dados_cache.index(None)] = enderecos_solicitados[contador]
				else:
					dados_cache.pop()
					dados_cache.insert(0,enderecos_solicitados[contador])
			contador += 1
			status_cache_operacoes()

	if (tipo == "LFU"):

		while (contador < len(enderecos_solicitados)):
			if (enderecos_solicitados[contador] in dados_cache):
				print "CACHE-HIT - Os dados do endereço %d da memória já estavam na memória cache" % enderecos_solicitados[contador]
				acertos += 1
				dados_cache_frequencia[dados_cache.index(int(enderecos_solicitados[contador]))] += 1
			else:
				print "CACHE-MISS - Os dados do endereço %d da memória não estavam na memória cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache):
					dados_cache_frequencia[dados_cache.index(None)] = 1
					dados_cache[dados_cache.index(None)] = enderecos_solicitados[contador]
				else:
					index = dados_cache.index(min(dados_cache))
					dados_cache.pop(index)
					dados_cache.insert(index, enderecos_solicitados[contador])
					dados_cache_frequencia[index] = 1
			contador += 1
			status_cache_operacoes()

	if (tipo == "RANDOM"):

		while (contador < len(enderecos_solicitados)):
			if (enderecos_solicitados[contador] in dados_cache):
				print "CACHE-HIT - Os dados do endereço %d da memória já estavam na memória cache" % enderecos_solicitados[contador]
				acertos += 1
			else:
				print "CACHE-MISS - Os dados do endereço %d da memória não estavam na memória cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache):
					dados_cache[dados_cache.index(None)] = enderecos_solicitados[contador]
				else:
					numero_aleatorio = random.randrange(tamanho_paginas_cache)
					dados_cache.pop(numero_aleatorio)
					dados_cache.insert(numero_aleatorio, enderecos_solicitados[contador])
			contador += 1
			status_cache_operacoes()

	fracao_acertos()
	status_cache()
	print


# mapeamento associativo por conjuntos
def mapeamento_associativo_conjuntos(enderecos_solicitados, tipo):
	status_cache()
	global acertos, erros
	acertos = 0
	erros = 0
	contador = 0

	enderecos_solicitados = map(int, enderecos_solicitados)

	if (tipo == "FIFO"):

		while (contador < len(enderecos_solicitados)):
			conjunto = enderecos_solicitados[contador]%tamanho_paginas_cache/tamanho_quadro
			#print enderecos_solicitados[contador]
			#print conjunto
			if (enderecos_solicitados[contador] in dados_cache[conjunto*tamanho_quadro:(conjunto+1)*tamanho_quadro]):
				print "CACHE-HIT - Os dados do endereço %d da memória já estavam na memória cache" % enderecos_solicitados[contador]
				acertos += 1
			else:
				print "CACHE-MISS - Os dados do endereço %d da memória não estavam na memória cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache[conjunto*tamanho_quadro:(conjunto+1)*tamanho_quadro]):
					dados_cache[conjunto*tamanho_quadro+dados_cache[conjunto*tamanho_quadro:(conjunto+1)*tamanho_quadro].index(None)] = enderecos_solicitados[contador]
				else:
					dados_cache.pop(conjunto*tamanho_quadro)
					dados_cache.insert((conjunto+1)*tamanho_quadro-1,enderecos_solicitados[contador])
			contador += 1
			status_cache_operacoes()

	if (tipo == "LRU"):

		while (contador < len(enderecos_solicitados)):
			conjunto = enderecos_solicitados[contador] % tamanho_paginas_cache / tamanho_quadro
			#print enderecos_solicitados[contador]
			#print conjunto
			if (enderecos_solicitados[contador] in dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro]):
				print "CACHE-HIT - Os dados do endereço %d da memória já estavam na memória cache" % enderecos_solicitados[contador]
				acertos += 1
				aux = dados_cache.pop(dados_cache.index(int(enderecos_solicitados[contador])))
				dados_cache.insert(conjunto * tamanho_quadro, aux)
			else:
				print "CACHE-MISS - Os dados do endereço %d da memória não estavam na memória cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro]):
					dados_cache[
						conjunto * tamanho_quadro + dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro].index(
							None)] = enderecos_solicitados[contador]
				else:
					dados_cache.pop((conjunto + 1) * tamanho_quadro - 1)
					dados_cache.insert((conjunto + 1) * tamanho_quadro - 1, enderecos_solicitados[contador])
			contador += 1
			status_cache_operacoes()

	if (tipo == "LFU"):

		while (contador < len(enderecos_solicitados)):
			conjunto = enderecos_solicitados[contador] % tamanho_paginas_cache / tamanho_quadro
			#print enderecos_solicitados[contador]
			#print conjunto
			if (enderecos_solicitados[contador] in dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro]):
				print "CACHE-HIT - Os dados do endereço %d da memória já estavam na memória cache" % enderecos_solicitados[contador]
				acertos += 1
				dados_cache_frequencia[dados_cache.index(int(enderecos_solicitados[contador]))] += 1
			else:
				print "CACHE-MISS - Os dados do endereço %d da memória não estavam na memória cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro]):
					dados_cache_frequencia[ (conjunto * tamanho_quadro) +dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro].index(None)] = 1
					dados_cache[
						conjunto * tamanho_quadro + dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro].index(
							None)] = enderecos_solicitados[contador]
				else:
					index = dados_cache.index(min(dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro]))
					dados_cache.pop(index)
					dados_cache.insert(index, enderecos_solicitados[contador])
					dados_cache_frequencia[index] = 1
			contador += 1
			status_cache_operacoes()

	if (tipo == "RANDOM"):

		while (contador < len(enderecos_solicitados)):
			conjunto = enderecos_solicitados[contador] % tamanho_paginas_cache / tamanho_quadro
			#print enderecos_solicitados[contador]
			#print conjunto
			if (enderecos_solicitados[contador] in dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro]):
				print "CACHE-HIT - Os dados do endereço %d da memória já estavam na memória cache" % enderecos_solicitados[contador]
				acertos += 1
				aux = dados_cache.pop(dados_cache.index(int(enderecos_solicitados[contador])))
				dados_cache.insert(conjunto * tamanho_quadro, aux)
			else:
				print "CACHE-MISS - Os dados do endereço %d da memória não estavam na memória cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro]):
					dados_cache[
						conjunto * tamanho_quadro + dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro].index(
							None)] = enderecos_solicitados[contador]
				else:
					numero_aleatorio = random.randrange((conjunto) * tamanho_quadro,(conjunto+1) * tamanho_quadro)
					dados_cache.pop(numero_aleatorio)
					dados_cache.insert((conjunto + 1) * tamanho_quadro - 1, enderecos_solicitados[contador])
			contador += 1
			status_cache_operacoes()

	fracao_acertos()
	status_cache()
	print


def abrir_arquivo_de_acessos_mp(nome):
	try:
		f = open(nome, "r")
		enderecos = f.readlines()
		f.close()
		return enderecos
	except:
		return False


def gerar_requisicoes_aleatorias(tamanho_requisicoes):
	return np.random.randint(low=0, high=tamanho_paginas_cache*3, size=tamanho_requisicoes)


def instancia_memoria_cache():
	dados_cache = np.empty((1, tamanho_paginas_cache), object)
	dados_cache = dados_cache[0]
	dados_cache = list(dados_cache)
	return dados_cache


def propriedades_memorias():
	print("O tamanho da cache é de " + str(len(dados_cache)) + " páginas")
	print("O tamanho da memoria principal é de " + str(tamanho_mp))
	print


def status_cache():
	print("dados da cache: " + str(dados_cache))


def fracao_acertos():
    #print("Acertos: " + str(acertos))
    #print("Erros: " + str(erros))
    print "Fração de acertos: %.3f %%" %((acertos/float((erros+acertos)))*100)


def status_cache_operacoes():
	print("páginas armazenadas na memória cache após a operação: " + str(dados_cache))


# ---------------------- Configuracoes ---------------------------

tamanho_paginas_cache = raw_input("Digite o número de páginas da cache: ")
tamanho_paginas_cache = int(tamanho_paginas_cache)
tipo_mapeamento = raw_input("Digite o tipo de mapeamento: \n\n1 - Mapeamento Direto\n2 - Mapeamento Associativo\n3 - Mapeamento Associativo por conjunto\n\n")
tipo_mapeamento = int(tipo_mapeamento)
while (tipo_mapeamento != 1 and tipo_mapeamento != 2 and tipo_mapeamento != 3):
    tipo_mapeamento = raw_input("Valor incorreto!\n\nDigite o tipo de mapeamento: \n\n1 - Mapeamento Direto\n2 - Mapeamento Associativo\n3 - Mapeamento Associativo\n\n")
    tipo_mapeamento = int(tipo_mapeamento)

if (tipo_mapeamento == 2 or tipo_mapeamento == 3):
    tipo = raw_input("\nDigite o algoritmo: \n\n1 - FIFO\n2 - LRU\n3 - LFU\n4 - RANDOM\n\n")
    tipo = int(tipo)
    while (tipo != 1 and tipo != 2 and tipo != 3 and tipo != 4):
        tipo = raw_input("\nDigite o algoritmo: \n\n1 - FIFO\n2 - LRU\n3 - LFU\n4 - RANDOM\n\n")
        tipo = int(tipo)
    if (tipo_mapeamento == 3):
        tamanho_quadro = raw_input("\nDigite o número de quadros por conjunto: ")
        tamanho_quadro = int(tamanho_quadro)
        while (tamanho_quadro < 0 or tamanho_paginas_cache%tamanho_quadro != 0):
            tamanho_quadro = raw_input("\nNúmero de quadros não multiplo do número de células da memória cache! Digite outro número de quadros por conjunto: ")
            tamanho_quadro = int(tamanho_quadro)

arquivo_entrada = raw_input("\nDigite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executável. Exemplo: 'nome_do_arquivo.txt'): ")
enderecos_memoria = abrir_arquivo_de_acessos_mp(arquivo_entrada)
while (enderecos_memoria == False):
    arquivo_entrada = raw_input("\nArquivo não encontrado! Digite o nome do arquivo de entrada novamente: ")
    enderecos_memoria = abrir_arquivo_de_acessos_mp(arquivo_entrada)

tamanho_mp = tamanho_paginas_cache * 100
dados_cache = instancia_memoria_cache()
propriedades_memorias()
# ----------------------------------------------------------------


# -------------------- Mapeamento direto -------------------------
if (tipo_mapeamento == 1):
    #enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache)
    mapeamento_direto(enderecos_memoria)

# ----------------------------------------------------------------


# -------------------- Mapeamento Associativo -------------------------
if (tipo_mapeamento == 2):
    # ------------------------------FIFO------------------------------------

    if (tipo == 1):
        #enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache) #teste - gerando requisicoes aleatórias
        mapeamento_associativo(enderecos_memoria, "FIFO")


    # ------------------------------LRU------------------------------------
    if (tipo == 2):
        #enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache) #teste - gerando requisicoes aleatórias
        mapeamento_associativo(enderecos_memoria, "LRU")
        #enderecos_memoria = list([enderecos_memoria[3], enderecos_memoria[3], enderecos_memoria[3], enderecos_memoria[5], 1]) #teste
        #mapeamento_associativo(enderecos_memoria, "LRU") #teste


    # ------------------------------LFU------------------------------------
    if (tipo == 3):
        dados_cache_frequencia = instancia_memoria_cache()
        #enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache) #teste - gerando requisicoes aleatórias
        mapeamento_associativo(enderecos_memoria, "LFU")
        #enderecos_memoria = list([enderecos_memoria[3], enderecos_memoria[3], enderecos_memoria[3], enderecos_memoria[5], 1,3,4,5,1,4,2,3,3]) #teste
        print("Frequencia das páginas da cache: "+dados_cache_frequencia)
        #mapeamento_associativo(enderecos_memoria, "LFU")  #teste
        #print(dados_cache_frequencia)  #teste


    # ----------------------------RANDOM------------------------------------
    if (tipo == 4):
        #enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache) #teste - gerando requisicoes aleatórias
        mapeamento_associativo(enderecos_memoria, "RANDOM")




# ------------- Mapeamento Associativo por conjunto --------------------
if (tipo_mapeamento == 3):
    # ------------------------------FIFO------------------------------------
    if (tipo == 1):
        #enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache) #teste - gerando requisicoes aleatórias
        mapeamento_associativo_conjuntos(enderecos_memoria, "FIFO")

    # ------------------------------LRU------------------------------------
    if (tipo == 2):
        #enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache) #teste - gerando requisicoes aleatórias
        mapeamento_associativo_conjuntos(enderecos_memoria, "LRU")
        #enderecos_memoria = list([1159, 1159, 1159, 1039, enderecos_memoria[5], 1]) #teste
        #mapeamento_associativo_conjuntos(enderecos_memoria, "LRU") #teste

    # ------------------------------LFU------------------------------------
    if (tipo == 3):
		dados_cache_frequencia = instancia_memoria_cache()
		#enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache) #teste - gerando requisicoes aleatórias
		mapeamento_associativo_conjuntos(enderecos_memoria, "LFU")
		#enderecos_memoria = list([enderecos_memoria[3], enderecos_memoria[3], enderecos_memoria[3], enderecos_memoria[5], 1, 3, 4, 5, 1, 4, 2, 3, 3]) #teste
		print("Frequencia das páginas da cache: " + dados_cache_frequencia)
		#mapeamento_associativo_conjuntos(enderecos_memoria, "LFU") #teste
		#print(dados_cache_frequencia) #teste

    # ----------------------------RANDOM------------------------------------
    if (tipo == 4):
        #enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache) #teste - gerando requisicoes aleatórias
        mapeamento_associativo_conjuntos(enderecos_memoria, "RANDOM")
        #enderecos_memoria = gerar_requisicoes_aleatorias(5) #teste - gerando requisicoes aleatórias
        #mapeamento_associativo_conjuntos(enderecos_memoria, "RANDOM") #teste

