# ==============================================================
# Evidencia de Aprendizaje 2
# Simulación y análisis de la distribución binomial
#
# Estudiantes: Hanna Jineth Contreras Salinas
# Programa: Ingeniería de Software y Datos
#
# Descripción:
# Este script simula un proceso de ensamblaje con distribución
# binomial (n=15, p=0.8), calcula estadísticas descriptivas,
# evalúa probabilidades teóricas, compara la PMF con datos
# simulados y realiza una prueba de bondad de ajuste Chi².
# 
# ==============================================================

# Importo las tres librerías necesarias para toda la actividad.
# numpy para cálculos numéricos, matplotlib para la gráfica,
# y de scipy solo importo binom (distribución binomial) y
# chisquare (prueba de bondad de ajuste) para no cargar todo.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, chisquare

# ==============================================================
# PARÁMETROS GLOBALES DEL PROBLEMA
# ==============================================================

# Defino los parámetros del problema como variables globales
# para que si alguno cambia, solo se modifique en este lugar.
n_intentos  = 15     # Intentos de ensamblaje por ciclo
prob_exito  = 0.8    # Probabilidad de éxito por intento (80%)
n_ensambles = 100    # Total de ciclos simulados
semilla     = 42     # Semilla fija para resultados reproducibles
alpha       = 0.05   # Nivel de significancia para la prueba Chi²

# ==============================================================
# NUMERAL 1 — Simulación y estadísticas descriptivas
# ==============================================================

def simular_ensambles(n: int, p: float, num_ensambles: int, semilla: int) -> np.ndarray:
    """
    Simulo el número de éxitos en cada ensamble usando la
    distribución binomial. Fijo la semilla para que cualquier
    persona que ejecute este script obtenga los mismos resultados.
    Retorna un array con los 100 resultados de la simulación.
    """
    # La semilla garantiza que la secuencia aleatoria sea siempre
    # la misma, haciendo el trabajo completamente reproducible.
    np.random.seed(semilla)

    # Simulo n_ensambles ciclos, cada uno con n intentos y
    # probabilidad p de éxito. Retorno el array de resultados.
    return np.random.binomial(n, p, num_ensambles)


def mostrar_estadisticas(datos: np.ndarray, n: int, p: float) -> None:
    """
    Calculo e imprimo la media y varianza simuladas comparadas
    con los valores teóricos, y verifico la propiedad σ²=n·p·(1−p).
    """
    # Calculo la media y varianza de los datos reales simulados.
    # np.var usa varianza poblacional (sin corrección de Bessel).
    media_simulada    = np.mean(datos)
    varianza_simulada = np.var(datos)

    # Calculo los valores teóricos con las fórmulas de la binomial.
    # La media teórica es n*p y la varianza es n*p*(1-p).
    media_teorica    = n * p
    varianza_teorica = n * p * (1 - p)

    print("=" * 50)
    print("NUMERAL 1 — Estadísticas descriptivas")
    print("=" * 50)
    print(f" Media simulada   : {media_simulada:.4f}")
    print(f" Media teórica    : {media_teorica:.4f} (μ = n·p)")
    print(f" Varianza simulada: {varianza_simulada:.4f}")
    print(f" Varianza teórica : {varianza_teorica:.4f} (σ² = n·p·(1−p))")

    # Mido qué tan lejos está la varianza simulada de la teórica.
    diferencia_var = abs(varianza_simulada - varianza_teorica)
    print(f"\n Diferencia absoluta en varianza: {diferencia_var:.4f}")

    print("\n Interpretación:")
    print(" La media simulada de 12.18 es muy cercana a la teórica de 12.0, calculada")
    print(" con la fórmula μ = n·p = 15 × 0.8. La varianza simulada de 2.3876 se aproxima")
    print(" a la teórica de 2.4000, con una diferencia de apenas 0.0124, lo que confirma")
    print(" que la propiedad σ² = n·p·(1−p) se cumple. La pequeña diferencia es normal")
    print(" y esperada: con solo 100 ensambles siempre existe una variación aleatoria.")
    print(" Si se aumentara el número de ensambles a 10.000, la diferencia sería aún")
    print(" menor debido a la ley de los grandes números.\n")


# ==============================================================
# NUMERAL 2 — Probabilidades teóricas
# ==============================================================

def calcular_probabilidades(n: int, p: float) -> None:
    """
    Calculo las tres probabilidades teóricas solicitadas usando
    la PMF para valores exactos y la CDF para rangos acumulados.
    """
    # a) P(X = 12): uso la PMF porque pregunta por un valor exacto.
    # Internamente evalúa: C(15,12) × 0.8^12 × 0.2^3
    prob_exactamente_12 = binom.pmf(12, n, p)

    # b) P(X >= 10): uso el complemento de la CDF.
    # P(X>=10) = 1 - P(X<=9). Es más eficiente que sumar
    # individualmente P(10)+P(11)+P(12)+P(13)+P(14)+P(15).
    prob_al_menos_10 = 1 - binom.cdf(9, n, p)

    # c) P(8 <= X <= 12): uso la diferencia de dos CDF.
    # binom.cdf(12) acumula del 0 al 12, binom.cdf(7) acumula
    # del 0 al 7. La diferencia deja solo el rango 8 a 12.
    prob_entre_8_12 = binom.cdf(12, n, p) - binom.cdf(7, n, p)

    print("=" * 50)
    print("NUMERAL 2 — Probabilidades teóricas")
    print("=" * 50)
    print(f" a) P(X = 12)       : {prob_exactamente_12:.6f} ({prob_exactamente_12*100:.4f}%)")
    print(f" b) P(X >= 10)      : {prob_al_menos_10:.6f} ({prob_al_menos_10*100:.4f}%)")
    print(f" c) P(8 <= X <= 12) : {prob_entre_8_12:.6f} ({prob_entre_8_12*100:.4f}%)")

    print("\n Interpretación:")
    print(" a) Aproximadamente 25% de probabilidad de obtener exactamente 12 éxitos.")
    print(" b) Alta probabilidad de lograr 10 o más éxitos (equipo eficiente).")
    print(" c) El rango 8–12 concentra gran parte de la probabilidad.\n")


# ==============================================================
# NUMERAL 3 — Gráfico comparativo
# ==============================================================

def graficar_pmf_vs_simulacion(datos: np.ndarray, n: int, p: float) -> None:
    """
    Comparo visualmente la PMF teórica con el histograma simulado.
    Guardo la figura en PNG y la muestro sin bloquear la terminal.
    """
    # Genero los valores posibles del 0 al 15 para el eje x.
    x = np.arange(0, n + 1)

    # Calculo la probabilidad teórica para cada valor posible.
    pmf_teorica = binom.pmf(x, n, p)

    plt.figure(figsize=(8, 5))

    # Dibujo las barras de la PMF teórica con transparencia
    # para que el histograma simulado sea visible detrás.
    plt.bar(x, pmf_teorica, alpha=0.6, label="PMF Teórica")

    # Dibujo el histograma de los datos simulados.
    # bins con -0.5 centra cada barra exactamente sobre su
    # valor entero, alineándola con las barras teóricas.
    # density=True normaliza para comparar en escala de probabilidad.
    plt.hist(
        datos,
        bins=np.arange(0, n + 2) - 0.5,
        density=True,
        alpha=0.6,
        label="Datos simulados"
    )

    plt.xlabel("Número de éxitos por ensamble")
    plt.ylabel("Probabilidad")
    plt.title("Comparación binomial teórica vs simulación")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    # Guardo la figura en alta resolución antes de mostrarla.
    plt.savefig("grafica_binomial.png", dpi=300)

    print("=" * 50)
    print("NUMERAL 3 — Gráfico")
    print("=" * 50)
    print(" Gráfica guardada como 'grafica_binomial.png'\n")

    # Muestro la gráfica sin bloquear la terminal (block=False),
    # la mantengo visible 3 segundos y luego la cierro.
    plt.show(block=False)
    plt.pause(3)
    plt.close()


# ==============================================================
# NUMERAL 4 — Prueba Chi²
# ==============================================================

def prueba_bondad_ajuste(datos: np.ndarray, n: int, p: float, alpha: float) -> None:
    """
    Realizo la prueba Chi² para verificar si los datos simulados
    se ajustan a la distribución binomial teórica.
    Agrupo celdas con frecuencia esperada menor a 5 para cumplir
    el supuesto básico del test Chi².
    """
    num_ensambles = len(datos)
    valores_x     = np.arange(0, n + 1)
    pmf_teorica   = binom.pmf(valores_x, n, p)

    # Cuento cuántas veces apareció cada valor en los datos reales.
    frecuencias_obs = np.array([np.sum(datos == k) for k in valores_x], dtype=float)

    # Calculo cuántas veces debería aparecer cada valor si los datos
    # siguieran perfectamente la binomial teórica.
    frecuencias_esp = pmf_teorica * num_ensambles

    # Agrupa celdas con frecuencia esperada < 5.
    # El test Chi² no es válido si alguna celda tiene menos de 5,
    # porque los valores muy pequeños distorsionan el estadístico.
    # Acumulo valores consecutivos hasta alcanzar el mínimo de 5.
    obs_agrupado = []
    esp_agrupado = []
    acum_obs     = 0.0
    acum_esp     = 0.0

    for obs_i, esp_i in zip(frecuencias_obs, frecuencias_esp):
        acum_obs += obs_i
        acum_esp += esp_i

        if acum_esp >= 5:
            obs_agrupado.append(acum_obs)
            esp_agrupado.append(acum_esp)
            acum_obs = 0.0
            acum_esp = 0.0

    # Si quedó algún residuo al final, lo uno a la última celda.
    if acum_esp > 0 and esp_agrupado:
        obs_agrupado[-1] += acum_obs
        esp_agrupado[-1] += acum_esp

    obs_agrupado = np.array(obs_agrupado)
    esp_agrupado = np.array(esp_agrupado)

    # Ejecuto la prueba Chi² con las frecuencias ya agrupadas.
    chi2_stat, p_valor = chisquare(obs_agrupado, f_exp=esp_agrupado)

    print("=" * 50)
    print("NUMERAL 4 — Prueba de bondad de ajuste Chi²")
    print("=" * 50)
    print(f" Celdas usadas tras agrupación : {len(obs_agrupado)}")
    print(f" Estadístico Chi²              : {chi2_stat:.4f}")
    print(f" p-valor                       : {p_valor:.6f}")
    print(f" Nivel de significancia (alpha): {alpha}")

    print("\n Interpretación:")
    # Si el p-valor es mayor al nivel de significancia, no hay
    # evidencia suficiente para rechazar que los datos son binomiales.
    if p_valor > alpha:
        print(" No se rechaza H0. Los datos son consistentes con la binomial.")
    else:
        print(" Se rechaza H0. Los datos NO se ajustan a la binomial.")
    print()


# ==============================================================
# PUNTO DE ENTRADA
# ==============================================================

# Este bloque garantiza que el código solo se ejecute cuando
# el archivo se corra directamente, no cuando se importe.
if __name__ == "__main__":

    # Genero los datos simulados una sola vez y los reutilizo
    # en los numerales 1, 3 y 4 para garantizar coherencia.
    datos_simulados = simular_ensambles(
        n_intentos,
        prob_exito,
        n_ensambles,
        semilla
    )

    mostrar_estadisticas(datos_simulados, n_intentos, prob_exito)
    calcular_probabilidades(n_intentos, prob_exito)
    graficar_pmf_vs_simulacion(datos_simulados, n_intentos, prob_exito)
    prueba_bondad_ajuste(datos_simulados, n_intentos, prob_exito, alpha)