# Experimento: Condição de Corrida e Controle com Lock em Python

## Sobre o projeto

Este projeto apresenta um experimento desenvolvido em Python para demonstrar o problema conhecido como condição de corrida (*race condition*) e a importância dos mecanismos de sincronização no uso de múltiplas threads.

O experimento utiliza um contador como recurso compartilhado e compara duas situações: o acesso simultâneo sem proteção e o acesso controlado pelo mecanismo Lock.

## Objetivo

Demonstrar como o acesso concorrente a um recurso compartilhado pode provocar perda de atualizações e como a utilização de Lock permite garantir a integridade dos dados.

## Tecnologias utilizadas

- Python 3.13.14
- threading
- time
- Visual Studio Code

## Funcionamento do experimento

Foram utilizadas 12 threads, cada uma realizando 1.000 incrementos em um contador, totalizando 12.000 incrementos esperados.

O programa realiza dois testes:

1. **Sem Lock:** as threads modificam o contador sem proteção, permitindo a ocorrência de condições de corrida.
2. **Com Lock:** o acesso ao contador é protegido, permitindo que apenas uma thread por vez execute a seção crítica.

## Resultados obtidos

Foram realizadas três execuções, com os seguintes resultados:

| Execução | Sem Lock | Com Lock |
|---|---:|---:|
| Teste 1 | 1.002 | 12.000 |
| Teste 2 | 1.004 | 12.000 |
| Teste 3 | 1.002 | 12.000 |

Os resultados demonstraram a perda de atualizações na execução sem proteção e a consistência dos valores obtidos com a utilização de Lock.

## Conclusão

O experimento demonstrou a importância dos mecanismos de sincronização em aplicações concorrentes. A utilização de Lock garantiu a atualização correta do contador, enquanto a ausência de proteção provocou inconsistências nos resultados.

O projeto foi desenvolvido para fins acadêmicos e de estudo sobre concorrência, condições de corrida e sincronização de threads em Python.
