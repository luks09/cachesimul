# memsimul
Simulador de substituição de memória cache

REQUISITOS:
-> Ter um Python instalado com versão abaixo da 3;

COMO EXECUTAR:
-> Basta clicar duas vezes no arquivo simulador_de_memoria_cache.py para executar o programa

TUTORIAL:
1 - Após os dois cliques no arquivo simulador_de_memoria_cache.py, uma janela surgirá com a mensagem "Digite o numero de paginas da cache: ", pedindo pra que o número de paginas da memória cache seja preenchido. O valor deve ser um inteiro;
2 - Depois de informar o número de paginas da cache, a seguinte mensagem aparecerá na tela:

//Digite o tipo de mapeamento: 
//
//1 - Mapeamento Direto
//2 - Mapeamento Associativo
//3 - Mapeamento Associativo por conjunto

    É necessário somente digitar o número respectivo ao mapeamento desejado;
3 - No caso de escolha do mapeamento direto, será necessário somente digitar o nome do arquivo que contem as requisições de endereços de memória. O nome do arquivo deve ser informado também com a sua extensão; Ex.: 'nome_do_arquivo.txt' 
4 - No caso de escolha do mapeamento associativo e associativo por conjunto, a seguinte mensagem aparecerá na tela:
Digite o algoritmo: 

//1 - FIFO
//2 - LRU
//3 - LFU
//4 - RANDOM

    É necessário somente digitar o número respectivo ao algoritmo desejado;
    
5 - No caso de escolha do mapeamento associativo por conjunto, após a escolha do algoritmo, uma mensagem aparecerá requisitando a informação do número de quadros por conjunto;
6 - Ao fim do preenchimento das informações, será executado o mapeamento escolhido na configuração informada. A cada solicitação, é apresentado o estado da cache, a solicitacao de endereco específica e também se aconteceu um cache-hit ou cache-miss. 
    
EXEMPLOS DE UTILIZAÇÃO:
*MAPEAMENTO DIRETO:

#----------------------------------------

Digite o numero de paginas da cache: 12
Digite o tipo de mapeamento: 

1 - Mapeamento Direto
2 - Mapeamento Associativo
3 - Mapeamento Associativo por conjunto

1

Digite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): acessos.txt
O tamanho da cache e de 12 paginas
O tamanho da memoria principal e de 1200

dados da cache: [None, None, None, None, None, None, None, None, None, None, None, None]
CACHE-MISS - Os dados do endereco 1000 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, None, None, None, 1000, None, None, None, None, None, None, None]
CACHE-MISS - Os dados do endereco 2476 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, None, None, None, 2476, None, None, None, None, None, None, None]
CACHE-MISS - Os dados do endereco 1209 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, None, None, None, 2476, None, None, None, None, 1209, None, None]
CACHE-MISS - Os dados do endereco 5782 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, None, None, None, 2476, None, None, None, None, 1209, 5782, None]
CACHE-MISS - Os dados do endereco 4738 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, None, None, None, 2476, None, None, None, None, 1209, 4738, None]
CACHE-MISS - Os dados do endereco 1629 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, None, None, None, 2476, None, None, None, None, 1629, 4738, None]
CACHE-MISS - Os dados do endereco 1826 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, None, 1826, None, 2476, None, None, None, None, 1629, 4738, None]
CACHE-MISS - Os dados do endereco 1023 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, None, 1826, 1023, 2476, None, None, None, None, 1629, 4738, None]
CACHE-MISS - Os dados do endereco 123989 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, None, 1826, 1023, 2476, 123989, None, None, None, 1629, 4738, None]
CACHE-MISS - Os dados do endereco 726481 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, 726481, 1826, 1023, 2476, 123989, None, None, None, 1629, 4738, None]
CACHE-MISS - Os dados do endereco 152805 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, 726481, 1826, 1023, 2476, 123989, None, None, None, 152805, 4738, None]
CACHE-MISS - Os dados do endereco 128739 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, 726481, 1826, 128739, 2476, 123989, None, None, None, 152805, 4738, None]
CACHE-MISS - Os dados do endereco 752935 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, 726481, 1826, 128739, 2476, 123989, None, 752935, None, 152805, 4738, None]
CACHE-HIT - Os dados do endereco 752935 da memoria ja estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [None, 726481, 1826, 128739, 2476, 123989, None, 752935, None, 152805, 4738, None]
CACHE-MISS - Os dados do endereco 0 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [0, 726481, 1826, 128739, 2476, 123989, None, 752935, None, 152805, 4738, None]
CACHE-MISS - Os dados do endereco 1000 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [0, 726481, 1826, 128739, 1000, 123989, None, 752935, None, 152805, 4738, None]
CACHE-MISS - Os dados do endereco 2476 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [0, 726481, 1826, 128739, 2476, 123989, None, 752935, None, 152805, 4738, None]
CACHE-MISS - Os dados do endereco 1209 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [0, 726481, 1826, 128739, 2476, 123989, None, 752935, None, 1209, 4738, None]
CACHE-MISS - Os dados do endereco 5782 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [0, 726481, 1826, 128739, 2476, 123989, None, 752935, None, 1209, 5782, None]
CACHE-MISS - Os dados do endereco 4738 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [0, 726481, 1826, 128739, 2476, 123989, None, 752935, None, 1209, 4738, None]
CACHE-MISS - Os dados do endereco 1629 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [0, 726481, 1826, 128739, 2476, 123989, None, 752935, None, 1629, 4738, None]
CACHE-HIT - Os dados do endereco 1826 da memoria ja estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [0, 726481, 1826, 128739, 2476, 123989, None, 752935, None, 1629, 4738, None]
CACHE-MISS - Os dados do endereco 1023 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [0, 726481, 1826, 1023, 2476, 123989, None, 752935, None, 1629, 4738, None]
Fracao de acertos: 8.696 %
dados da cache: [0, 726481, 1826, 1023, 2476, 123989, None, 752935, None, 1629, 4738, None]

Pressione qualquer tecla para finalizar

#----------------------------------------

*MAPEAMENTO ASSOCIATIVO:

- FIFO:
#----------------------------------------

Digite o numero de paginas da cache: 12
Digite o tipo de mapeamento: 

1 - Mapeamento Direto
2 - Mapeamento Associativo
3 - Mapeamento Associativo por conjunto

2

Digite o algoritmo: 

1 - FIFO
2 - LRU
3 - LFU
4 - RANDOM

1

Digite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): acessos.txt
O tamanho da cache e de 12 paginas
O tamanho da memoria principal e de 1200

dados da cache: [None, None, None, None, None, None, None, None, None, None, None, None]
CACHE-MISS - Os dados do endereco 1000 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, None, None, None, None, None, None, None, None, None, None, None]
CACHE-MISS - Os dados do endereco 2476 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, 2476, None, None, None, None, None, None, None, None, None, None]
CACHE-MISS - Os dados do endereco 1209 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, 2476, 1209, None, None, None, None, None, None, None, None, None]
CACHE-MISS - Os dados do endereco 5782 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, 2476, 1209, 5782, None, None, None, None, None, None, None, None]
CACHE-MISS - Os dados do endereco 4738 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, 2476, 1209, 5782, 4738, None, None, None, None, None, None, None]
CACHE-MISS - Os dados do endereco 1629 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, 2476, 1209, 5782, 4738, 1629, None, None, None, None, None, None]
CACHE-MISS - Os dados do endereco 1826 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, 2476, 1209, 5782, 4738, 1629, 1826, None, None, None, None, None]
CACHE-MISS - Os dados do endereco 1023 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, 2476, 1209, 5782, 4738, 1629, 1826, 1023, None, None, None, None]
CACHE-MISS - Os dados do endereco 123989 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, 2476, 1209, 5782, 4738, 1629, 1826, 1023, 123989, None, None, None]
CACHE-MISS - Os dados do endereco 726481 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, 2476, 1209, 5782, 4738, 1629, 1826, 1023, 123989, 726481, None, None]
CACHE-MISS - Os dados do endereco 152805 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, 2476, 1209, 5782, 4738, 1629, 1826, 1023, 123989, 726481, 152805, None]
CACHE-MISS - Os dados do endereco 128739 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1000, 2476, 1209, 5782, 4738, 1629, 1826, 1023, 123989, 726481, 152805, 128739]
CACHE-MISS - Os dados do endereco 752935 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [2476, 1209, 5782, 4738, 1629, 1826, 1023, 123989, 726481, 152805, 128739, 752935]
CACHE-HIT - Os dados do endereco 752935 da memoria ja estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [2476, 1209, 5782, 4738, 1629, 1826, 1023, 123989, 726481, 152805, 128739, 752935]
CACHE-MISS - Os dados do endereco 0 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1209, 5782, 4738, 1629, 1826, 1023, 123989, 726481, 152805, 128739, 752935, 0]
CACHE-MISS - Os dados do endereco 1000 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [5782, 4738, 1629, 1826, 1023, 123989, 726481, 152805, 128739, 752935, 0, 1000]
CACHE-MISS - Os dados do endereco 2476 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [4738, 1629, 1826, 1023, 123989, 726481, 152805, 128739, 752935, 0, 1000, 2476]
CACHE-MISS - Os dados do endereco 1209 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1629, 1826, 1023, 123989, 726481, 152805, 128739, 752935, 0, 1000, 2476, 1209]
CACHE-MISS - Os dados do endereco 5782 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1826, 1023, 123989, 726481, 152805, 128739, 752935, 0, 1000, 2476, 1209, 5782]
CACHE-MISS - Os dados do endereco 4738 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [1023, 123989, 726481, 152805, 128739, 752935, 0, 1000, 2476, 1209, 5782, 4738]
CACHE-MISS - Os dados do endereco 1629 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [123989, 726481, 152805, 128739, 752935, 0, 1000, 2476, 1209, 5782, 4738, 1629]
CACHE-MISS - Os dados do endereco 1826 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [726481, 152805, 128739, 752935, 0, 1000, 2476, 1209, 5782, 4738, 1629, 1826]
CACHE-MISS - Os dados do endereco 1023 da memoria nao estavam na memoria cache
paginas armazenadas na memoria cache apos a operacao: [152805, 128739, 752935, 0, 1000, 2476, 1209, 5782, 4738, 1629, 1826, 1023]
Fracao de acertos: 4.348 %
dados da cache: [152805, 128739, 752935, 0, 1000, 2476, 1209, 5782, 4738, 1629, 1826, 1023]

Pressione qualquer tecla para finalizar

#----------------------------------------

- LRU:

#----------------------------------------



#----------------------------------------

- LFU:

*MAPEAMENTO ASSOCIATIVO POR CONJUNTO:
