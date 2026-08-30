import statistics
import numpy as np

# Contexto: notas de uma turma escolar.
# Cada aluno tem 3 notas (CP1, CP2, CP3), com pesos 1, 2 e 3 (a última
# prova vale mais) — a nota final do aluno é a média ponderada dessas notas.
# Peso usado para média/mediana ponderada da turma: frequência do aluno (%).

PESOS_PROVAS = [1, 2, 3]

ALUNOS = {
    "Ana":      {"notas": [7, 8, 9],   "frequencia": 95},
    "Bruno":    {"notas": [5, 6, 7],   "frequencia": 80},
    "Carla":    {"notas": [9, 9, 10],  "frequencia": 98},
    "Diego":    {"notas": [4, 5, 5],   "frequencia": 65},
    "Elisa":    {"notas": [6, 7, 8],   "frequencia": 88},
    "Fabio":    {"notas": [3, 4, 4],   "frequencia": 55},
    "Gabriela": {"notas": [8, 8, 9],   "frequencia": 92},
    "Hugo":     {"notas": [7, 6, 8],   "frequencia": 85},
    "Isabela":  {"notas": [10, 9, 10], "frequencia": 99},
    "Joao":     {"notas": [2, 3, 3],   "frequencia": 45},
    "Karina":   {"notas": [6, 6, 7],   "frequencia": 78},
    "Lucas":    {"notas": [8, 9, 8],   "frequencia": 90},
    "Marina":   {"notas": [5, 5, 6],   "frequencia": 70},
    "Nicolas":  {"notas": [9, 10, 10], "frequencia": 97},
    "Otavio":   {"notas": [7, 7, 7],   "frequencia": 83},
}


def nota_final(notas, pesos=PESOS_PROVAS):
    return sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)


def media_aritmetica(dados):
    return statistics.mean(dados)


def media_ponderada(dados, pesos):
    return sum(x * p for x, p in zip(dados, pesos)) / sum(pesos)


def mediana(dados):
    return statistics.median(dados)


def mediana_ponderada(dados, pesos):
    pares = sorted(zip(dados, pesos))
    metade = sum(pesos) / 2
    acumulado = 0
    for valor, peso in pares:
        acumulado += peso
        if acumulado >= metade:
            return valor
    return pares[-1][0]


def media_aparada(dados, proporcao=0.1):
    ordenados = sorted(dados)
    corte = int(len(ordenados) * proporcao)
    aparado = ordenados[corte: len(ordenados) - corte] if corte > 0 else ordenados
    return statistics.mean(aparado)


def amplitude_total(dados):
    return max(dados) - min(dados)


def moda(dados):
    return statistics.mode(dados)


def variancia_amostral(dados):
    return statistics.variance(dados)


def desvio_padrao_amostral(dados):
    return statistics.stdev(dados)


def desvio_padrao_populacional(dados):
    return statistics.pstdev(dados)


def quartil_1(dados):
    return np.percentile(dados, 25)


def percentil_90(dados):
    return np.percentile(dados, 90)


def iqr(dados):
    return np.percentile(dados, 75) - np.percentile(dados, 25)


def outliers_iqr(dados):
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    amplitude_iqr = q3 - q1
    limite_inferior = q1 - 1.5 * amplitude_iqr
    limite_superior = q3 + 1.5 * amplitude_iqr
    return [x for x in dados if x < limite_inferior or x > limite_superior]


def mad(dados):
    med = statistics.median(dados)
    return statistics.median(abs(x - med) for x in dados)


def main():
    notas_finais = [nota_final(aluno["notas"]) for aluno in ALUNOS.values()]
    frequencias = [aluno["frequencia"] for aluno in ALUNOS.values()]

    print("Alunos:", list(ALUNOS.keys()))
    print("Notas finais da turma:", [round(n, 2) for n in notas_finais])
    print("Frequências (%, peso):", frequencias)
    print("-" * 50)
    print(f"1.  Média aritmética:            {media_aritmetica(notas_finais):.2f}")
    print(f"2.  Média ponderada:             {media_ponderada(notas_finais, frequencias):.2f}")
    print(f"3.  Mediana:                     {mediana(notas_finais):.2f}")
    print(f"4.  Mediana ponderada:           {mediana_ponderada(notas_finais, frequencias):.2f}")
    print(f"5.  Média aparada (10%):         {media_aparada(notas_finais):.2f}")
    print(f"6.  Amplitude total:             {amplitude_total(notas_finais):.2f}")
    print(f"7.  Moda:                        {moda([round(n, 2) for n in notas_finais])}")
    print(f"8.  Variância amostral:          {variancia_amostral(notas_finais):.2f}")
    print(f"9.  Desvio-padrão amostral:      {desvio_padrao_amostral(notas_finais):.2f}")
    print(f"10. Desvio-padrão populacional:  {desvio_padrao_populacional(notas_finais):.2f}")
    print(f"11. IQR:                         {iqr(notas_finais):.2f}")
    print(f"12. 1º quartil (25%):            {quartil_1(notas_finais):.2f}")
    print(f"13. 90º percentil:               {percentil_90(notas_finais):.2f}")
    print(f"14. Outliers (critério IQR):     {[round(x, 2) for x in outliers_iqr(notas_finais)]}")
    print(f"15. MAD:                         {mad(notas_finais):.2f}")


if __name__ == "__main__":
    main()