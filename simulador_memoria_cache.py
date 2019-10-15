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
from os import system, name
import random
import sys

acertos = 0
erros = 0


# mapeamento direto
def mapeamento_direto(enderecos_solicitados):
	status_cache()
	global acertos, erros
	acertos = 0
	erros = 0
	for endereco in enderecos_solicitados:
		status_operacao(int(endereco))
		if (int(endereco) == dados_cache[int(endereco) % tamanho_paginas_cache]):
			print "CACHE-HIT - Os dados do endereco %d da memoria principal ja estavam na memoria cache" % int(endereco)
			acertos += 1
		else:
			print "CACHE-MISS - Os dados do endereco %d da memoria principal nao estavam na memoria cache" % int(endereco)
			dados_cache[int(endereco) % tamanho_paginas_cache] = int(endereco)
			erros += 1
		status_cache_operacoes()
	fracao_acertos()
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

		contador_fifo = 0

		while (contador < len(enderecos_solicitados)):
			status_operacao(enderecos_solicitados[contador])
			if (enderecos_solicitados[contador] in dados_cache):
				print "CACHE-HIT - Os dados do endereco %d da memoria principal ja estavam na memoria cache" % enderecos_solicitados[contador]
				acertos += 1
			else:
				print "CACHE-MISS - Os dados do endereco %d da memoria principal nao estavam na memoria cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache):
					dados_cache[dados_cache.index(None)] = enderecos_solicitados[contador]
				else:
					dados_cache.pop(contador_fifo)
					dados_cache.insert(contador_fifo, enderecos_solicitados[contador])
					contador_fifo += 1
					if (contador_fifo == len(dados_cache)):
						contador_fifo = 0
			contador += 1
			status_cache_operacoes()

	if (tipo == "LRU"):

		while (contador < len(enderecos_solicitados)):
			status_operacao(enderecos_solicitados[contador])

			if (enderecos_solicitados[contador] in dados_cache):
				print "CACHE-HIT - Os dados do endereco %d da memoria principal ja estavam na memoria cache" % enderecos_solicitados[contador]
				acertos += 1
				aux = dados_cache_recencia.pop(dados_cache_recencia.index(int(enderecos_solicitados[contador])))
				dados_cache_recencia.insert(0, aux)
			else:
				print "CACHE-MISS - Os dados do endereco %d da memoria principal nao estavam na memoria cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache):
					dados_cache[dados_cache.index(None)] = enderecos_solicitados[contador]
					dados_cache_recencia.insert(0,enderecos_solicitados[contador])
					dados_cache_recencia.pop()
				else:
					index = dados_cache.index(dados_cache_recencia.pop())
					dados_cache.pop(index)
					dados_cache.insert(index,enderecos_solicitados[contador])
					dados_cache_recencia.insert(0,enderecos_solicitados[contador])
			contador += 1
			status_cache_operacoes()

	if (tipo == "LFU"):

		while (contador < len(enderecos_solicitados)):
			status_operacao(enderecos_solicitados[contador])
			if (enderecos_solicitados[contador] in dados_cache):
				print "CACHE-HIT - Os dados do endereco %d da memoria principal ja estavam na memoria cache" % enderecos_solicitados[contador]
				acertos += 1
				dados_cache_frequencia[dados_cache.index(int(enderecos_solicitados[contador]))] += 1
			else:
				print "CACHE-MISS - Os dados do endereco %d da memoria principal nao estavam na memoria cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache):
					dados_cache_frequencia[dados_cache.index(None)] = 1
					dados_cache[dados_cache.index(None)] = enderecos_solicitados[contador]
				else:
					index = dados_cache_frequencia.index(min(dados_cache_frequencia))
					dados_cache.pop(index)
					dados_cache.insert(index, enderecos_solicitados[contador])
					dados_cache_frequencia[index] = 1
			contador += 1
			status_cache_operacoes()

	if (tipo == "RANDOM"):

		while (contador < len(enderecos_solicitados)):
			status_operacao(enderecos_solicitados[contador])
			if (enderecos_solicitados[contador] in dados_cache):
				print "CACHE-HIT - Os dados do endereco %d da memoria principal ja estavam na memoria cache" % enderecos_solicitados[contador]
				acertos += 1
			else:
				print "CACHE-MISS - Os dados do endereco %d da memoria principal nao estavam na memoria cache" % enderecos_solicitados[contador]
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

		contador_fifo = [0]*(tamanho_paginas_cache/tamanho_quadro)

		while (contador < len(enderecos_solicitados)):
			status_operacao(enderecos_solicitados[contador])
			conjunto = enderecos_solicitados[contador] % (tamanho_paginas_cache/tamanho_quadro)
			if (enderecos_solicitados[contador] in dados_cache[conjunto*tamanho_quadro:(conjunto+1)*tamanho_quadro]):
				print "CACHE-HIT - Os dados do endereco %d da memoria principal ja estavam na memoria cache" % enderecos_solicitados[contador]
				acertos += 1
			else:
				print "CACHE-MISS - Os dados do endereco %d da memoria principal nao estavam na memoria cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache[conjunto*tamanho_quadro:(conjunto+1)*tamanho_quadro]):
					dados_cache[conjunto*tamanho_quadro+dados_cache[conjunto*tamanho_quadro:(conjunto+1)*tamanho_quadro].index(None)] = enderecos_solicitados[contador]
				else:
					dados_cache.pop(conjunto*tamanho_quadro+contador_fifo[conjunto])
					dados_cache.insert(conjunto*tamanho_quadro+contador_fifo[conjunto],enderecos_solicitados[contador])
					contador_fifo[conjunto] += 1

					if (contador_fifo[conjunto] == tamanho_quadro):
						contador_fifo[conjunto] = 0
			contador += 1
			status_cache_operacoes()

	if (tipo == "LRU"):

		while (contador < len(enderecos_solicitados)):
			status_operacao(enderecos_solicitados[contador])

			conjunto = enderecos_solicitados[contador] % (tamanho_paginas_cache/tamanho_quadro)
			if (enderecos_solicitados[contador] in dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro]):
				print "CACHE-HIT - Os dados do endereco %d da memoria principal ja estavam na memoria cache" % enderecos_solicitados[contador]
				acertos += 1
				aux = dados_cache_recencia.pop(dados_cache_recencia.index(int(enderecos_solicitados[contador])))
				dados_cache_recencia.insert(conjunto * tamanho_quadro, aux)
			else:
				print "CACHE-MISS - Os dados do endereco %d da memoria principal nao estavam na memoria cache" % enderecos_solicitados[contador]
				erros += 1
				if (None in dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro]):
					dados_cache[conjunto * tamanho_quadro + dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro].index(None)] = enderecos_solicitados[contador]
					dados_cache_recencia.insert(conjunto * tamanho_quadro, enderecos_solicitados[contador])
					dados_cache_recencia.pop((conjunto + 1) * tamanho_quadro)
				else:
					index = dados_cache.index(dados_cache_recencia.pop((conjunto + 1) * tamanho_quadro - 1))
					dados_cache.pop(index)
					dados_cache.insert(index,enderecos_solicitados[contador])
					dados_cache_recencia.insert(conjunto * tamanho_quadro, enderecos_solicitados[contador])
			contador += 1
			status_cache_operacoes()

	if (tipo == "LFU"):

		while (contador < len(enderecos_solicitados)):
			status_operacao(enderecos_solicitados[contador])
			conjunto = enderecos_solicitados[contador] % (tamanho_paginas_cache/tamanho_quadro)

			if (enderecos_solicitados[contador] in dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro]):
				print "CACHE-HIT - Os dados do endereco %d da memoria principal ja estavam na memoria cache" % enderecos_solicitados[contador]
				acertos += 1
				dados_cache_frequencia[dados_cache.index(int(enderecos_solicitados[contador]))] += 1
			else:
				print "CACHE-MISS - Os dados do endereco %d da memoria principal nao estavam na memoria cache" % enderecos_solicitados[contador]
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
			status_operacao(enderecos_solicitados[contador])
			conjunto = enderecos_solicitados[contador] % (tamanho_paginas_cache/tamanho_quadro)
			if (enderecos_solicitados[contador] in dados_cache[conjunto * tamanho_quadro:(conjunto + 1) * tamanho_quadro]):
				print "CACHE-HIT - Os dados do endereco %d da memoria principal ja estavam na memoria cache" % enderecos_solicitados[contador]
				acertos += 1
				aux = dados_cache.pop(dados_cache.index(int(enderecos_solicitados[contador])))
				dados_cache.insert(conjunto * tamanho_quadro, aux)
			else:
				print "CACHE-MISS - Os dados do endereco %d da memoria principal nao estavam na memoria cache" % enderecos_solicitados[contador]
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
	print


def abrir_arquivo_de_acessos_mp(nome):
	try:
		f = open(nome, "r")
		enderecos = f.readlines()
		f.close()
		return enderecos
	except:
		return False


def status_arquivo_de_acessos_mp(enderecos):
	print len(enderecos)


def limpa_tela():
	# windows
	if name == 'nt':
		_ = system('cls')

	# mac e linux
	else:
		_ = system('clear')

	#def gerar_requisicoes_aleatorias(tamanho_requisicoes):
#	return np.random.randint(low=0, high=tamanho_paginas_cache*3, size=tamanho_requisicoes)


def instancia_memoria_cache(inicial=None):
	#dados_cache = np.empty((1, tamanho_paginas_cache), object)
	#dados_cache = dados_cache[0]
	#dados_cache = list(dados_cache)
	if (inicial == None or inicial==0):
		dados = [inicial]*tamanho_paginas_cache
	else:
		dados = list(inicial)
	return dados


def propriedades_memoria():
	print("O tamanho da cache e de " + str(len(dados_cache)) + " paginas")
	print


def status_cache():
	maximo = max(dados_cache)
	if (maximo == None):
		maximo = 0
	digitos = len(str(maximo))
	print("\nDados da cache: ")
	for i in range(tamanho_paginas_cache):
		if (i%tamanho_quadro==0 or tipo_mapeamento == 1):
			if (i != 0):
				sys.stdout.write("|")
			print
		sys.stdout.write("| ")
		if (dados_cache[i] == None):
			valor = '-'
		else:
			valor = dados_cache[i]
		espaco = digitos - len(str(valor))
		for espaco_branco in range(espaco+1):
			sys.stdout.write(" ")
		sys.stdout.write(str(valor)+" ")
	sys.stdout.write("| \n\n")


def fracao_acertos():
	print("CACHE-HITS: " + str(acertos))
	print("CACHE-MISSES: " + str(erros))
	print "FRACAO DE CACHE-HITS: %.2f %%" %((acertos/float((erros+acertos)))*100)


def status_cache_operacoes():
	print("Dados da cache apos a solicitacao: ")
	maximo = max(dados_cache)
	if (maximo == None):
		maximo = 0
	digitos = len(str(maximo))
	for i in range(tamanho_paginas_cache):
		if (i%tamanho_quadro==0 or tipo_mapeamento == 1):
			if (i != 0):
				sys.stdout.write("|")
			print

		sys.stdout.write("| ")
		if (dados_cache[i] == None):
			valor = '-'
		else:
			valor = dados_cache[i]
		espaco = digitos - len(str(valor))
		for espaco_branco in range(espaco+1):
			sys.stdout.write(" ")
		sys.stdout.write(str(valor)+" ")
	sys.stdout.write("| \n\n")


def status_operacao(endereco):
	print("Dados do endereco %d da memoria principal foram solicitados!"%endereco)

recomecar = "sim"
num_conjuntos = 1
num_conjuntos_ant = 0
while (str.lower(recomecar) == "sim" or str.lower(recomecar).replace(" ","") == "sim-naozerarcache"):

	if str.lower(recomecar).replace(" ", "") == "sim":
		limpa_tela()
		tamanho_paginas_cache = 0
		tamanho_quadro = 0
		dados_cache = instancia_memoria_cache()
		dados_cache_recencia = instancia_memoria_cache()
		dados_cache_frequencia = instancia_memoria_cache()
	else:
		tipo = ""
		tipo_mapeamento = ""

	print "-------------CACHESIMUL-------------"
	print "----Simulador de memoria Cache----\n"

	# ---------------------- Configuracoes ---------------------------

	if (recomecar == "sim"):
		tamanho_paginas_cache = raw_input("Digite o numero de paginas da cache: ")
		try:
			tamanho_paginas_cache = int(tamanho_paginas_cache)
		except:
			tamanho_paginas_cache = 0
		while (tamanho_paginas_cache<=0):
			tamanho_paginas_cache = raw_input("Numero de paginas incorreto! Digite o numero de paginas da cache: ")
			try:
				tamanho_paginas_cache = int(tamanho_paginas_cache)
			except:
				tamanho_paginas_cache = 0
		tamanho_quadro = tamanho_paginas_cache
	tipo_mapeamento = raw_input("Digite o tipo de mapeamento: \n\n1 - Mapeamento Direto\n2 - Mapeamento Associativo\n3 - Mapeamento Associativo por conjunto\n\n")
	try:
		tipo_mapeamento = int(tipo_mapeamento)
	except:
		print
	while (tipo_mapeamento != 1 and tipo_mapeamento != 2 and tipo_mapeamento != 3):
		tipo_mapeamento = raw_input("Valor incorreto!\n\nDigite o tipo de mapeamento: \n\n1 - Mapeamento Direto\n2 - Mapeamento Associativo\n3 - Mapeamento Associativo\n\n")
		try:
			tipo_mapeamento = int(tipo_mapeamento)
		except:
			print

	if (tipo_mapeamento == 2 or tipo_mapeamento == 3):
		tipo = raw_input("\nDigite o algoritmo: \n\n1 - FIFO\n2 - LRU\n3 - LFU\n4 - RANDOM\n\n")
		try:
			tipo = int(tipo)
		except:
			print
		while (tipo != 1 and tipo != 2 and tipo != 3 and tipo != 4):
			tipo = raw_input("\nDigite o algoritmo: \n\n1 - FIFO\n2 - LRU\n3 - LFU\n4 - RANDOM\n\n")
			try:
				tipo = int(tipo)
			except:
				print

		if (tipo_mapeamento == 3):
			try:
				num_conjuntos = raw_input("\nDigite a quantidade de conjuntos: ")
				num_conjuntos = int(num_conjuntos)
				if (num_conjuntos == 0):
					num_conjuntos = -1
			except:
				num_conjuntos = -1

			while (num_conjuntos < 0 or tamanho_paginas_cache%num_conjuntos != 0):
				try:
					num_conjuntos = raw_input("\nNumero de conjuntos nao multiplo do numero de paginas da memoria cache! Digite novamente a quantidade de conjuntos: ")
					num_conjuntos = int(num_conjuntos)
					if (num_conjuntos == 0):
						num_conjuntos = -1
				except:
					num_conjuntos = -1

			tamanho_quadro = tamanho_paginas_cache/num_conjuntos
	arquivo_entrada = raw_input("\nDigite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): ")
	enderecos_memoria = abrir_arquivo_de_acessos_mp(arquivo_entrada)
	while (enderecos_memoria == False):
		arquivo_entrada = raw_input("\nArquivo nao encontrado! Digite o nome do arquivo de entrada novamente: ")
		enderecos_memoria = abrir_arquivo_de_acessos_mp(arquivo_entrada)

	tamanho_mp = tamanho_paginas_cache * 100

	if (recomecar == "sim"):
		dados_cache = instancia_memoria_cache()
	propriedades_memoria()
	# ----------------------------------------------------------------

	#arquivo_entrada = raw_input("\nDigite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): ")

	# -------------------- Mapeamento direto -------------------------
	if (tipo_mapeamento == 1):
		mapeamento_direto(enderecos_memoria)


	# -------------------- Mapeamento Associativo -------------------------
	if (tipo_mapeamento == 2):
		# ------------------------------FIFO------------------------------------

		if (tipo == 1):
			mapeamento_associativo(enderecos_memoria, "FIFO")
			if dados_cache_frequencia:
					del dados_cache_frequencia
			if dados_cache_recencia:
					del dados_cache_recencia

		# ------------------------------LRU------------------------------------
		if (tipo == 2):
			if (recomecar == "sim"):
				dados_cache_recencia = instancia_memoria_cache()
			elif not dados_cache_recencia or num_conjuntos != num_conjuntos_ant:
				dados_cache_recencia = instancia_memoria_cache(inicial=dados_cache)
				if dados_cache_frequencia:
					del dados_cache_frequencia
			mapeamento_associativo(enderecos_memoria, "LRU")

		# ------------------------------LFU------------------------------------
		if (tipo == 3):
			if (recomecar == "sim"):
				dados_cache_frequencia = instancia_memoria_cache()
			elif not dados_cache_frequencia:
				dados_cache_frequencia = instancia_memoria_cache(inicial=0)
				if dados_cache_recencia:
					del dados_cache_recencia
			mapeamento_associativo(enderecos_memoria, "LFU")

		# ----------------------------RANDOM------------------------------------
		if (tipo == 4):
			mapeamento_associativo(enderecos_memoria, "RANDOM")

	# ------------- Mapeamento Associativo por conjunto --------------------
	if (tipo_mapeamento == 3):
		# ------------------------------FIFO------------------------------------
		if (tipo == 1):
			mapeamento_associativo_conjuntos(enderecos_memoria, "FIFO")

		# ------------------------------LRU------------------------------------
		if (tipo == 2):
			if (recomecar == "sim"):
				dados_cache_recencia = instancia_memoria_cache()
			elif not dados_cache_recencia or num_conjuntos != num_conjuntos_ant:
				dados_cache_recencia = instancia_memoria_cache(inicial=dados_cache)
				if dados_cache_frequencia:
					del dados_cache_frequencia
			mapeamento_associativo_conjuntos(enderecos_memoria, "LRU")

		# ------------------------------LFU------------------------------------
		if (tipo == 3):
			if (recomecar == "sim"):
				dados_cache_frequencia = instancia_memoria_cache()
			elif not dados_cache_frequencia:
				dados_cache_frequencia = instancia_memoria_cache(inicial=0)
				if dados_cache_recencia:
					del dados_cache_recencia
			mapeamento_associativo_conjuntos(enderecos_memoria, "LFU")

		# ----------------------------RANDOM------------------------------------
		if (tipo == 4):
			mapeamento_associativo_conjuntos(enderecos_memoria, "RANDOM")

	num_conjuntos_ant = num_conjuntos
	recomecar = raw_input("\nDeseja executar o programa novamente (sim/ nao) *ARGUMENTO: -naozerarcache): ")
	print
	while (str.lower(recomecar) != "sim" and str(recomecar) != "nao" and str.lower(recomecar).replace(" ","") != "sim-naozerarcache"):
		recomecar = raw_input("\nErro de comando! Deseja executar o programa novamente (sim/ nao) *ARGUMENTO: -naozerarcache: ")
		print

print
raw_input("Pressione qualquer tecla para finalizar")