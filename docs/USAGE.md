# Guía de Uso Detallada - AI Text Humanizer

## 📋 Tabla de Contenidos

1. [Instalación Paso a Paso](#instalación-paso-a-paso)
2. [Primer Uso](#primer-uso)
3. [Modos de Operación](#modos-de-operación)
4. [Opciones Avanzadas](#opciones-avanzadas)
5. [Interpretación de Resultados](#interpretación-de-resultados)
6. [Solución de Problemas](#solución-de-problemas)
7. [Mejores Prácticas](#mejores-prácticas)
8. [Ejemplos de Uso](#ejemplos-de-uso)

---

## Instalación Paso a Paso

### 1. Requisitos del Sistema

**Sistema Operativo:**
- Linux (Ubuntu 20.04+, Debian 11+, etc.)
- macOS (10.15+)
- Windows 10/11 (con WSL2 recomendado)

**Hardware Mínimo:**
- CPU: 4 cores
- RAM: 8GB (16GB recomendado)
- Almacenamiento: 20GB libres

**Software:**
- Python 3.8 o superior
- Git
- pip (gestor de paquetes de Python)

### 2. Instalar Ollama

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**macOS:**
```bash
# Descargar desde https://ollama.ai
# O usando Homebrew:
brew install ollama
```

**Windows:**
- Descargar desde https://ollama.ai/download

### 3. Descargar Modelo de IA

```bash
# Verificar instalación de Ollama
ollama --version

# Descargar modelo qwen2.5:14b (recomendado)
ollama pull qwen2.5:14b

# Verificar que el modelo está disponible
ollama list
```

**Modelos Alternativos:**
```bash
# Si qwen2.5:14b es muy pesado, usa:
ollama pull qwen2.5:7b

# Para mejor calidad (requiere más RAM):
ollama pull qwen2.5:32b
```

### 4. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/ai-text-humanizer.git
cd ai-text-humanizer
```

### 5. Crear Entorno Virtual

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 6. Instalar Dependencias

```bash
# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt

# Instalar navegadores para Playwright
playwright install chromium
```

### 7. Verificar Instalación

```bash
# Ejecutar test básico
python -m pytest tests/ -v

# O probar directamente
python -m src.main --help
```

---

## Primer Uso

### Ejecución Básica

```bash
# Activar entorno virtual (si no está activo)
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Ejecutar programa
python -m src.main
```

### Flujo Interactivo

1. **Seleccionar Idioma:**
   ```
   [?] Selecciona el idioma del texto:
     > Español
       English
       Français
   ```

2. **Ingresar Texto:**
   ```
   📝 Pega tu texto a continuación
   (Presiona Enter dos veces para terminar)
   
   > [Tu texto aquí...]
   ```

3. **Análisis Inicial:**
   - Se ejecutan múltiples detectores de IA
   - Verás resultados en tiempo real

4. **Confirmación:**
   ```
   ¿Deseas humanizar este texto? (Y/n)
   ```

5. **Proceso de Humanización:**
   - Se realizan hasta 5 iteraciones
   - Cada iteración muestra progreso

6. **Resultados:**
   - Texto humanizado
   - Reporte de análisis
   - Archivos guardados en `/output`

---

## Modos de Operación

### Modo 1: Interactivo (Por Defecto)

```bash
python -m src.main
```

- Guía paso a paso
- Preguntas interactivas
- Mejor para usuarios nuevos

### Modo 2: Con Parámetros

```bash
python -m src.main \
  --language es \
  --max-iterations 3 \
  --threshold 10
```

- Más rápido
- Sin preguntas interactivas
- Mejor para uso repetitivo

### Modo 3: Desde Archivo

```bash
python -m src.main --input mi_texto.txt
```

- Lee texto desde archivo
- Útil para textos largos
- Permite automatización

### Modo 4: Personalizado

```bash
python -m src.main \
  --config mi_config.yaml \
  --input texto.txt \
  --language en \
  --max-iterations 10 \
  --threshold 5
```

- Control total
- Configuración personalizada
- Para usuarios avanzados

---

## Opciones Avanzadas

### Opciones de Línea de Comandos

```bash
python -m src.main [OPCIONES]

Opciones:
  -l, --language CÓDIGO      Idioma (es, en, fr, de, pt, it)
  -i, --input ARCHIVO        Archivo de entrada
  -m, --max-iterations NUM   Máximo de iteraciones (default: 5)
  -t, --threshold NUM        Umbral de % IA (default: 15)
  -c, --config ARCHIVO       Archivo de configuración
  --help                     Mostrar ayuda
```

### Personalizar Configuración

Edita `config/config.yaml`:

```yaml
# Cambiar modelo de IA
ollama:
  model: "qwen2.5:7b"  # Modelo más ligero
  temperature: 0.8     # Más creativo

# Habilitar/deshabilitar detectores
detectors:
  enabled:
    - gptzero
    - writer
    # - sapling  # Comentar para deshabilitar

# Ajustar iteraciones
rewriting:
  max_iterations: 10
  target_threshold: 5
```

---

## Interpretación de Resultados

### Scores de Detección

| Porcentaje | Interpretación | Acción |
|------------|---------------|--------|
| 0-15% | Bajo / Humano | ✅ Objetivo alcanzado |
| 16-40% | Moderado | ⚡ Mejorable |
| 41-70% | Alto | ⚠️ Requiere trabajo |
| 71-100% | Muy Alto | ❌ Necesita reescritura |

### Detectores Individuales

**GPTZero:**
- Generalmente más estricto
- Enfocado en patrones de IA

**Writer.com:**
- Balance entre precisión y recall
- Bueno para contenido general

**ZeroGPT:**
- A veces da falsos positivos
- Útil como referencia adicional

**Sapling:**
- Menos preciso pero rápido
- Útil para screening inicial

### Análisis de Mejora

```
Iteración 1: 85% → 45% (-40 puntos) ✨ Excelente
Iteración 2: 45% → 38% (-7 puntos)  ✓ Bien
Iteración 3: 38% → 42% (+4 puntos)  ⚠️ Empeoró
```

**Interpretación:**
- Mejora >10 puntos: Excelente progreso
- Mejora 5-10 puntos: Buen progreso
- Mejora <5 puntos: Mejora marginal
- Empeora: Iterar más no ayudará

---

## Solución de Problemas

### Problema: Ollama no funciona

**Síntomas:**
```
Error: Ollama not available
```

**Soluciones:**
```bash
# Verificar que Ollama está corriendo
ollama list

# Si no responde, reiniciar servicio
# Linux/macOS:
sudo systemctl restart ollama

# O ejecutar manualmente:
ollama serve
```

### Problema: Modelo no disponible

**Síntomas:**
```
Model qwen2.5:14b not available
```

**Soluciones:**
```bash
# Descargar modelo
ollama pull qwen2.5:14b

# Verificar descarga
ollama list

# Si sigue fallando, usar modelo alternativo
# Editar config/config.yaml:
# model: "qwen2.5:7b"
```

### Problema: Detectores fallan

**Síntomas:**
```
❌ gptzero: Timeout
❌ writer: Network error
```

**Soluciones:**

1. **Verificar conexión a internet:**
   ```bash
   ping google.com
   ```

2. **Aumentar timeout en config.yaml:**
   ```yaml
   detectors:
     gptzero:
       timeout: 60  # Aumentar a 60 segundos
   ```

3. **Ejecutar con menos detectores:**
   ```yaml
   detectors:
     enabled:
       - gptzero  # Solo usar uno
   ```

4. **Modo headless off (para debugging):**
   ```yaml
   browser:
     headless: false  # Ver qué pasa
   ```

### Problema: Texto no mejora

**Síntomas:**
```
Iteración 1: 80%
Iteración 2: 79%
Iteración 3: 78%
...mejora muy lenta
```

**Soluciones:**

1. **Cambiar temperatura:**
   ```yaml
   ollama:
     temperature: 0.9  # Más creativo
   ```

2. **Usar modelo más grande:**
   ```bash
   ollama pull qwen2.5:32b
   ```

3. **Editar texto manualmente** antes de procesar

4. **Dividir en secciones** más pequeñas

### Problema: RAM insuficiente

**Síntomas:**
```
Killed
Out of memory
```

**Soluciones:**

1. **Usar modelo más pequeño:**
   ```bash
   ollama pull qwen2.5:7b
   ```

2. **Cerrar otras aplicaciones**

3. **Procesar texto en chunks más pequeños:**
   ```yaml
   text:
     chunk_size: 1000  # Reducir tamaño
   ```

4. **Desactivar detección paralela:**
   ```yaml
   performance:
     parallel_detection: false
   ```

---

## Mejores Prácticas

### 1. Preparación del Texto

**ANTES de procesar:**

✅ **Hacer:**
- Revisar ortografía básica
- Asegurar coherencia
- Eliminar texto innecesario

❌ **Evitar:**
- Textos con muchos errores
- Mezcla de idiomas
- Formatos especiales (tablas, código)

### 2. Configuración Óptima

**Para textos cortos (<500 palabras):**
```yaml
rewriting:
  max_iterations: 3
  target_threshold: 15
ollama:
  temperature: 0.7
```

**Para textos largos (>1000 palabras):**
```yaml
rewriting:
  max_iterations: 5
  target_threshold: 10
text:
  chunk_size: 2000
```

**Para máxima humanización:**
```yaml
rewriting:
  max_iterations: 10
  target_threshold: 5
ollama:
  temperature: 0.9
  model: "qwen2.5:32b"
```

### 3. Verificación Post-Proceso

**SIEMPRE verificar:**

1. ✓ El significado se mantiene
2. ✓ No hay información incorrecta
3. ✓ El tono es apropiado
4. ✓ La gramática es correcta
5. ✓ Coherencia general

**Revisar manualmente** antes de usar el texto final.

---

## Ejemplos de Uso

### Ejemplo 1: Análisis Rápido

```bash
# Solo analizar, no humanizar
python -m src.main --language es --input texto.txt

# En el prompt:
¿Deseas humanizar este texto? N
```

### Ejemplo 2: Humanización Estándar

```bash
python -m src.main \
  --language es \
  --input ensayo.txt \
  --max-iterations 5 \
  --threshold 15
```

### Ejemplo 3: Máxima Calidad

```bash
# Editar config.yaml primero:
# model: qwen2.5:32b
# temperature: 0.9

python -m src.main \
  --language en \
  --input paper.txt \
  --max-iterations 10 \
  --threshold 5
```

### Ejemplo 4: Batch Processing

```bash
# Script para procesar múltiples archivos
for file in textos/*.txt; do
    python -m src.main \
      --language es \
      --input "$file" \
      --max-iterations 5
done
```

---

## Preguntas Frecuentes

**P: ¿Cuánto tiempo toma?**
R: Depende de la longitud del texto y número de iteraciones. Típicamente 2-10 minutos para un texto de 1000 palabras.

**P: ¿Funciona offline?**
R: Parcialmente. La IA local funciona offline, pero los detectores requieren internet.

**P: ¿Puedo usar otros modelos?**
R: Sí, cualquier modelo compatible con Ollama. Edita `config.yaml`.

**P: ¿Es 100% indetectable?**
R: No hay garantías. Los detectores mejoran constantemente.

**P: ¿Cambia el significado del texto?**
R: Se intenta mantener el significado, pero siempre verifica manualmente.

---

Para más ayuda, consulta:
- [README.md](../README.md)
- [ETHICS.md](ETHICS.md)
- [GitHub Issues](https://github.com/tu-usuario/ai-text-humanizer/issues)
