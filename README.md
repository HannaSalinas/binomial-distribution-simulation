# 📊 Simulación y Análisis de la Distribución Binomial

**Autora:** Hanna Jineth Contreras Salinas  
**Programa:** Ingeniería de Software y Datos — IUDigital  
**Materia:** Evaluación de Probabilidades  

---

## 📋 Descripción

Simulación completa de un proceso de ensamblaje industrial modelado con la distribución binomial (**n=15, p=0.8**). El proyecto cubre desde la simulación de datos hasta la validación estadística formal mediante prueba Chi², pasando por el cálculo de probabilidades teóricas y visualización comparativa.

---

## 🧪 ¿Qué hace este proyecto?

| Numeral | Descripción |
|---------|-------------|
| 1 | Simulación de 100 ciclos de ensamblaje + estadísticas descriptivas (media y varianza simulada vs teórica) |
| 2 | Cálculo de probabilidades teóricas exactas y acumuladas usando PMF y CDF |
| 3 | Gráfico comparativo: PMF teórica vs histograma de datos simulados |
| 4 | Prueba de bondad de ajuste Chi² con agrupación de celdas y decisión estadística |

---

## 🛠️ Tecnologías

| Librería | Uso |
|----------|-----|
| `numpy` | Simulación binomial, estadísticas descriptivas |
| `scipy.stats` | PMF, CDF, prueba Chi² |
| `matplotlib` | Gráfico comparativo (PNG de alta resolución) |

---

## 🚀 Cómo ejecutar

### 1. Instalar dependencias

```bash
pip install numpy scipy matplotlib
```

### 2. Ejecutar el script

```bash
python Simulando_la_distribución_binomial.py
```

### 3. Salida esperada

```
==================================================
NUMERAL 1 — Estadísticas descriptivas
==================================================
 Media simulada   : 12.1800
 Media teórica    : 12.0000 (μ = n·p)
 Varianza simulada: 2.3876
 Varianza teórica : 2.4000 (σ² = n·p·(1−p))
...

==================================================
NUMERAL 4 — Prueba de bondad de ajuste Chi²
==================================================
 Estadístico Chi² : 3.XXXX
 p-valor          : 0.XXXXXX
 → No se rechaza H0. Los datos son consistentes con la binomial.
```

El script también genera el archivo `grafica_binomial.png` en el directorio de trabajo.

---

## 📐 Parámetros del modelo

```python
n_intentos  = 15     # Intentos de ensamblaje por ciclo
prob_exito  = 0.8    # Probabilidad de éxito por intento (80%)
n_ensambles = 100    # Total de ciclos simulados
semilla     = 42     # Semilla para reproducibilidad
alpha       = 0.05   # Nivel de significancia Chi²
```

Para cambiar el escenario, modifica estos valores al inicio del script. Todos los numerales se recalculan automáticamente.

---

## 📊 Resultados clave

- **Media simulada ≈ 12.18** vs **teórica = 12.0** — diferencia mínima, confirma μ = n·p
- **Varianza simulada ≈ 2.39** vs **teórica = 2.40** — propiedad σ² = n·p·(1−p) verificada
- **P(X = 12) ≈ 25%** — alta concentración alrededor del valor esperado
- **P(X ≥ 10) ≈ 94%** — proceso de ensamblaje muy eficiente
- **Prueba Chi²**: no se rechaza H₀ → los datos simulados se ajustan a la distribución teórica

---

## 🗂️ Estructura del proyecto

```
📁 simulacion-binomial/
├── Simulando_la_distribución_binomial.py   # Script principal
├── grafica_binomial.png                    # Gráfico generado (se crea al ejecutar)
└── README.md                               # Este archivo
```

---

## 💡 Conceptos aplicados

- Distribución binomial: PMF y CDF con `scipy.stats.binom`
- Reproducibilidad con semilla fija (`np.random.seed`)
- Agrupación de celdas para cumplir supuesto del test Chi² (frecuencia esperada ≥ 5)
- Normalización del histograma (`density=True`) para comparación en escala de probabilidad
- Separación en funciones con docstrings para código limpio y mantenible

