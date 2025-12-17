# Examen Machine Learning – Riesgo Crediticio (Regresión Logística)

Proyecto de Machine Learning orientado a la **detección temprana de riesgo de incumplimiento crediticio**, utilizando **Regresión Logística** y **ajuste de umbral** para priorizar el *recall* de la clase minoritaria.

---

## Estructura del proyecto

- `01_data_understanding/`: Análisis exploratorio de datos (EDA)
- `02_data_preparation/`: Limpieza, transformación y generación de datasets finales
- `03_modeling/`: Entrenamiento del modelo (Regresión Logística)
- `04_evaluation/`: Evaluación del modelo, métricas y análisis de trade-offs
- `05_deployment/`: API FastAPI para simular uso en un entorno productivo
- `05_deployment/artifacts/`: Modelo entrenado y umbral (`.joblib`)
- `datos_examen/`: Datos originales en formato parquet (pueden excluirse por tamaño)

---

## Modelo

- **Algoritmo:** Regresión Logística  
- **Objetivo:** Predecir la probabilidad de incumplimiento crediticio (clase positiva)  
- **Métrica priorizada:** Recall de la clase minoritaria  
- **Umbral estándar:** 0.5  
- **Umbral recomendado (ajustado):** 0.3  

---

## Deployment (FastAPI)

### 1) Instalar dependencias

Desde la carpeta raíz del repositorio (donde se encuentra `requirements.txt`):

```bash
py -m pip install -r requirements.txt

### 2) Levantar la API
cd 05_deployment
py -m uvicorn app:app --reload

### La API queda disponible en:

Home: http://127.0.0.1:8000/

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

### 3) Endpoint /predict

Método: POST

URL: http://127.0.0.1:8000/predict

Entrada:
Recibe un JSON con las mismas columnas/features utilizadas durante el entrenamiento del modelo.

Salida:

prob_incumplimiento: probabilidad estimada de la clase positiva

prediccion:

1 si prob_incumplimiento >= threshold

0 en caso contrario

## Nota:
Si se envía un JSON vacío {} o con llaves incorrectas, la API puede retornar un error 500, ya que el DataFrame generado no coincide con las variables esperadas por el modelo.

## Datos

Los datasets originales pueden no incluirse en el repositorio debido a las restricciones de tamaño de GitHub (>100MB).

Para reproducir el proyecto, se deben ubicar los archivos .parquet en la carpeta datos_examen/, respetando los nombres originales.

## Notas técnicas
- La API carga el modelo y el umbral desde archivos `.joblib`.
- El endpoint `/predict` calcula la probabilidad y aplica el umbral ajustado para la decisión final.
