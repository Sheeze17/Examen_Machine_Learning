# Examen Machine Learning – Riesgo Crediticio

## Descripción
Proyecto de Machine Learning orientado a la detección temprana de riesgo de incumplimiento crediticio
utilizando Regresión Logística y ajuste de umbral de decisión.

## Estructura del proyecto
- `01_data_understanding/`: Análisis exploratorio de datos (EDA)
- `02_data_preparation/`: Limpieza, transformación y generación de datasets finales
- `03_modeling/`: Entrenamiento del modelo de Regresión Logística
- `04_evaluation/`: Evaluación del modelo, métricas y análisis de trade-offs
- `05_deployment/`: Simulación de uso del modelo en un entorno productivo
- `artifacts/`: Modelo entrenado, umbral y datasets procesados
- `datos_examen/`: Datos originales en formato parquet

## Modelo
- Algoritmo: Regresión Logística
- Métrica clave: Recall de la clase minoritaria (incumplimiento)
- Umbral estándar: 0.5
- Umbral ajustado recomendado: 0.3

## Conclusión
El modelo es adecuado como sistema de apoyo a la decisión en contextos preventivos,
priorizando la detección temprana de incumplimientos, asumiendo un aumento controlado
de falsos positivos.

## Autor
Examen académico – Machine Learning
