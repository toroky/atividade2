import time
import multiprocessing

# ──────────────────────────────────────────
# AJUSTE AQUI o caminho do seu arquivo
ARQUIVO = "numero2.txt"
# ──────────────────────────────────────────

def soma_parcial(chunk):
    return sum(chunk)

def main():
    # Lê o arquivo uma vez só
    with open(ARQUIVO, 'r') as f:
        numeros = list(map(int, f.read().split()))

    print(f"Arquivo: {ARQUIVO}")
    print(f"Total de números: {len(numeros)}")
    print("=" * 50)

    # ── SERIAL ──────────────────────────────
    inicio = time.perf_counter()
    total_serial = sum(numeros)
    tempo_serial = time.perf_counter() - inicio

    print(f"[SERIAL]")
    print(f"  Soma:  {total_serial}")
    print(f"  Tempo: {tempo_serial:.6f} s")
    print("=" * 50)

    # ── PARALELO ────────────────────────────
    print(f"[PARALELO]")
    resultados = []

    for num_threads in [2, 4, 8, 12]:
        tamanho_chunk = len(numeros) // num_threads
        chunks = [numeros[i * tamanho_chunk:(i + 1) * tamanho_chunk] for i in range(num_threads)]
        chunks[-1].extend(numeros[num_threads * tamanho_chunk:])

        inicio = time.perf_counter()
        with multiprocessing.Pool(processes=num_threads) as pool:
            parciais = pool.map(soma_parcial, chunks)
        total_paralelo = sum(parciais)
        tempo_paralelo = time.perf_counter() - inicio

        speedup    = tempo_serial / tempo_paralelo
        eficiencia = speedup / num_threads * 100

        print(f"  Threads: {num_threads:2d} | Soma: {total_paralelo} | "
              f"Tempo: {tempo_paralelo:.6f} s | "
              f"Speedup: {speedup:.4f} | "
              f"Eficiência: {eficiencia:.2f}%")

        resultados.append((num_threads, tempo_paralelo, speedup, eficiencia))

    print("=" * 50)
    print("\nCOPIE OS VALORES ABAIXO PARA O EXCEL:")
    print(f"{'Threads':<10} {'Tempo(s)':<15} {'Speedup':<12} {'Eficiência(%)'}")
    print(f"{'Serial':<10} {tempo_serial:<15.6f} {'1.0000':<12} {'100.00'}")
    for t, tp, sp, ef in resultados:
        print(f"{t:<10} {tp:<15.6f} {sp:<12.4f} {ef:.2f}")

if __name__ == "__main__":
    main()