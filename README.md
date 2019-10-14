# cachesimul

## Simulador de substituição de memória cache

### REQUISITOS:

-> Python versão 2.7 instalado;

### COMO EXECUTAR:

-> Basta clicar duas vezes no arquivo simulador_de_memoria_cache.py para executar o programa

### TUTORIAL:

1. Após os dois cliques no arquivo simulador_de_memoria_cache.py, uma janela surgirá com a mensagem "Digite o numero de paginas da cache: ", pedindo pra que o número de paginas da memória cache seja preenchido. O valor deve ser um inteiro;

2. Depois de informar o número de paginas da cache, a seguinte mensagem aparecerá na tela:

//Digite o tipo de mapeamento: 

//

//1 - Mapeamento Direto

//2 - Mapeamento Associativo

//3 - Mapeamento Associativo por conjunto

    É necessário somente digitar o número respectivo ao mapeamento desejado;
3. No caso de escolha do mapeamento direto, será necessário somente digitar o nome do arquivo que contem as requisições de endereços de memória. O nome do arquivo deve ser informado também com a sua extensão; Ex.: 'nome_do_arquivo.txt' 

4. No caso de escolha do mapeamento associativo e associativo por conjunto, a seguinte mensagem aparecerá na tela:
Digite o algoritmo: 

//1 - FIFO

//2 - LRU

//3 - LFU

//4 - RANDOM

    É necessário somente digitar o número respectivo ao algoritmo desejado;
    
5. No caso de escolha do mapeamento associativo por conjunto, após a escolha do algoritmo, uma mensagem aparecerá requisitando a informação do número de quadros por conjunto;

6. Ao fim do preenchimento das informações, será executado o mapeamento escolhido na configuração informada. A cada solicitação, é apresentado o estado da cache, a solicitacao de endereco específica e também se aconteceu um cache-hit ou cache-miss. 
    
### EXEMPLOS DE UTILIZAÇÃO:

acessos.txt:

#----------------------------------------

0

1

2

3

4

3

2

1

5

8

6

10

2

1

#----------------------------------------

#### *MAPEAMENTO DIRETO:

#----------------------------------------

-------------CACHESIMUL-------------

----Simulador de memória Cache----



Digite o numero de paginas da cache: 4

Digite o tipo de mapeamento: 



1 - Mapeamento Direto

2 - Mapeamento Associativo

3 - Mapeamento Associativo por conjunto



1



Digite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): acessos.txt

O tamanho da cache e de 4 paginas





Dados da cache: 



|     - |

|     - |

|     - |

|     - | 



Dados do endereco 0 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 0 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |

|  - |

|  - |

|  - | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |

|  1 |

|  - |

|  - | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |

|  1 |

|  2 |

|  - | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 3 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |

|  1 |

|  2 |

|  3 | 



Dados do endereco 4 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 4 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |

|  1 |

|  2 |

|  3 | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 3 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |

|  1 |

|  2 |

|  3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 2 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |

|  1 |

|  2 |

|  3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 1 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |

|  1 |

|  2 |

|  3 | 



Dados do endereco 5 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 5 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |

|  5 |

|  2 |

|  3 | 



Dados do endereco 8 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 8 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  8 |

|  5 |

|  2 |

|  3 | 



Dados do endereco 6 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 6 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  8 |

|  5 |

|  6 |

|  3 | 



Dados do endereco 10 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 10 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|   8 |

|   5 |

|  10 |

|   3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  8 |

|  5 |

|  2 |

|  3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  8 |

|  1 |

|  2 |

|  3 | 



CACHE-HITS: 3

CACHE-MISSES: 11

FRACAO DE CACHE-HITS: 21.43 %



Deseja executar o programa novamente (SIM/ NAO) (OPÇÕES: -naozerarcache): nao

Pressione qualquer tecla para finalizar


#----------------------------------------

#### *MAPEAMENTO ASSOCIATIVO:

##### FIFO:

#----------------------------------------

-------------CACHESIMUL-------------

----Simulador de memória Cache----



Digite o numero de paginas da cache: 4

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

O tamanho da cache e de 4 paginas





Dados da cache: 



|     - |     - |     - |     - | 



Dados do endereco 0 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 0 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |  - |  - | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  - |  - | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  2 |  - | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 3 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  2 |  3 | 



Dados do endereco 4 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 4 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 3 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 2 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 1 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 5 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 5 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  5 |  2 |  3 | 



Dados do endereco 8 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 8 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  5 |  8 |  3 | 



Dados do endereco 6 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 6 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  5 |  8 |  6 | 



Dados do endereco 10 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 10 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   5 |   8 |   6 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   2 |   8 |   6 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   2 |   1 |   6 | 



CACHE-HITS: 3

CACHE-MISSES: 11

FRACAO DE CACHE-HITS: 21.43 %



Deseja executar o programa novamente (SIM/ NAO) (OPÇÕES: -naozerarcache): nao

Pressione qualquer tecla para finalizar

#----------------------------------------

##### LRU:

#----------------------------------------

-------------CACHESIMUL-------------

----Simulador de memória Cache----



Digite o numero de paginas da cache: 4

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



2



Digite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): acessos.txt

O tamanho da cache e de 4 paginas





Dados da cache: 



|     - |     - |     - |     - | 



Dados do endereco 0 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 0 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |  - |  - | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  - |  - | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  2 |  - | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 3 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  2 |  3 | 



Dados do endereco 4 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 4 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 3 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 2 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 1 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 5 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 5 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  5 |  1 |  2 |  3 | 



Dados do endereco 8 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 8 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  5 |  1 |  2 |  8 | 



Dados do endereco 6 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 6 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  5 |  1 |  6 |  8 | 



Dados do endereco 10 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 10 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|   5 |  10 |   6 |   8 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|   2 |  10 |   6 |   8 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|   2 |  10 |   6 |   1 | 



CACHE-HITS: 3

CACHE-MISSES: 11

FRACAO DE CACHE-HITS: 21.43 %



Deseja executar o programa novamente (SIM/ NAO) (OPÇÕES: -naozerarcache): nao

Pressione qualquer tecla para finalizar

#----------------------------------------

##### LFU:

#----------------------------------------

-------------CACHESIMUL-------------

----Simulador de memória Cache----



Digite o numero de paginas da cache: 4

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



3



Digite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): acessos.txt

O tamanho da cache e de 4 paginas





Dados da cache: 



|     - |     - |     - |     - | 



Dados do endereco 0 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 0 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |  - |  - | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  - |  - | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  2 |  - | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 3 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  2 |  3 | 



Dados do endereco 4 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 4 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 3 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 2 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 1 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  1 |  2 |  3 | 



Dados do endereco 5 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 5 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  5 |  1 |  2 |  3 | 



Dados do endereco 8 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 8 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  8 |  1 |  2 |  3 | 



Dados do endereco 6 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 6 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  6 |  1 |  2 |  3 | 



Dados do endereco 10 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 10 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   1 |   2 |   3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 2 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   1 |   2 |   3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 1 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   1 |   2 |   3 | 



CACHE-HITS: 5

CACHE-MISSES: 9

FRACAO DE CACHE-HITS: 35.71 %



Deseja executar o programa novamente (SIM/ NAO) (OPÇÕES: -naozerarcache): nao

Pressione qualquer tecla para finalizar

#----------------------------------------

##### RANDOM:

#----------------------------------------

-------------CACHESIMUL-------------

----Simulador de memória Cache----



Digite o numero de paginas da cache: 4

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



4



Digite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): acessos.txt

O tamanho da cache e de 4 paginas





Dados da cache: 



|     - |     - |     - |     - | 



Dados do endereco 0 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 0 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |  - |  - | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  - |  - | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  2 |  - | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 3 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  2 |  3 | 



Dados do endereco 4 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 4 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  4 |  3 | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 3 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  4 |  3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  2 |  3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 1 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  1 |  2 |  3 | 



Dados do endereco 5 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 5 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  5 |  2 |  3 | 



Dados do endereco 8 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 8 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  5 |  8 |  3 | 



Dados do endereco 6 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 6 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  5 |  6 |  3 | 



Dados do endereco 10 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 10 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|   0 |   5 |  10 |   3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  5 |  2 |  3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  5 |  2 |  1 | 



CACHE-HITS: 2

CACHE-MISSES: 12

FRACAO DE CACHE-HITS: 14.29 %



Deseja executar o programa novamente (SIM/ NAO) (OPÇÕES: -naozerarcache): nao

Pressione qualquer tecla para finalizar

#----------------------------------------

#### *MAPEAMENTO ASSOCIATIVO POR CONJUNTO:

##### FIFO:

#----------------------------------------


-------------CACHESIMUL-------------

----Simulador de memoria Cache----



Digite o numero de paginas da cache: 4

Digite o tipo de mapeamento: 



1 - Mapeamento Direto

2 - Mapeamento Associativo

3 - Mapeamento Associativo por conjunto



3



Digite o algoritmo: 



1 - FIFO

2 - LRU

3 - LFU

4 - RANDOM



1



Digite a quantidade de conjuntos: 2



Digite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): acessos.txt

O tamanho da cache e de 4 paginas





Dados da cache: 



|  - |  - |

|  - |  - | 



Dados do endereco 0 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 0 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |

|  - |  - | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |

|  1 |  - | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  2 |

|  1 |  - | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 3 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  2 |

|  1 |  3 | 



Dados do endereco 4 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 4 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 3 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 2 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 1 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 5 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 5 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  5 |  3 | 



Dados do endereco 8 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 8 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  8 |

|  5 |  3 | 



Dados do endereco 6 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 6 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  6 |  8 |

|  5 |  3 | 



Dados do endereco 10 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 10 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|   6 |  10 |

|   5 |   3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|   2 |  10 |

|   5 |   3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|   2 |  10 |

|   5 |   1 | 



CACHE-HITS: 3

CACHE-MISSES: 11

FRACAO DE CACHE-HITS: 21.43 %



Deseja executar o programa novamente (SIM/ NAO) (OPÇÕES: -naozerarcache): nao

Pressione qualquer tecla para finalizar

#----------------------------------------

##### LRU:

#----------------------------------------


-------------CACHESIMUL-------------

----Simulador de memoria Cache----



Digite o numero de paginas da cache: 4

Digite o tipo de mapeamento: 



1 - Mapeamento Direto

2 - Mapeamento Associativo

3 - Mapeamento Associativo por conjunto



3



Digite o algoritmo: 



1 - FIFO

2 - LRU

3 - LFU

4 - RANDOM



2



Digite a quantidade de conjuntos: 2



Digite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): acessos.txt

O tamanho da cache e de 4 paginas





Dados da cache: 



|  - |  - |

|  - |  - | 



Dados do endereco 0 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 0 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |

|  - |  - | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |

|  1 |  - | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  2 |

|  1 |  - | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 3 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  2 |

|  1 |  3 | 



Dados do endereco 4 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 4 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 3 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 2 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 1 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 5 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 5 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  5 | 



Dados do endereco 8 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 8 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  8 |  2 |

|  1 |  5 | 



Dados do endereco 6 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 6 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  8 |  6 |

|  1 |  5 | 



Dados do endereco 10 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 10 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   6 |

|   1 |   5 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   2 |

|   1 |   5 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 1 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   2 |

|   1 |   5 | 



CACHE-HITS: 4

CACHE-MISSES: 10

FRACAO DE CACHE-HITS: 28.57 %



Deseja executar o programa novamente (SIM/ NAO) (OPÇÕES: -naozerarcache): nao

Pressione qualquer tecla para finalizar

#----------------------------------------

##### LFU:

#----------------------------------------


-------------CACHESIMUL-------------

----Simulador de memoria Cache----



Digite o numero de paginas da cache: 4

Digite o tipo de mapeamento: 



1 - Mapeamento Direto

2 - Mapeamento Associativo

3 - Mapeamento Associativo por conjunto



3



Digite o algoritmo: 



1 - FIFO

2 - LRU

3 - LFU

4 - RANDOM



3



Digite a quantidade de conjuntos: 2



Digite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): acessos.txt

O tamanho da cache e de 4 paginas





Dados da cache: 



|  - |  - |

|  - |  - | 



Dados do endereco 0 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 0 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |

|  - |  - | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |

|  1 |  - | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  2 |

|  1 |  - | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 3 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  2 |

|  1 |  3 | 



Dados do endereco 4 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 4 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 3 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 2 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 1 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  1 |  3 | 



Dados do endereco 5 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 5 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  2 |

|  5 |  3 | 



Dados do endereco 8 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 8 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  4 |  8 |

|  5 |  3 | 



Dados do endereco 6 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 6 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  6 |  8 |

|  5 |  3 | 



Dados do endereco 10 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 10 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   8 |

|   5 |   3 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   2 |

|   5 |   3 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  10 |   2 |

|   5 |   1 | 



CACHE-HITS: 3

CACHE-MISSES: 11

FRACAO DE CACHE-HITS: 21.43 %



Deseja executar o programa novamente (SIM/ NAO) (OPÇÕES: -naozerarcache): nao

Pressione qualquer tecla para finalizar

#----------------------------------------

##### RANDOM:

#----------------------------------------


-------------CACHESIMUL-------------

----Simulador de memoria Cache----



Digite o numero de paginas da cache: 4

Digite o tipo de mapeamento: 



1 - Mapeamento Direto

2 - Mapeamento Associativo

3 - Mapeamento Associativo por conjunto



3



Digite o algoritmo: 



1 - FIFO

2 - LRU

3 - LFU

4 - RANDOM



4



Digite a quantidade de conjuntos: 2



Digite o nome do arquivo de entrada (o arquivo deve estar na mesma pasta que este executavel. Exemplo: 'nome_do_arquivo.txt'): acessos.txt

O tamanho da cache e de 4 paginas





Dados da cache: 



|  - |  - |

|  - |  - | 



Dados do endereco 0 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 0 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |

|  - |  - | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  - |

|  1 |  - | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 2 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  2 |

|  1 |  - | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 3 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  0 |  2 |

|  1 |  3 | 



Dados do endereco 4 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 4 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  2 |  4 |

|  1 |  3 | 



Dados do endereco 3 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 3 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  2 |  4 |

|  3 |  1 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 2 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  2 |  4 |

|  3 |  1 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 1 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|  2 |  4 |

|  1 |  3 | 



Dados do endereco 5 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 5 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  2 |  4 |

|  3 |  5 | 



Dados do endereco 8 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 8 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  2 |  8 |

|  3 |  5 | 



Dados do endereco 6 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 6 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|  2 |  6 |

|  3 |  5 | 



Dados do endereco 10 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 10 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|   2 |  10 |

|   3 |   5 | 



Dados do endereco 2 da memoria principal foram solicitados!

CACHE-HIT - Os dados do endereco 2 da memoria principal ja estavam na memoria cache

Dados da cache apos a solicitacao: 



|   2 |  10 |

|   3 |   5 | 



Dados do endereco 1 da memoria principal foram solicitados!

CACHE-MISS - Os dados do endereco 1 da memoria principal nao estavam na memoria cache

Dados da cache apos a solicitacao: 



|   2 |  10 |

|   3 |   1 | 



CACHE-HITS: 4

CACHE-MISSES: 10

FRACAO DE CACHE-HITS: 28.57 %



Deseja executar o programa novamente (SIM/ NAO) (OPÇÕES: -naozerarcache): nao

Pressione qualquer tecla para finalizar


#----------------------------------------
