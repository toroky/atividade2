# Relatório — Avaliação de Desempenho da Soma de Valores em Paralelo

**Disciplina:** Programação Concorrente e Distribuída
**Aluno(s):** Arthur Ferreira Poeck
**Turma:** Noturno
**Professor:** Rafael
**Data:** 18/03/2026

---

## 1. Descrição do Problema

Este trabalho consiste na implementação e avaliação de desempenho de um programa que realiza a **soma de uma grande quantidade de valores inteiros**, comparando a versão serial com versões paralelas executadas com diferentes números de processos.

### Questões respondidas

- **Qual é o objetivo do programa?**
  Somar 10 milhões de números inteiros armazenados em um arquivo de texto (`numero2.txt`) e comparar o tempo de execução entre a abordagem serial e a paralela.

- **Qual o volume de dados processado?**
  10.000.000 de números inteiros, com soma total igual a **5384**.

- **Qual algoritmo foi utilizado?**
  Divisão da lista em *chunks* (fatias) de tamanho igual, com cada processo somando sua fatia de forma independente. Os resultados parciais são somados ao final (redução).

- **Qual a complexidade aproximada do algoritmo?**
  O(n) — linear em relação ao número de elementos, tanto na versão serial quanto na paralela.

- **Qual o objetivo da paralelização?**
  Distribuir o trabalho entre múltiplos processos para reduzir o tempo total de execução, explorando os núcleos disponíveis no processador.

---

## 2. Ambiente Experimental

| Item                        | Descrição                          |
|-----------------------------|------------------------------------|
| Processador                 | Intel Core i5 (geração 2024)       |
| Número de núcleos           | Não identificado                   |
| Memória RAM                 | 18 GB                              |
| Sistema Operacional         | Windows 11                         |
| Linguagem utilizada         | Python 3                           |
| Biblioteca de paralelização | `multiprocessing` (Python padrão)  |
| Compilador / Versão         | Python 3.x                         |

---

## 3. Metodologia de Testes

### Como o tempo foi medido
O tempo de execução foi medido utilizando a função `time.perf_counter()` da biblioteca padrão do Python, que oferece alta resolução para medição de intervalos de tempo. O cronômetro é iniciado imediatamente antes da operação de soma e encerrado logo após.

### Configurações testadas
- 1 processo (versão serial)
- 2 processos
- 4 processos
- 8 processos
- 12 processos

### Procedimento experimental
- Foi realizada **1 execução** por configuração
- O tempo registrado é o tempo direto de cada execução
- Os experimentos foram realizados em ambiente local, com o sistema em uso normal
- O arquivo de entrada (`numero2.txt`) contém 10.000.000 números inteiros

---

## 4. Resultados Experimentais

| Nº Threads/Processos | Tempo de Execução (s) |
|----------------------|-----------------------|
| 1 (Serial)           | 0.057012              |
| 2                    | 0.841900              |
| 4                    | 0.631762              |
| 8                    | 0.668835              |
| 12                   | 0.694358              |

---

## 5. Cálculo de Speedup e Eficiência

### Fórmulas Utilizadas

**Speedup**
```
Speedup(p) = T(1) / T(p)
```
Onde:
- T(1) = tempo da execução serial
- T(p) = tempo com p threads/processos

**Eficiência**
```
Eficiência(p) = Speedup(p) / p
```
Onde:
- p = número de threads ou processos

---

## 6. Tabela de Resultados

| Threads/Processos | Tempo (s) | Speedup | Eficiência |
|-------------------|-----------|---------|------------|
| 1 (Serial)        | 0.057012  | 1.0000  | 1.00       |
| 2                 | 0.841900  | 0.0677  | 0.0339     |
| 4                 | 0.631762  | 0.0902  | 0.0226     |
| 8                 | 0.668835  | 0.0852  | 0.0107     |
| 12                | 0.694358  | 0.0821  | 0.0068     |

---

## 7. Gráfico de Tempo de Execução
<img width="1185" height="734" alt="grafico_tempo" src="https://github.com/user-attachments/assets/6a7721a8-3c6f-46a4-8bbb-88b50ad68765" />

Descrição: O gráfico apresenta o tempo de execução (eixo Y, em segundos) em função do número de processos utilizados (eixo X). A versão serial executa em apenas 0.057s, enquanto todas as versões paralelas apresentam tempos entre 0.63s e 0.84s. Isso evidencia que o overhead de criação de processos e comunicação domina o tempo total, tornando a versão paralela significativamente mais lenta para este problema.
---

## 8. Gráfico de Speedup

<img width="1185" height="734" alt="grafico_speedup" src="https://github.com/user-attachments/assets/9a2fa3b2-d5a6-46cb-8fd8-f3119dd39b73" />

Descrição: O gráfico compara o speedup real obtido (linha azul, eixo Y) com o speedup ideal teórico (linha verde tracejada) em função do número de processos (eixo X). O speedup ideal seria linear — 2, 4, 8 e 12 para cada configuração respectivamente. O speedup real ficou abaixo de 0.10 em todos os casos, demonstrando que a paralelização não trouxe ganho e que o custo de comunicação entre processos superou qualquer benefício do processamento distribuído.
---

## 9. Gráfico de Eficiência
<img width="1184" height="734" alt="grafico_eficiencia" src="https://github.com/user-attachments/assets/e1e7f08c-f572-42d2-80bc-5fb295b44df3" />

Descrição: O gráfico mostra a eficiência da paralelização (eixo Y, em %) em função do número de processos (eixo X). A linha verde tracejada representa a eficiência ideal de 100%. A eficiência despencou de 100% (serial) para apenas 3.39% com 2 processos, continuando a cair até 0.68% com 12 processos. Isso indica que a maior parte do tempo paralelo é desperdiçada com overhead, e não com processamento útil.
---

## 10. Análise dos Resultados

### O speedup obtido foi próximo do ideal?
Não. O speedup ideal para 2, 4, 8 e 12 processos seria 2, 4, 8 e 12 respectivamente. Os valores obtidos foram todos inferiores a 0.1, ou seja, a versão paralela foi **aproximadamente 15 vezes mais lenta** do que a serial em todos os casos.

### A aplicação apresentou escalabilidade?
Não. O tempo paralelo não diminuiu com o aumento do número de processos — pelo contrário, oscilou entre 0.63s e 0.84s independentemente da configuração, enquanto o serial executou em apenas 0.057s.

### Em qual ponto a eficiência começou a cair?
A eficiência já se mostrou muito baixa desde a configuração com 2 processos (3.39%), indicando que o problema começa antes mesmo de qualquer aumento no paralelismo.

### O número de threads ultrapassa o número de núcleos físicos da máquina?
Possivelmente sim na configuração com 12 processos, o que pode gerar contenção adicional de recursos do sistema operacional.

### Houve overhead de paralelização?
Sim, de forma muito expressiva. O módulo `multiprocessing` do Python cria **processos independentes** (não threads), o que implica:
- Criação e destruição de processos a cada execução
- Serialização e desserialização dos dados (*pickling*) para envio entre processos
- Cópia completa da lista de 10 milhões de números para cada processo

### Possíveis causas para a perda de desempenho

- **Overhead de criação de processos:** O custo de inicializar cada processo é fixo e relativamente alto comparado ao tempo da operação de soma em si.
- **Pickling (serialização):** O Python precisa serializar os chunks da lista para enviá-los aos processos filhos, o que é custoso para grandes volumes de dados.
- **Operação muito simples:** A soma é uma operação extremamente rápida em série (O(n) com operação elementar), não justificando o custo de distribuição.
- **Comunicação entre processos:** O retorno dos resultados parciais também envolve comunicação via IPC (*Inter-Process Communication*).
- **Contenção de memória:** A cópia dos dados para múltiplos processos pressiona o uso de memória RAM.

---

## 11. Conclusão

O experimento demonstrou que a paralelização **não trouxe ganho de desempenho** para este problema específico. A soma de 10 milhões de inteiros é uma operação simples e rápida em série (0.057s), e o custo de dividir os dados, criar processos e comunicar resultados foi muito maior do que o trabalho a ser paralelizado.

O melhor desempenho absoluto foi obtido pela **versão serial**, com tempo de 0.057012 segundos. A versão paralela com 4 processos apresentou o menor tempo entre as configurações paralelas (0.631762s), mas ainda assim aproximadamente **11 vezes mais lenta** que o serial.

O programa **não escala bem** com o aumento do paralelismo, pois o gargalo está no overhead de comunicação e criação de processos, e não no processamento em si.

### Melhorias possíveis
- Utilizar **numpy** para a soma, que executa operações vetorizadas em C internamente e é muito mais eficiente.
- Testar com volumes de dados ainda maiores (100 milhões+) onde o custo de comunicação se torna proporcionalmente menor.
- Utilizar linguagens como C ou Java com suporte nativo a threads para obter ganhos reais de paralelismo em operações aritméticas simples.
