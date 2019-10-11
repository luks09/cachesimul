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
			acertos += 1
		else:
			dados_cache[int(endereco) % tamanho_paginas_cache] = int(endereco)
			erros += 1
	print("Acertos: " + str(acertos))
	print("Erros: " + str(erros))
	status_cache()
	print


# mapeamento associativo
def mapeamento_associativo(enderecos_solicitados, tipo):
	status_cache()
	global acertos, erros
	acertos = 0
	erros = 0
	contador = 0

	if (tipo == "FIFO"):

		while (contador < len(enderecos_solicitados)):
			if (enderecos_solicitados[contador] in dados_cache):
				acertos += 1
			else:
				erros += 1
				if (None in dados_cache):
					dados_cache[dados_cache.index(None)] = enderecos_solicitados[contador]
				else:
					dados_cache.pop(0)
					dados_cache.append(enderecos_solicitados[contador])
			contador += 1

	if (tipo == "LRU"):

		while (contador < len(enderecos_solicitados)):
			if (enderecos_solicitados[contador] in dados_cache):
				acertos += 1
				aux = dados_cache.pop(dados_cache.index(int(enderecos_solicitados[contador])))
				dados_cache.insert(0, aux)
			else:
				erros += 1
				if (None in dados_cache):
					dados_cache[dados_cache.index(None)] = enderecos_solicitados[contador]
				else:
					dados_cache.pop()
					dados_cache.append(enderecos_solicitados[contador])
			contador += 1

	if (tipo == "LFU"):

		while (contador < len(enderecos_solicitados)):
			if (enderecos_solicitados[contador] in dados_cache):
				acertos += 1
				aux = dados_cache.pop(dados_cache.index(int(enderecos_solicitados[contador])))
				dados_cache.insert(0, aux)
			else:
				erros += 1
				if (None in dados_cache):
					dados_cache[dados_cache.index(None)] = enderecos_solicitados[contador]
				else:
					dados_cache.pop()
					dados_cache.append(enderecos_solicitados[contador])
			contador += 1
		'''
		# verificar se os enderecos solicitados ja estao na cache
		while (contador < len(enderecos_solicitados)):
			# se ja estiver dentro da cache
			if (int(enderecos_solicitados[contador]) in dados_cache):
				acertos += 1  # adiciona na variavel que aconteceu um cache hit
				aux = dados_cache.pop(dados_cache.index(int(enderecos_solicitados[contador])))
				dados_cache.reverse()
				dados_cache.append(aux)
				dados_cache.reverse()
			# se não estiver dentro da cache
			else:
				dados_cache.pop()
				dados_cache.append(enderecos_solicitados[
									   contador])  # substitui pelo novo valor de memoria que nao estava presente na cache
				erros += 1  # adiciona na variavel que aconteceu um cache miss
			contador += 1
		'''
	if (tipo == "RANDOM"):

		while (contador < len(enderecos_solicitados)):
			if (enderecos_solicitados[contador] in dados_cache):
				acertos += 1
			else:
				erros += 1
				if (None in dados_cache):
					dados_cache[dados_cache.index(None)] = enderecos_solicitados[contador]
				else:
					numero_aleatorio = random.randrange(tamanho_paginas_cache)
					dados_cache.pop(numero_aleatorio)
					dados_cache.insert(numero_aleatorio, enderecos_solicitados[contador])
			contador += 1

	print("Acertos: " + str(acertos))
	print("Erros: " + str(erros))
	status_cache()
	print


# mapeamento associativo direto
def mapeamento_associativo_conjuntos(enderecos_solicitados, tipo):
	status_cache()
	global acertos, erros
	acertos = 0
	erros = 0
	if (tipo == "FIFO"):
		print("fifo")
	if (tipo == "LRU"):
		print("fifo")
	if (tipo == "LFU"):
		print("fifo")
	if (tipo == "RANDOM"):
		print("fifo")
	print("Acertos: " + str(acertos))
	print("Erros: " + str(erros))
	status_cache()
	print


def abrir_arquivo_de_acessos_mp(nome):
	f = open(nome, "r")
	enderecos = f.readlines()
	f.close()
	return enderecos


def gerar_requisicoes_aleatorias(tamanho_requiscoes):
	return np.random.randint(low=0, high=tamanho_mp, size=tamanho_requiscoes)


def instancia_memoria_cache():
	dados_cache = np.empty((1, tamanho_paginas_cache), object)
	dados_cache = dados_cache[0]
	dados_cache = list(dados_cache)
	return dados_cache


def propriedades_memorias():
	print("O tamanho da cache é de " + str(len(dados_cache)) + " blocos")
	print("O tamanho da memoria principal é de " + str(tamanho_mp))
	print


def status_cache():
	print("dados da cache: " + str(dados_cache))


# print("O valor do quadro da primeira linha da cache: "+str(dados_cache[0]))
# print("O valor do quadro da ultima linha da cache: "+str(dados_cache[tamanho_paginas_cache-1]))

# ---------------------- Configuracoes ---------------------------
# recebe o tamanho da memoria cache (numero total de paginas)
tamanho_paginas_cache = 12
tamanho_mp = tamanho_paginas_cache * 100
dados_cache = instancia_memoria_cache()
propriedades_memorias()
# ----------------------------------------------------------------


# -------------------- Mapeamento direto -------------------------
'''
#teste mapeamento direto
#enderecos_memoria = abrir_arquivo_de_acessos_mp("acessos.txt")
enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache)
mapeamento_direto(enderecos_memoria)

#enderecos_memoria = abrir_arquivo_de_acessos_mp("acessos.txt")
mapeamento_direto(enderecos_memoria)
'''
# ----------------------------------------------------------------


# -------------------- Mapeamento Associativo -------------------------
# ------------------------------FIFO------------------------------------
'''
enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache)
mapeamento_associativo(enderecos_memoria, "FIFO")
#enderecos_memoria = gerar_requisicoes_aleatorias(5)
mapeamento_associativo(enderecos_memoria, "FIFO")
'''

# ----------------------------RANDOM------------------------------------
'''
enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache)
mapeamento_associativo(enderecos_memoria, "RANDOM")
enderecos_memoria = gerar_requisicoes_aleatorias(5)
mapeamento_associativo(enderecos_memoria, "RANDOM")
'''

# ------------------------------LRU------------------------------------
'''
enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache)
mapeamento_associativo(enderecos_memoria, "LRU")
enderecos_memoria = list([enderecos_memoria[3], enderecos_memoria[3], enderecos_memoria[3], enderecos_memoria[5], 1])
mapeamento_associativo(enderecos_memoria, "LRU")
'''

# ------------------------------LFU------------------------------------

dados_cache_frequencia = instancia_memoria_cache()
enderecos_memoria = gerar_requisicoes_aleatorias(tamanho_paginas_cache)
mapeamento_associativo(enderecos_memoria, "LFU")
enderecos_memoria = gerar_requisicoes_aleatorias(5)
mapeamento_associativo(enderecos_memoria, "LFU")

