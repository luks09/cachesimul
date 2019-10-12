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
    
