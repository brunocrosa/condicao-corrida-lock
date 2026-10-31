# Experimento: Condição de Corrida e Controle por Lock em Python

## Sobre o projeto

Este projeto apresenta um experimento desenvolvido em Python com o objetivo de demonstrar o problema conhecido como condição de corrida (*race condition*) e a importância dos mecanismos de sincronização na execução de tarefas utilizando múltiplas threads.

Foi utilizado um contador como recurso compartilhado, permitindo analisar como diferentes threads podem acessar e modificar simultaneamente uma mesma variável, ocasionando inconsistências nos resultados.

## Objetivo

Demonstrar como o acesso simultâneo a um recurso compartilhado pode provocar a perda de atualizações e como a utilização de mecanismos de sincronização, como o Lock, permite controlar esse acesso e garantir a integridade dos dados.

## Tecnologias utilizadas

- **Python 3.13.14**
- **threading:** criação e gerenciamento de threads, além da utilização de mecanismos de sincronização.
- **time:** simulação de pequenos atrasos entre as operações de leitura e escrita.
- **Visual Studio Code:** ambiente utilizado para desenvolvimento e execução do programa.

## Como funciona

O programa realiza duas etapas:

1. **Execução sem Lock:** são criadas 12 threads, cada uma responsável por realizar 1.000 incrementos em um contador compartilhado, sem qualquer mecanismo de proteção. Essa situação permite observar a ocorrência de condições de corrida e a perda de atualizações.
2. **Execução com Lock:** as mesmas 12 threads realizam os incrementos utilizando o mecanismo Lock, que controla o acesso ao contador e permite que apenas uma thread por vez execute a seção crítica.

Ao final, o programa apresenta os resultados das duas execuções e compara os valores obtidos com o total esperado de 12.000 incrementos.

## Como executar

1. Instale o Python em seu computador.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto no Visual Studio Code ou em outro ambiente compatível.
4. Execute o seguinte comando no terminal:

```bash
python pratica2_threads.py
```

## Resultados obtidos

Foram realizadas três execuções do programa, utilizando 12 threads e 1.000 incrementos por thread. Os resultados obtidos foram:

| Indicador | Resultado |
|---|---:|
| Quantidade de threads | 12 |
| Incrementos por thread | 1.000 |
| Total esperado | 12.000 |
| Resultado sem Lock (teste 1) | 1.002 |
| Resultado sem Lock (teste 2) | 1.004 |
| Resultado sem Lock (teste 3) | 1.002 |
| Resultado com Lock (três testes) | 12.000 |

Os resultados demonstraram a ocorrência de perdas de atualizações na execução sem proteção e a consistência dos valores obtidos com a utilização de Lock.

## Conclusão

O experimento demonstrou a importância dos mecanismos de sincronização em programas que utilizam múltiplas threads e compartilham recursos.

A comparação entre as duas situações evidenciou que a ausência de proteção pode provocar condições de corrida e inconsistências nos dados. Por outro lado, a utilização de Lock garantiu que todas as 12.000 operações fossem contabilizadas corretamente nas três execuções realizadas.

É importante destacar que o pequeno atraso introduzido pela função `time.sleep()` teve finalidade didática, aumentando a possibilidade de ocorrência de condições de corrida e facilitando a observação desse comportamento.

---

**Projeto desenvolvido para fins acadêmicos e de estudo sobre concorrência, condições de corrida e sincronização de threads em Python.**
