# Monitor - Sistemas Operacionais

| **Sumário** |
|-------------|
| [Autores](#autores) |
| [Compilação e Execução](#compilação-e-execução) |
| [Funcionamento](#funcionamento) |


## Autores
 - Gabriel Frasson Costa - 202035001
 - Gabriel Gomes Bahia - 202035028
 - João Pedro Ferreira Pedreira - 202076009
 - Nélio Alves Gouvêa - 201935037

## Compilação e Execução

**Requisitos:** Para executar o programa é necessário ter o `python` instalado.

**OBS:** Não é necessário instalar nenhuma biblioteca.

Para **executar** o programa, rode o comando na **raiz** do projeto:

```bash
python src/main.py
```

Para **interromper** a execução do programa (loop infinito) digite `Ctrl + C` no terminal.

## Funcionamento

O código é composto por dois arquivos: `main.py` e `Monitor.py`.

### `Monitor.py`

Em `Monitor.py` é implementada uma classe chamada `ProducerConsumer` responsável pela lógica do monitor.
Ela possui dois atributos do tipo `Semaphore` (da bilioteca `threading` nativa do python), que controlam 
os acessos ao buffer da classe. Esses atributos são `empty_semaphore` (inicializado com tamanho `size`) 
e `full_semaphore` (inicializado com tamanho `0`), que representam os espaços vazios e espaços cheios do 
buffer, respectivamente. Além disso, a classe também possui um mutex que utiliza a classe `Lock` da 
biblioteca `threading` responsável por proteger o acesso à região crítica. O `buffer`, por sua vez, 
é representado por uma lista que é inicializada vazia, podendo atingir um tamanho máximo que é armazenado 
no atributo `size`.

A classe é composta por dois **métodos**: `insert` e `remove`.
 - `insert`:
    - ***Down*** no semáforo `empty_semaphore`;
    - ***Down*** no `mutex` para acessar a região crítica;
    - Inserção do item no `buffer`;
    - ***Up*** no `mutex` para liberar a região crítica;
    - ***Up*** no semáforo `full_semaphore`;

 - `remove`:
    - ***Down*** no semáforo `full_semaphore`;
    - ***Down*** no `mutex` para acessar a região crítica;
    - Remoção do item no `buffer`;
    - ***Up*** no `mutex` para liberar a região crítica;
    - ***Up*** no semáforo `empty_semaphore`;

### `main.py`

Em `main.py` é implementada uma classe `Program` com dois métodos `produce` e `consume`, responsáveis 
por produzir e consumir itens do buffer, respectivamente, em um loop infinito, **utilizando o monitor** 
`ProducerConsumer`. Em seguida são criadas múltiplas threads produtoras e consumidoras para executar 
os métodos da classe `Program` até que seja solicitada a finalização do programa. O gerenciamento de threads 
foi feito utilizando a classe `Thread` da biblioteca `threading` do python.
