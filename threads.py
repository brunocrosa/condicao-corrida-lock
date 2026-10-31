
"""
Prática 2 — Condição de corrida e controle por Lock.

Demonstra como múltiplas threads podem acessar e modificar
um recurso compartilhado, utilizando um contador como exemplo.

O programa compara duas situações:
1. Incrementos sem proteção por Lock.
2. Incrementos protegidos por Lock.

Foram utilizadas 12 threads, cada uma realizando 1.000 incrementos.
"""

import threading
import time

# Configurações do experimento
NUM_THREADS = 12
INCREMENTOS_POR_THREAD = 1000
ATRASO_DIDATICO = 0.00001

# Recurso compartilhado
contador = 0
lock = threading.Lock()


def incrementar_sem_lock():
    """Realiza incrementos sem proteção, demonstrando a condição de corrida."""
    global contador

    for _ in range(INCREMENTOS_POR_THREAD):
        valor_antigo = contador
        time.sleep(ATRASO_DIDATICO)
        contador = valor_antigo + 1


def incrementar_com_lock():
    """Realiza incrementos protegidos pelo Lock."""
    global contador

    for _ in range(INCREMENTOS_POR_THREAD):
        with lock:
            valor_antigo = contador
            time.sleep(ATRASO_DIDATICO)
            contador = valor_antigo + 1


def executar_teste(funcao):
    """Cria as threads, inicia a execução e aguarda todas terminarem."""
    global contador

    contador = 0

    threads = [
        threading.Thread(
            target=funcao,
            name=f"Thread-{i + 1}"
        )
        for i in range(NUM_THREADS)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return contador


def main():
    esperado = NUM_THREADS * INCREMENTOS_POR_THREAD

    print("\n=== PRÁTICA 2: RECURSO COMPARTILHADO ===")
    print(f"Threads: {NUM_THREADS}")
    print(f"Incrementos por thread: {INCREMENTOS_POR_THREAD}")
    print(f"Incrementos totais esperados: {esperado}\n")

    # Teste sem Lock
    sem_protecao = executar_teste(incrementar_sem_lock)

    print(f"Sem Lock: {sem_protecao} (esperado: {esperado})")

    # Teste com Lock
    com_protecao = executar_teste(incrementar_com_lock)

    print(f"Com Lock: {com_protecao} (esperado: {esperado})")

    # Explicação dos resultados
    print("\n=== ANÁLISE DOS RESULTADOS ===")
    print("Por que join() não resolve a condição de corrida?")
    print("Porque join() apenas aguarda o término das threads.")
    print("O Lock controla o acesso simultâneo ao recurso compartilhado.")

    print("\nAtenção: o resultado sem Lock pode variar a cada execução.")
    print("Com Lock, o resultado esperado é sempre alcançado.")


if __name__ == "__main__":
    main()
